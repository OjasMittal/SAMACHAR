from trycourier import Courier
import os
from dotenv import load_dotenv
load_dotenv()
client = Courier(auth_token=os.getenv("AUTH_TOKEN"))
def send_sms(number):
    client.send_message(
            message={
                "to": {
                    "phone_number": f"91{number}"
                },
                "content": {
                    "title": "E-Newspaper(Samachar) mailed",
                    "body": "Your E-Newspaper(Samachar) for today has been mailed to you!"
                },
                "data": {
                    "news": "Your E-Newspaper(Samachar) for today has been mailed to you!"
                },
            }
        )
