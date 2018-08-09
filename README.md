このプログラムは[Cory Althoff the self-taught PROGRAMMER](https://theselftaughtprogrammer.io/) 
に出てきたwebスクレイピングのコードを手本にYukiya025が作りました。
# 開発環境
- cloud9
- Python2.7
- BeautifulSoup4.6.0
- urllib2

# このプログラムの挙動
1. 指定されたウェブページ上で<a></a>タグをすべて集める。
2. その中でhrefタグを持っているものを絞り込み、さらにhrefタグにhtmlを含んだ文字列をbash画面に表示
 

# このプログラムの使い方
1. あなたがお使いのPythonのバージョンを確認します。Python2であればOK! Python3であれば多少のエラーが出ます (urllib周辺)。
2. BeautifulSoup4.6.0をインストールします。
3. python_ex289_ex293.pyを実行してください。
 
# 手本とは異なる部分
- 手本はPython3ですが、本コードはPython2.7で書きました。
- 手本では[Google news](https://news.google.com) をスクレイピング対象にしているが、現在のGoogle newsはhrefタグなどを使っておらず、まったく記事を抽出できないため、[BeautifulSoupドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) をスクレイピング対象としました。


     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Python project on Cloud9 IDE!

To show what Cloud9 can do, we added a basic sample web application to this
workspace, from the excellent Python tutorial _Learning Python the Hard Way_.
We skipped ahead straight to example 50 which teaches how to build a web
application.

If you've never looked at the tutorial or are interested in learning Python,
go check it out. It's a great hands-on way for learning all about programming
in Python.

* _Learning Python The Hard Way_, online version and videos: 
http://learnpythonthehardway.org/book/

* Full book: http://learnpythonthehardway.org

## Starting from the Terminal

To try the example application, type the following in the terminal:

```
cd ex50
python bin/app.py
```

Alternatively, open the file in ex50/bin and click the green Run
button!

## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide.