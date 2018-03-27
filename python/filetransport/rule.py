#!/usr/bin/env python

"""
EndPoint Definition
"""

import endpoint

class Rule:
    def __init__(self):
        self.src_endpoint = None
        self.dest_endpoint = None
        self.match_str = ''


class Rules:
    """
    A container contains all rule

    Each rule is a namedtuple as following:
    ['src_name','src_point','dest_name','dest_point','match']
    """
    def __init__(self):
        self.rules_list = []

    def get_endpoint(self,endpoint_name, src=True):
        """
        Find and Return the endpoint by the name
        """
        if src:
            # e is a namedtuple
            for e in self.rules_list:
                if e['name'] = endpoint_name:
                    return e['endpoint']


# class RulesFactory(NamedConfiguration):
#     """
#     Return the a list contains all rule
#     """
#     pass


def get_rules(*args):

    rule_list = []

    return rule_list