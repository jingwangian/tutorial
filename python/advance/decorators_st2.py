#!/usr/bin/env python3

'''
Decorators study


'''

import time


class Request():
    def __init__(self, method='GET', data=None):
        self.method = method
        self.data = data


def require_http_methods(request_method_list):
    print('go into require_http_methods')

    def decorator(func):
        print('In decorator, func is {}'.format(func.__name__))

        def inner(request, *args, **kwargs):
            print('In request, request is {}'.format(vars(request)))
            if request.method not in request_method_list:
                print('Method Not Allowed')
            return func(request, *args, **kwargs)
            print('return inner')
        return inner
        print('return decorator')
    return decorator


def require_http_methods_2(func):
    print('In require_http_methods_2, func is {}'.format(func.__name__))

    def wrapper(request, *args, **kwargs):
        print('In wrapper, request is {}'.format(vars(request)))
        return func(request, *args, **kwargs)
    return wrapper


cl_request = Request('GET', 'hello world!')


@require_http_methods(["GET", "POST"])
def handle_request(request):
    print('Method: {}'.format(request.method))
    print('Data: {}'.format(request.data))

print(handle_request.__name__)
handle_request(cl_request)

cl_request_2 = Request('POST', 'Welcome to Python website')


@require_http_methods_2
def handle_request_2(request):
    print('Method: {}'.format(request.method))
    print('Data: {}'.format(request.data))

print(handle_request_2.__name__)
handle_request_2(cl_request_2)
