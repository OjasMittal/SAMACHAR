from trycourier import Courier
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

client = Courier(auth_token=os.getenv("AUTH_TOKEN"))
from news import Newsfeed
def send_email(name,email,interestt):
                news_feed=Newsfeed(interest=interestt,
                                   from_date=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                                   to_date=datetime.datetime.now().strftime('%Y-%m-%d'))
                print(news_feed.get())
                resp = client.send_message(
                        message={
                          "to": {
                            "email": f"{email}",
                          },
                          "content": {
                            "title": f"Your {interestt} Samachar for today",
                            "body": f"Hi {name}! \n Check out today's Samachar(News) on {interestt} \nDo not reply back to this email. \n\n {news_feed.get()}\nRegards\nSamachar",
                          },
                          "data": {"note": f"\nDo not reply back to this email. \n\n {news_feed.get()}\nRegards,\nSamachar",
                          },
                          "routing": {
                                "method": "single",
                                "channels": ["email"],
                            },
                        }
                      )
                return True
