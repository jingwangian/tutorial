#!/usr/bin/env python

"""
Start multipule thread to download url from website
"""

import os
import time
import concurrent.futures
import requests


max_workers = 2

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


WORK_DIR="incoming"

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    print('Downloading from URL: {}'.format(url))
    r = requests.get(url, timeout=timeout)
    print("Status = {} for URL = {}".format(r.status_code,url))
    time.sleep(3)
    # with urllib.request.urlopen(url, timeout=timeout) as conn:
    #     return conn.read()
    return r.text

executor =  concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

def execute_download(url, results):
    fe = executor.submit(load_url, url, 60)
    results.append((fe,url))
    return results

def check_future_list(future_list):
    """check the future in future_list
    """

    print("Enter to check_future_list")
    num = 0
    list_len = len(future_list)
    while(num <list_len):
        future = future_list[num]
        if future.done():
            future_list.pop(num)
            print("Removed {} from future_list".format(future[1]))
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))

    # print("Enter to check_future_list")
def check_incoming_files():
    """Check the input file
    
    Return a file_list
    """

    print("Enter check_incoming_files")

    files = []

    ret_list = os.listdir(WORK_DIR)

    for r in ret_list:
        if r.lower().endswith('txt'):
            file_name = os.path.join(WORK_DIR,r)
            files.append(file_name)

    return files

def get_url_list_from_file(file_name):
    """Get the url_list from the content of the file
    """
    url_list = []


    return url_list

def main():
    results = []

    while True:
        files = check_incoming_files()
        for file_name in files:
            url_list = get_url_list_from_file(file_name)

            for url in url_list:
                results = execute_download(url, results)

        check_future_list(results)

        time.sleep(2)

    print("Shutdown the executor!")
    executor.shutdown()


if __name__=='__main__':
    main()