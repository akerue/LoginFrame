# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

import login_frame

def sample_function(username, password):
    # Do something to log in
    print("Login Name: {}".format(username))
    print("Password: {}".format(password))
    return

def main():
    login_frame.call_frame(sample_function)

if __name__ == "__main__":
    main()
