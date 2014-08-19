# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

from LoginFrame.login_frame import *

@frame_wrapper
def sample_function(username, password):
    # Do something to log in
    print("Login Name: {}".format(username))
    print("Password: {}".format(password))
    return

@frame_wrapper(title="Other frame window", message="他のメッセージも指定可能")
def sample_function2(username, password):
    # Do something to log in
    print("Login Name: {}".format(username))
    print("Password: {}".format(password))
    return

def main():
    sample_function()

if __name__ == "__main__":
    main()
