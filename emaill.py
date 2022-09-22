from trycourier import Courier
import datetime

client = Courier(auth_token="pk_prod_Y1AEKZC6XV4RS0J6VJW3EC3PTT8M")
from news import Newsfeed
def send_email(name,email,interestt):
                news_feed=Newsfeed(interest=interestt,
                                   from_date=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                                   to_date=datetime.datetime.now().strftime('%Y-%m-%d'))
                client.send_message(
                        message={
                          "to": {
                            "email": f"{email}",
                          },
                          "content": {
                            "title": f"Your {interestt} Samachar for today",
                            "body": f"Hi {name}! \n Check out todays Samachar on {interestt} \nDo not reply back to this email \n\n {news_feed.get()}\nSamachar",
                          },
                          "data": {"note" : f"\nDo not reply back to this email \n\n {news_feed.get()}\nSamachar",
                          },
                          "routing": {
                                "method": "single",
                                "channels": ["email"],
                            },
                        }
                      )
                return True
