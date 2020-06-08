#These declarations should be added to a config file at some point
client_id = "extremecouponing-86ad221d8eada4a080f4926f9f360d978630074420274554339"
client_secret = "HMTrTx0DubgKGqrnilwViWvFIKAAqPRLbf75pM8p"
redirect_uri = "http://localhost:4200/"

username = "extremecouponingapp@gmail.com"#If a new user wants access to this project they should have to enter this information
password = "P4ssword"

scope = "product.compact"

OAUTH2_BASE_URL = "https://api.kroger.com/v1/connect/oauth2"
API_BASE_URL = "https://api.kroger.com"

#https://developer.kroger.com/documentation/consume/tutorials/authorization
import requests, traceback
#Interacting with an API and grants the OAUTH token
#the reactive approach is requesting a new token when it's expired
#the proactive approach is refreshing when it's close to the token expiring.
#Our token is 1800 long
try:
    session = requests.Session() #Like a http request but this will store cookies. this is like urllib, but this is smarter because it will automatically follow redirects
                                 #urllib requires you to make a handler to go through and go to the redirect. more complicated.
    data = {
        "grant_type": "client_credentials",
        "scope": scope
    }
    response = session.post(OAUTH2_BASE_URL + "/token", auth=requests.auth.HTTPBasicAuth(client_id, client_secret), data=data)#params=params and headers=headers is a keyword arg. So by DEFAULT it will be params. if you want to specify it to be something else you can pass it and it will change the arg
    print(response.status_code)
    #print(response.content)
    print(response.url)
    print(response.json())
    response.close()

except:
    print(traceback.format_exc()) #General exception, print what the error is

#We should now have an authenticated token that we may use to interact with other parts of the API with.