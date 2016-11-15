# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

from LoginFrame.login_frame import *


@frame_wrapper
def sample_function(username, password, args):
    # Do something to log in
    print("Login Name: {}".format(username))
    print("Password: {}".format(password))
    print("args: {}".format(args))
    return username, password


@frame_wrapper(title="Other frame window", message="他のメッセージも指定可能")
def sample_function2(username, password, args):
    # Do something to log in
    print("Login Name: {}".format(username))
    print("Password: {}".format(password))
    print("args: {}".format(args))
    return username, password


def main():
    print(sample_function())
    print(sample_function2("args"))

if __name__ == "__main__":
    main()
