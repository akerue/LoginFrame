## TK Interを用いたログインスクリプトプログラム
---
**Python 2.X**

最終更新: 2014/08/12

### 使い方
Pythonスクリプト内でユーザにユーザ名とパスワードを要求したい場合に
login_frame内のframe_wrapperデコレータを使用することでユーザにユーザ名とパスワードを
要求するGUIウィンドウを出力し、ラップされた関数にユーザの入力情報を渡すことができる．

### 使用例
sample.pyに簡単な例を載せるが，基本的にはlogin_frame.pyからframe_wrapperデコレータを呼び出せばよい．
デコレータでラップされる関数は引数にユーザ名とパスワードを定義できるが、呼び出す際には引数なしで呼び出せる．
sample.pyスクリプトでは標準出力に入力されたログインネームとパスワードを表示するのみにとどまる．
実際に使用する際にはsample_functionの中で(例えばmechanizeなどを使用して)ログイン処理を書けばよい．

### オプション
frame_wrapperデコレータはいくつかのオプションを引数に指定できる．

- title: ウィンドウのタイトルを変更できる．デフォルトは"Login Window"
- message: ウィンドウ内のメッセージを変更できる．デフォルトは"ログイン名とパスワードを入力してください。"
- first_label: 一つ目の入力欄のラベルを変更できる．デフォルトは"ログイン名"
- second_label: 二つ目の入力欄のラベルを変更できる．デフォルトは"パスワード"
- visible: Falseにすると二つ目の入力文字が"*"に変更される．デフォルトはFalse

sample.py内で定義されたsample_function2のように辞書式でオプションを追加可能

### インストール方法
```
$ sudo python setup.py install
```

