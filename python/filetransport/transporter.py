"""
File Transporter Definition
"""

import os
import time

from .file import FilesFactory
from .rule import RulesFactory

class FileTransporter:
    """
    Transporting file from one location to another location
    """

    def __init__(self):
        self.rules = FilesFactory('NONE')
        self.files = RulesFactory('RULES')

    def run(self):
        """
        Core function to check and move file
        """
        for rule in self.rules:
            incoming_files = rule.check_incoming_files()
            for f in incoming_files:
                self.files.update(f)

        for f in self.files:
            f.check_status()

        time.sleep(2)