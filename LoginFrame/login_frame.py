# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals
import types
import functools

try:
    from Tkinter import *  # pylint: disable=W0614
    from tkMessageBox import *  # pylint: disable=W0614
except ImportError:
    pass


class LoginFrame(Frame):
    def callback(self, event):
        self.message.set("実行中...")
        self.throw_login_info()

    def callquit(self, event):
        self.quit()

    def throw_login_info(self):
        self.message.set("実行中...")
        self.update()
        try:
            if self.args is not None:
                self.result = self.func(self.username.get(), self.password.get(), self.args)
            else:
                self.result = self.func(self.username.get(), self.password.get())
        except BaseException, e:
            self.quit()
            raise e
        self.message.set("")
        self.quit()

    def __init__(self, master=None, func=None, title="Login Window",
                 message=None, first_label=None, second_label=None,
                 visible=False, args=None):
        Frame.__init__(self, master)
        self.pack()

        if args is not None:
            self.args = args

        # ログイン情報を渡す関数を登録
        self.func = func

        self.master.title(title)

        self.username = StringVar()
        self.username.set("")
        self.password = StringVar()
        self.password.set("")

        if message is None:
            message = "ログイン名とパスワードを入力してください。"

        if first_label is None:
            first_label = "ログイン名"

        if second_label is None:
            second_label = "パスワード"

        input_frame = Frame(self, width=140, height=40, relief='flat',
                            borderwidth=4, bg='gray')

        main_label = Label(input_frame, text=message)
        main_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        login_label = Label(input_frame, text=first_label)
        login_label.grid(row=1, column=0, padx=5, pady=5)
        entry1 = Entry(input_frame, textvariable=self.username)
        entry1.grid(row=1, column=1, padx=5, pady=5)
        entry1.focus_set()

        passwd_label = Label(input_frame, text=second_label)
        passwd_label.grid(row=2, column=0, padx=5, pady=5)
        if visible:
            entry2 = Entry(input_frame, textvariable=self.password)
        else:
            entry2 = Entry(input_frame, textvariable=self.password, show="*")
        entry2.grid(row=2, column=1, padx=5, pady=5)

        entry1.bind('<Return>', self.callback)
        entry2.bind('<Return>', self.callback)

        self.message = StringVar()
        self.message.set("")
        message_label = Label(input_frame, textvariable=self.message, bg="gray")
        message_label.grid(row=3, column=0, padx=3, pady=5)

        input_btn = Button(input_frame, text='ログイン',
                           command=self.throw_login_info)
        input_btn.grid(row=3, column=2, padx=5, pady=5)
        input_btn.bind('<Return>', self.callback)

        exit_btn = Button(input_frame, text='キャンセル', command=self.quit)
        exit_btn.grid(row=3, column=3, padx=5, pady=5)
        exit_btn.bind('<Return>', self.callquit)

        input_frame.grid(padx=5, pady=5)


def frame_wrapper(func=None, screen_name="Input Login Info",
                  title="Login Window", message=None, first_label=None,
                  second_label=None, visible=False):

    if isinstance(func, types.FunctionType):
        # call decorator without args
        @functools.wraps(func)
        def _inner_wrapper(*args):
            root = Tk(screenName=screen_name)
            login_frame = LoginFrame(master=root, func=func, title=title,
                                     message=message, first_label=first_label,
                                     second_label=second_label, visible=visible,
                                     args=args)
            login_frame.mainloop()
            root.destroy()
            return login_frame.result
    else:
        # call decorator with args
        def _inner_wrapper(login_function):
            @functools.wraps(login_function)
            def _call_frame(*args):
                root = Tk(screenName=screen_name)
                login_frame = LoginFrame(master=root, func=login_function,
                                         title=title, message=message,
                                         first_label=first_label,
                                         second_label=second_label,
                                         visible=visible, args=args)
                login_frame.mainloop()
                root.destroy()
                return login_frame.result
            return _call_frame
    return _inner_wrapper
