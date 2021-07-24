可见性与绑定 https://www.cnblogs.com/yssjun/p/9873689.html
简单起见，这里不介绍命名空间与变量查找规则LGB相关的概念。
变量的可见性+绑定
Free variable是一个比较重要的概念，在闭包中引用的父函数中的局部变量是一个free variable，而且该free variable被存放在一个cell对象中。这个会在闭包相关的文章中介绍。 

匿名函数：lambda表达式  func = lambda _i=i: _i * _i
闭包 : 闭包的三个条件
1，返回的是内函数
2，内函数-必现-使用了外函数的局部变量
3，返回的内函数中没有引用父函数中定义的local variable 不叫闭包

Python的for..in..if语法

2021年最值得测试同学使用的python库
乙醇 创建于 4 个月 之前

最后更新时间 2020-12-01

2021年最值得测试同学使用的python库

title = "2021年最值得测试同学使用的python库"
description = ""
author = "乙醇"
tags = []
2021年不期而至了，我们不妨盘点一下2021年最值得测试同学使用的python库/工具吧。

Validation
jsonschema: An(other) implementation of JSON Schema for Python
jsonschema可以用来进行json数据的校验。试想一下这样的场景，我们需要验证api返回的json字符串的正确性，但如果一个字段一个字段去校验效率自然是不高的，这时候jasonsschema就可以大展身手了。

>>> from jsonschema import validate

>>> # A sample schema, like what we'd get from json.load()
>>> schema = {
...     "type" : "object",
...     "properties" : {
...         "price" : {"type" : "number"},
...         "name" : {"type" : "string"},
...     },
... }

>>> # If no exception is raised by validate(), the instance is valid.
>>> validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

>>> validate(
...     instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema,
... )                                   # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
ValidationError: 'Invalid' is not of type 'number'
我们可以自定义schema，如果api返回的结果满足schema定义的规则的话，那么用例就通过，否则失败，用例的编写效率和准确性都可以得到提升。

项目地址:https://github.com/Julian/jsonschema

算法
algorithms:Minimal examples of data structures and algorithms in Python。
库如其名，用python实现了各种常见算法，实现优雅，例子相对简单，适合学习。 项目地址：https://github.com/keon/algorithms

命令行工具
howdoi:instant coding answers via the command line
写代码的时候经常会不知道某个功能怎么实现或者代码报错需要去搜索一下解决方案，但每次打开浏览器搜索的话还是比较麻烦的，这时候howdoi就有用武之地了。

howdoi是一个命令行工具，用法就是什么不会搜什么，比如我想用python读取文件，但不知道怎么写，那么你可以在命令行里这样做。

$howdoi python read file
with open('C:/path/numbers.txt') as f:
    lines = f.read().splitlines()
没有任何的废话，直接给你答案。

项目地址：https://github.com/gleitz/howdoi

thefuck: Magnificent app which corrects your previous console command.
人非圣贤，孰能无过，敲命令行的时候自然是很容易出错的，这时候你可能需要thefuck，这个工具可以帮你自动的修正错误命令并且运行，能较大的提升效率。



项目地址: https://github.com/nvbn/thefuck

db
tinydb
使用json进行持久化的简单数据库，提供了完整的持久化，查询等方案，数据库文件就是一个.json文件，可以用来实现配置存储，做一些小工具的开发等。

>>> from tinydb import TinyDB, Query
>>> db = TinyDB('/path/to/db.json')
>>> db.insert({'int': 1, 'char': 'a'})
>>> db.insert({'int': 1, 'char': 'b'})
项目地址: https://github.com/msiemens/tinydb

Deep Learning
tensorflow
最流行的机器学习框架，值得我们去学习和了解。

项目地址: https://github.com/tensorflow/tensorflow

