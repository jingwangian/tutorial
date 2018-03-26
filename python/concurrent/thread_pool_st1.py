#!/usr/bin/env python

"""
Start multipule thread to download url from website
"""

import concurrent.futures
import urllib.request
import requests


max_workers = 1

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    print('Downloading from URL: {}'.format(url))
    r = requests.get(url, timeout=timeout)
    print("Status = {} for URL = {}".format(r.status_code,url))
    # with urllib.request.urlopen(url, timeout=timeout) as conn:
    #     return conn.read()
    return r.text

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))


# r = requests.get(URLS[0], timeout=10)
# print(r.text)