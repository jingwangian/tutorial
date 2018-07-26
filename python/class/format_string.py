#!/usr/bin/env python3

'''
Test the class in a function.

The instance will be created twice if the format_string funciont is invoked twice.

'''

def format_string(string, formatter=None):
    """Format a string using the formatter object,which is expected to have a format() emthod that accepts a string.
    """
    class DefaultFormattter:
        """Format a string in title class"""
        def format(self, string):
            return str(string).title()


    if not formatter:
        formatter = DefaultFormattter()
        print("Create a formatter instance!")


    print("formatter id = {}".format(id(formatter)))
    return formatter.format(string)

hello_string = "hello world, how are you today?"

hello_string2 = "hello mike, how are you going?"

print("input: "+ hello_string)
print("output:"+ format_string(hello_string))


print("")
print("input: "+ hello_string2)
print("output:"+ format_string(hello_string2))



