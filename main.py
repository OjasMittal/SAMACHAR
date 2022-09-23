import streamlit as st
from pyrebase import initialize_app
import sms
import emaill
import authorization
from PIL import Image
from annotated_text import annotated_text
from streamlit_lottie import st_lottie
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Work to do:
# 1.Add background image
# 2.encrypt secrets
# 3.Understand session state and authorisation
# 4.Try stopping rerunning of code
# 5.Create proper requirements.txt and Host on server

firebaseConfig = {
    'apiKey': os.getenv("API"),
    'authDomain': "samachar-e33a2.firebaseapp.com",
    'projectId': "samachar-e33a2",
    'databaseURL': "https://samachar-e33a2-default-rtdb.asia-southeast1.firebasedatabase.app",
    'storageBucket': "samachar-e33a2.appspot.com",
    'messagingSenderId': "68385710600",
    'appId': "1:68385710600:web:f06eed39e12f99a49327bd",
    'measurementId': "G-HFS4FHMB2L"
}

firebase = initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

img = Image.open('icon.jpeg')
st.set_page_config(page_title="SAMACHAR", page_icon=img)


# Animation
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.title("SAMACHAR")
st.subheader('Get your personalised Newspaper mailed to you')
st.write(" ")
flag = 1
if flag == 1:
    st.info("Login through login option in the left drop down menu to use this services")
    st.write(" ")
col1, col2 = st.columns([3, 2])
with col1:
    st.write(" ")
    st.write(
        f"\n**SAMACHAR helps you to get a personalised newspaper\N{newspaper} emailed  to you with links of the topic which interest you.**")
    st.write(" ")
    st.write(" ")
    annotated_text(("Get notified by sms","","#8ef"),("as soon as your newspaper gets mailed to you.","","#faa"))
with col2:
    lottie_animation_1 = "https://assets10.lottiefiles.com/datafiles/98a3d0add75fc3c86f6d6f9b148c111e/Newspaper animation.json"
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key="news")

st.sidebar.title("WELCOME!")
gauth = authorization.authorize()
if gauth != 2:
    st.sidebar.write("OR")
    choice = st.sidebar.selectbox('Login / SignUp to SAMACHAR', ['Login', 'Sign up'])
    email = st.sidebar.text_input("Enter your email address")
    password = st.sidebar.text_input("Enter your password", type="password")


if gauth == 2:
    name = st.text_input("Enter your name")
    phone = st.text_input("Enter your contact number")
    email = st.text_input("Enter your email")
    interest = st.text_input("Topic you want news of: ")
    result = st.button("Get SAMACHAR")
    if result:
        success = emaill.send_email(name, email, interest)
        sms.send_sms(phone)
        if success:
            st.write("E-Newspaper Mailed Successfully!")
else:
    if choice == "Sign up":
        handle = st.sidebar.text_input("Please enter your nickname", value="CoolPanda")
        submit = st.sidebar.button('Create my Account')
        if submit:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Your account is created successfully!")
                st.balloons()
                user = auth.sign_in_with_email_and_password(email, password)
                db.child(user['localId']).child("Handle").set(handle)
                db.child(user['localId']).child("Id").set(user['localId'])

            except:
                st.info("This account already exists !")

    if choice == "Login":
        login = st.sidebar.checkbox('Login', key=2)
        if login:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                flag = 0
                name = st.text_input("Enter your name")
                phone = st.text_input("Enter your contact number")
                email = st.text_input("Enter your email")
                interest = st.text_input("Enter your topic of interest")
                result = st.button("Get SAMACHAR")
                if result:
                    success = emaill.send_email(name, email, interest)
                    sms.send_sms(phone)
                    if success:
                        st.write("E-Newspaper Mailed Successfully!")
                        st.balloons()

            except:
                st.info("Enter a valid email/password !")
