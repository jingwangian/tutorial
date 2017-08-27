#!/usr/bin/env python3

"""
aws_lambda test
This is a client send HTTP request to AWS API which invoke
lambda after it.
"""

import requests
import time

t1 = time.time()
# r = requests.get('https://jnw8opkw25.execute-api.ap-southeast-2.amazonaws.com/prod/hello', auth=('user', 'pass'), timeout=8)
# r = requests.post('https://jnw8opkw25.execute-api.ap-southeast-2.amazonaws.com/prod/hello', data={'name': 'wangj', 'age': '55'})

post_data = {'name': 'wangj', 'age': '55'}
r = requests.post('https://jnw8opkw25.execute-api.ap-southeast-2.amazonaws.com/up/hello', auth=('user', 'pass'), data=post_data,)

t2 = time.time()

print(r.headers)
print(r.text)

print('[{} seconds]'.format((t2 - t1)))

# print(r.json)
