#!/usr/bin/env python3

import sys
from xml.parsers.expat import ParserCreate, ExpatError, errors

# 3 handler functions
def start_element(name, attrs):
    print('Start element:', name, attrs)
def end_element(name):
    print('End element:', name)
def char_data(data):
    print('Character data:', repr(data))

p = ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

file_name='bookstore.xml'


with open(file_name,'rb') as f:
	try:
		p.Parse(f.read(), 1)
	except ExpatError as err:
		print("Error in line [{}] with offset[{}], reason:".format(err.lineno,err.offset), errors.messages[err.code])
