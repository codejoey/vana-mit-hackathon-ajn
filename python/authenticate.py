import urllib.request as request
from urllib import parse as parse
import json

url="https://api.vana.com/api/v0/"

hdrs = {
	"Content-Type" : "application/json",
}

data={}
#parses data into the proper form for urllib requests
def par(data):
	return parse.urlencode(data).encode()
#makes the requests, and returns the response
def make_req(urladd, data, headers=None):
	req = request.Request(url+urladd, data=par(data))
	resp = request.urlopen(req)
	return resp.read().decode("utf-8")

#create the login
data['email'] = input("email:")
make_req("auth/create-login", data)
#use the user-submitted code to generate the auth token
data["code"]=input("Authentication Code:")
auth = json.loads(make_req("auth/login", data))
auth = "Bearer "+auth['token']

#save the auth token to the computer
f = open('auth', 'w')
f.write(auth)
f.close()

g = open('email', 'w')
g.write(data['email'])
g.close()