# ToDo-List

【概要】

Djangoのチュートリアルとして作成したTo−Doアプリです。

期限日が近くなると**ぷるぷる**と振動して視覚的に認識しやすく工夫しました。

# デモ

https://github.com/K-out-A/My-Portfolio/blob/main/media/todo_list.gif


# 使い方
### Githubからclone
Github上からソースコードをローカルPC上にcloneします。
```
$ git clone git@github.com:K-out-A/ToDo-List.git
```
cloneしたディレクトリ上に移動します。
```
$ cd MovieRecommend
```

### 動作環境の構築
仮想環境を作成します。（そのまま実行すると既存のパッケージに干渉してエラーが起きる可能性があるためです。）
```
$ python3 -m venv myvenv
```
仮想環境を実行します。
```
$ source myvenv/bin/activate
```
必要なライブラリを仮想環境上にinstallします。（requirements.txtの中に必要なライブラリのリストが入っています。）
```
$ pip3 install -r requirements.txt
```

### ソースコードの実行
以下のコードを順に実行します。
```
$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver
```

http://127.0.0.1:8000/ にアクセスして、デモ動画の冒頭ページが表示されたら成功です。

# 動作環境の詳細
- Ubuntu 18.04.5 LTS
- Python 3.7.3
- Django 3.1.2
- django_filters 2.3.0
- django-bootstrap4 2.2.0
- django-bootstrap-datepicker-plus 3.0.5