installer
pyinstaller:Freeze (package) Python programs into stand-alone executables
很多同学写完python脚本以后都想把python脚本打包成exe文件或者是其他可执行文件，然后发给小伙伴们一键运行，这时候就可以试试pyinstall库，支持主流操作系统，推荐给有分发需求的同学。

项目地址: https://github.com/pyinstaller/pyinstaller

Downloader
you-get
命令行下载工具，支持油管和b站，特别是b站可以直接下载一个视频的所有part，强烈推荐。

Environment Management
关于环境管理就放在一起介绍。

pyenv - Simple Python version management. 我最常用的安装python的工具，支持多个python版本共存和切换，强烈推荐。
virtualenv - A tool to create isolated Python environments. 这个库可以创建一个虚拟环境，每个虚拟环境里pip安装的第三方依赖都是隔离的，可以完美解决不同的库依赖同一个库的不同版本的问题，也可以让site pakcage 干净整洁，适合有洁癖和强迫症的同学。
GUI
Gooey: Turn (almost) any Python command line program into a full GUI application with one line
一个可以将命令行工具转换成gui的神奇工具，需要的代码量很少，适合做各种小工具，测试开发同学可以考虑一下。

项目地址: https://github.com/chriskiehl/Gooey

PySimpleGUI
star很高的gui库，没用过，不好评论，不过看代码的描述性很强，推荐有兴趣的同学尝试一下。

import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window
项目地址: https://github.com/PySimpleGUI/PySimpleGUI

html/xml parser
解析html和xml工具很多，我个人用过以下两个。

pyquery https://github.com/gawel/pyquery: 提供了类似jquery语法的解析语法，适合像我这样有上个世代前端开发经验的同学。
Beautiful Soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/: 最流行的html/xml解析库，适合大部分同学和大部分场景。
http client
requests A simple, yet elegant HTTP library.
用起来最舒服也是最流行的python http client，简单优雅，居家常备。

>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"type":"User"...'
>>> r.json()
{'disk_usage': 368627, 'private_gists': 484, ...}
项目地址: https://github.com/psf/requests

ORM
peewee a small, expressive orm -- supports postgresql, mysql and sqlite
peewee的代码风格符合直觉，使用简单，学习成本相对较低，推荐测试开发同学使用。

from peewee import *
import datetime


db = SqliteDatabase('my_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
项目地址: https://github.com/coleifer/peewee

安全测试
fsociety Hacking Tools Pack – A Penetration Testing Framework
提供一整套解决方案的安全测试框架。

项目地址: https://github.com/Manisso/fsociety

静态站点生成
pelican Static site generator that supports Markdown and reST syntax. Powered by Python.
python实现的静态博客生成器，流行度很高，适合有需求的同学。

项目地址: https://github.com/getpelican/pelican

测试库
pytest https://docs.pytest.org/en/latest/
最强大的python测试框架，特性丰富，功能强大，入门成本低，精通成本高，但基本上你需要的功能这个框架都能提供。

unittest
自带的测试框架，基本属于必修课了。

fake2db: create custom test databases that are populated with fake data
构建测试数据库以及测试数据的库。

项目地址: https://github.com/emirozer/fake2db

Faker is a Python package that generates fake data for you.
最流行的造数据的库，很贴心的支持中文。

from faker import Faker
fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'
项目地址: https://github.com/joke2k/faker

爬虫
requests-html Pythonic HTML Parsing for Humans
用起来非常简单顺手的爬虫工具，简单的爬虫需求可以用这个。

项目地址: https://github.com/psf/requests-html

pyspider A Powerful Spider(Web Crawler) System in Python.
非常流行的爬虫框架，适合复杂的爬虫项目。

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://scrapy.org/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
项目地址: https://github.com/binux/pyspider

web开发
django https://www.djangoproject.com/: python生态最丰富的MVC框架，基本是python web开发的王者。
flask https://flask.palletsprojects.com/en/1.1.x/: 简单的web开发框架，上手容易，性能尚可，最适合做简单的页面和接口。