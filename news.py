import requests
class Newsfeed:
    base_url='https://newsapi.org/v2/everything?'
    api_key= "f6fcf829fb5840cd8695085bc153b89d"
    def __init__(self,interest,from_date,to_date,language='en'):
        self.interest=interest
        self.from_date=from_date
        self.to_date=to_date
        self.language=language
    def get(self):
        url=f'{self.base_url}' \
        f'qInTitle={self.interest}&' \
        f'from={self.from_date}&' \
        f'to={self.to_date}&' \
        f'language={self.language}&' \
        f'apiKey={self.api_key}'

        response=requests.get(url)
        content=response.json()
        x=content['articles']

        email_body=''
        for i in x:
          email_body= email_body + i['title']+"\n"+ i['url']+"\n\n"
          #print(email_body)
        return email_body
