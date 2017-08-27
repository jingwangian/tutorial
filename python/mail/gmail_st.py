#!/usr/bin/env python3

import email
import imaplib
import ctypes
import getpass


def read_inbox():
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    unm = input("Please enter your mail id : ")
    pwd = getpass.getpass("Please input your password: ")

    mail.login(unm, pwd)
    mail.select("INBOX")

    retcode, message = mail.search(None, '(UNSEEN)')


def main():


if __name__ == '__main__':
    main()
