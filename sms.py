from trycourier import Courier
def send_sms(number):
    client = Courier(auth_token="pk_prod_Y1AEKZC6XV4RS0J6VJW3EC3PTT8M")
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
