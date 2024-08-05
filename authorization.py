import streamlit as st
import asyncio
from SessionState import get
from httpx_oauth.clients.google import GoogleOAuth2
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT")
client_id = CLIENT_ID
client_secret = CLIENT_SECRET


async def write_authorization_url(client,
                                  redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile","email"],
       # extras_params={"access_type": "offline"},
    )
    return authorization_url


async def write_access_token(client,
                             redirect_uri,
                             code):
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_email(client,
                    token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


def main(user_id, user_email):
    st.sidebar.write(f"You're logged in as {user_email}")


def authorize():
    client = GoogleOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(
        write_authorization_url(client=client,
                                redirect_uri=redirect_uri)
    )

    session_state = get(token=None)
    if session_state.token is None:
        try:
            code = st.experimental_get_query_params()['code']
        except:
            st.sidebar.write(f'''<h1>
                     <a target="_self"
                    href="{authorization_url}"><img src='data:image/png;base64,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'width="270"height="50"></a></h1>''',
                             unsafe_allow_html=True)
        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    write_access_token(client=client,
                                       redirect_uri=redirect_uri,
                                       code=code))


            except:
                st.sidebar.write(f'''<h1>
                        Session Expired ReLogin <a target="_self"
                        href="{authorization_url}"><img src='data:image/png;base64,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'width="270"height="50"></a></h1>''',
                         unsafe_allow_html=True)

            else:
                # Check if token has expired:
                if token.is_expired():
                    if token.is_expired():
                        st.write(f'''<h1>
                            Login session has ended,
                            please <a target="_self" href="{authorization_url}">
                            login</a> again.</h1>
                            ''')
                else:
                    session_state.token = token
                    user_id, user_email = asyncio.run(
                        get_email(client=client,
                                  token=token['access_token'])
                    )
                    session_state.user_id = user_id
                    session_state.user_email = user_email
                    main(user_id=session_state.user_id,
                         user_email=session_state.user_email)
                    return 2

    else:
        main(user_id=session_state.user_id,
             user_email=session_state.user_email)
        return 2
