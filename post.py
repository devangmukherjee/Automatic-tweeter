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
list=["Pexa is not safe",
"Don't know what kind of university takes exams during a pandemic",
"Our documents are at risk!",
"Enough is enough!",
"The company's software comes with virus!",
"Manipal address our problems!",
"It's high time you listen to your students",
"PEXA lite is virus laden app, its not even tested properly",
"Stop coming up with generic excuses!",
"They don't care",
"You're letting us down.",
"Borrow laptops from neighbours during lockdown",
"The circulars doesn't address any problems which we are facing",
"With all these viruses and not budging from their initial statement that PEXA Lite is safe",
"Thank you for not paying a heed to our concerns ",
"Not a single issue has been dealt with head-on."
"Ignorance, Negligence, Miscommunication, Lies!!",
"We stand united.",
"Use better platform, Institute of Eminence",
"Absolute joke of a software!",
"Handing over our personal information like this.",
"What are these people upto? it is sad.",
"Need of the hour!",
" "
]

# Posting of tweets 
for i in range(len(list)):
    try:
        #insert more hashtags if you want to here
        api.update_status(status =list[i]+" @ManipalUni"+" #BoycottPexa"+" @ugc_india") 
    except KeyboardInterrupt:
        exit()     

