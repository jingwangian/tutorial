"""
Rules Definition
"""

import endpoint

class Rule:
    def __init__(self):
        self.src_endpoint_name = ''
        self.src_endpoint = None
        self.dest_endpoint_name = ''
        self.dest_endpoint = None
        self.match_str = ''

    def check_incoming_files(self):
        """
        Return the files stat from the src_endpoint
        """

        incoming_files = []

        return incoming_files


class Rules:
    """
    A container contains all rule

    Each rule is a namedtuple as following:
    ['src_name','src_point','dest_name','dest_point','match']
    """
    def __init__(self):
        self.rules_list = []

    def get_src_endpoint(self,endpoint_name):
        """
        Find and Return the endpoint by the name
        """

        # e is a namedtuple
        for r in self.rules_list:
            if r.src_endpoint_name = endpoint_name:
                return r.src_endpoint

    def get_dest_endpoint(self,endpoint_name):
        """
        Find and Return the endpoint by the name
        """

        # e is a namedtuple
        for r in self.rules_list:
            if r.dest_endpoint_name = endpoint_name:
                return r.dest_endpoint

class RulesFactory:
    """
    Create a rules instance
    """

    def __init__(self, config_name):
        self.config_name

    def __call__(self)
        rules = []
        return rules