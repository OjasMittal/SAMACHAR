import streamlit as st
from pyrebase import initialize_app
import sms
import emaill
import authorization
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import os


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

page_bg_img=f"""
<style>
[data-testid="stReportViewContainer"] > .main{{
background-image: url("https://img.freepik.com/free-vector/vector-modern-abstract-geometric-background_260559-237.jpg?size=626&ext=jpg&ga=GA1.2.1693190306.1663954344");
background-size: 110%;
background-position: top left;
background-repeat: no-repeat;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

# [data-testid="stSidebar"]> div:first-child{{
# background-image: url("data:image/jpeg;base64,{img}");
# background-position: center;
# }}
</style>
 """
hide_menu_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)
st.markdown(page_bg_img,unsafe_allow_html=True)

#Animation
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.markdown("<h1 style='text-align: center; color: #F55F0E;'>SAMACHAR</h1>", unsafe_allow_html=True)
st.subheader('Get your personalised Newspaper mailed to you')
st.write(" ")
flag = 1
if flag == 1:
    st.info("Login through login option in the left drop down menu to use this service")
    st.warning('Make sure you are not logged in with multiple gmail accounts to use google authentication')
    st.write(" ")
col1, col2 = st.columns([5, 2])
with col1:
    st.write(" ")
    st.markdown(
        "<h3 style='text-align: center; color: #FFFFFF;'>SAMACHAR helps you to get a personalised newspaper \N{newspaper} emailed  to you instantly with links of the topic which interests you!</h3>",
        unsafe_allow_html=True)

    st.write(" ")
    st.write(" ")

with col2:
    lottie_animation_1 = "https://assets5.lottiefiles.com/datafiles/98a3d0add75fc3c86f6d6f9b148c111e/Newspaper animation.json"
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key="news")
st.subheader("**Save time in todays fast running world by getting news of your interest without hogging through various webpages!**")
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Get notified by SMS as soon as your newspaper gets mailed to you.</h3>", unsafe_allow_html=True)
st.write("")
st.sidebar.markdown(
        "<h1 style='text-align: center; color: #FFFFFF;'>WELCOME !</h1>",
        unsafe_allow_html=True)
gauth = authorization.authorize()
if gauth != 2:
    st.sidebar.write("OR")
    choice = st.sidebar.selectbox('Login / SignUp to SAMACHAR', ('Login', 'SignUp'))
    st.write('<style>div.row-widget.stRadio > div {flex-direction:row;}</style>', unsafe_allow_html=True)
    email = st.sidebar.text_input("Enter your email address")
    password = st.sidebar.text_input("Enter your password", type="password")


if gauth == 2:
    flag = 0
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    with st.sidebar:
        c1, c2, c3 = st.columns([1, 4, 1])
        with c2:
            lottie_animation_2 = "https://assets1.lottiefiles.com/packages/lf20_enlitdkl.json"
            lottie_anime_json = load_lottie_url(lottie_animation_2)
            st_lottie(lottie_anime_json, key="hello")
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
    if choice == "SignUp":
        handle = st.sidebar.text_input("Please enter your nickname", value="CoolPanda")
        submit = st.sidebar.button('Create my Account')
        if submit:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.sidebar.success("Your account has been created successfully!")
                st.sidebar.success("Click on Login to continue")
                st.balloons()
                user = auth.sign_in_with_email_and_password(email, password)
                db.child(user['localId']).child("Handle").set(handle)
                db.child(user['localId']).child("Id").set(user['localId'])

            except Exception as e:
                error_message = e.args[1]
                if "EMAIL_EXISTS" in error_message:
                    st.info("This account already exists!")
                else:
                    st.success(f"Welcome {handle} !")
                    st.balloons()

    if choice == "Login":
        login = st.sidebar.checkbox('Login', key=2)
        if login:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                flag = 0
                st.sidebar.success("You have Logged in Successfully!")
                name = st.text_input("Enter your name")
                phone = st.text_input("Enter your contact number")
                email = st.text_input("Enter your email")
                interest = st.text_input("Enter your topic of interest")
                result = st.button("Get SAMACHAR")
                if result:
                    success = emaill.send_email(name,email,interest)
                    sms.send_sms(phone)
                    if success:
                        st.write("E-Newspaper Mailed Successfully!")
                        st.balloons()

            except Exception as e:
                st.info("Enter a valid email/password !")

