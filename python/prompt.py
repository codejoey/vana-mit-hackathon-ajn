import urllib.request as request
from urllib import parse as parse
import json


def par(data):
	return parse.urlencode(data).encode()

url="https://api.vana.com/api/v0/"

#Read the authentication file
f = open('auth', 'r')
auth = f.read()
f.close()

g = open('email', 'r')
email = g.read()
g.close()

#Generate test request to check if auth token is valid.
req = request.Request(url+"account/balance")
req.add_header('Authorization', auth)
resp = request.urlopen(req)
print(resp.read())

#Take user input for request data
data = {}
data['email']=email
data['exhibit_name'] = input("Exhibit Name: ") or "slfjoIEFKJdkshfsj"
data['prompt'] = input("Prompt: ") or "{target_token}"
data["seed"]=int(input("Seed [default:-1]: ") or "-1")
data["n_samples"]=int(input("Number of samples [default: 10]: ") or 10)
data["ddim_steps"]=int(input("Steps [default:200]: ") or 200)

#make the request and print it to the console
req = request.Request(url+'jobs/text-to-image', data=par(data))
req.add_header('Authorization', auth)
resp = request.urlopen(req)
print(resp.read())
 

"""
1. grab text paragraph chuck it in
2. clean up text (remove "and, or, the"), chuck it in.'

3. output pdf with illustrations information


# EMOTION classifier for book
** ADD EMOJIS TO text


"""

#round vector graphic emoji style sticker of {target_token} emoji bright color vivid funny sticker pop style fun emoticon emotive emotional round