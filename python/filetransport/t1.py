#!/usr/bin/env python

"""
Start multipule thread to download url from website
"""

import os
import time
import concurrent.futures
import requests

class FileTransport:
    """
    Move the file from src to dest.
    """
    def __init__(self):
        self.rules = []
        self.endpoint_list = []
        self.file_list = []

    def init_rules(self):
        pass

    def init_endpoint(self, endpoint_name):
        pass

    def run(self):
        """
        Checking files status and make some actions
        """
        for r in self.rules:
            files_state = r[0].get_files_state(r[1])
        

class EndPoint:
    """
    Hold a endpoint information
    """
    pass

class FileStatus:
    """
    Hold a file status information
    """
    pass


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