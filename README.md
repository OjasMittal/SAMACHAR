# SAMACHAR
## Inspiration
In today's fast-running world, people don't get time to hogg from one website to another to check for news related to a particular topic, so **SAMACHAR** (i.e. News in the Hindi language) is here to solve this problem!

## What it does
SAMACHAR  helps its user to get a personalized **newspaper mailed** to their email id along with an **SMS** on their phone number notifying them about the delivery of their E-Newspaper.
As the newspaper is mailed, the news links are getting stored with the user for future reference.

## How I built it
I used Python's Streamlit framework along with HTML/CSS to make this app. I also used Firebase and Google's OAuth authentication to get a highly secured user authentication system along with use of a session state system to store authentication tokens so that the user remains signed in for the entire time he/she is on the app.
I used the API of  newsapi.org to get the news of users' interest, used Courier's Email service with Gmail as a provider along with Courier's SMS service with Twilio as the provider.

## Challenges I ran into
For making this website highly secure, implementing Google's OAuth along with storing access tokens was a challenging task for me.

## Accomplishments that I am proud of
-Doing the research, and constructing the backend as well as the front end all alone.
-Ensuring a high-security level of website for my users by implementing various authentications.
-Making a quality app with styling, animations, and security that will make the life of people easy and help them save their precious time.

## What I learned
-Using Courier's developer-friendly platform.
-Integrating APIs.
-Implementing Google Authentication.
-Using session state to store tokens.
-Using firebase authentication and database management system.
-Implementing CSS/HTML within Streamlit framework.
-Putting Animations on the website.

## What's next for SAMACHAR
Implementing Machine Learning algorithms to provide news in sorted order from most to least trending news.
