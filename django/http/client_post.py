#!/usr/bin/env python3

import requests

data = dict(choice=2, Vote='vote')
print(data)
url = 'http://127.0.0.1:8000/polls/1/vote/'

# print(dir(requests.get))
r = requests.get(url='http://127.0.0.1:8000/polls/1')
print(r.request.headers)
print(r.status_code)

print(r.text)
print(r.headers)
r = requests.post(url=url, data=data)
print(r.status_code)
print(r.text)
