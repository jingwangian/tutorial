#!/usr/bin/env python3
"""
If str.find() function is allowed to be used then using str_search.search
will be simple, otherwise using bf_search.search

test_search.py is used to make a unittest
"""
from bf_search import search
#from str_search import search

OUTPUT = '{} "{}"'

def main():
    text = input("Input text:")
    sub_text = input("Input sub_text:")

    results = [i for i in search(text, sub_text)]
    if results:
        print(OUTPUT.format(sub_text, ",".join(map(str, results))))
    else:
        print(OUTPUT.format(sub_text, "<No Output>"))

if __name__ == '__main__':
    main()
