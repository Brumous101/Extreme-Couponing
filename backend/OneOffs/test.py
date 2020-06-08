client_id = "kylejohnson-845c39a6fa9fb3c5bfa53bbfee7caacd3769168004044038667"
client_secret = "x1rgspLW5J6FWqrncVQlkw9WiVpORpXxqJaFGSNI"
redirect_uri = "https://example.com/callback"

scope = "product.compact"

OAUTH2_BASE_URL = "https://api.kroger.com/v1/connect/oauth2"
API_BASE_URL = "https://api.kroger.com"

#https://developer.kroger.com/documentation/consume/tutorials/authorization
import requests, traceback
#This is how we would do something if we had a client that wanted to interact with their personal kroger products
try:
    session = requests.Session() #Like a http request but this will store cookies. this is like urllib, but this is smarter because it will automatically follow redirects
                                 #urllib requires you to make a handler to go through and go to the redirect. more complicated.
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": scope
    }
    headers = {
        "Cache-Control": "no-cache"
    }
    response = session.get(OAUTH2_BASE_URL + "/authorize", params=params, headers=headers)#params=params and headers=headers is a keyword arg. So by DEFAULT it will be params. if you want to specify it to be something else you can pass it and it will change the arg
    print(response.status_code)
    #print(response.content)
    print(response.url)
    response.close()
except:
    print(traceback.format_exc()) #General exception, print what the error is