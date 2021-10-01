# importing the module 
import tweepy 


# personal information 
api_key = "insert your api key here"
api_secret_key = " insert your API secret key here"
access_token = "insert your Access token here"
access_token_secret ="insert your Access token secret here"


# authentication 
auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret) 


# authentication of access token and secret 
api = tweepy.API(auth) 


#put your tweets here
#some of these tweets have been taken from the top section of the hashtag #BoycottPexa,credit goes to the respective users 
list=[
"INSERT YOUR TWEETS HERE"
]

# Posting of tweets 
for i in range(len(list)):
    try:
        #insert more hashtags if you want to here
        api.update_status(status =list[i]+" @MAHE_Manipal"+" #BoycottPexa"+" @ugc_india") 
    except KeyboardInterrupt:
        exit()     

