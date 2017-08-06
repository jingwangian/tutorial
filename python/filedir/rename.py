#!/usr/bin/env python3

'''
file operation
'''

import os
import json

dir_name = '/db/github/tutorial/python/flight_price/final_results'


def get_file_list(dir_name):
    file_list = []

    for root, dirs, files in os.walk(dir_name):
        file_list = [os.path.join(root, file) for file in files]

    return file_list


def rename_file(dir_name):
    for org_file in get_file_list(dir_name):
        renamed_file = org_file.replace('.txt', '.json')
        rename_cmd = 'mv {} {}'.format(org_file, renamed_file)
        print('---->' + rename_cmd)
        os.system(rename_cmd)


def jsonl_2_json(dir_name):
    content_dict = dict()

    for file in get_file_list(dir_name):
        print('---->convert {}'.format(file))
        with open(file, 'r') as f:
            content_dict = json.load(f)

        with open(file, 'w') as f:
            json.dump(content_dict, f, indent=2, sort_keys=True)

jsonl_2_json(dir_name)
