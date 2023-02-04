import logging

from flask import Flask, render_template, request, jsonify
from utils import *

import json
from json import JSONDecodeError

app = Flask(__name__, template_folder='templates')



logger_one = logging.getLogger("one")
file_handler = logging.FileHandler('logs/api.log')
formatter_one = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter_one)
logger_one.addHandler(file_handler)


@app.route('/')
def view_posts():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:pk>')
def vie_posts(pk):
    post = load_post(pk)
    comments = load_comment(pk)
    return render_template('post.html', post=post, comments=comments)

@app.route('/users/<user_name>')
def show_posts(user_name):
    pos = load_post_by_user_name(user_name)
    return render_template('user-feed.html', pos=pos)

@app.route('/search/')
def search_posts1():
    word = request.args.get('word')
    posts = search_posts(word)
    print(posts)
    return render_template('index.html', posts=posts)


@app.route('/api/post')
def api_posts():
    posts = load_posts()
    logger_one.warning('запрос на апи')
    return jsonify(posts)


@app.route('/api/post/<int:pk>')
def api_post(pk):
    post = load_post(pk)
    logger_one.warning('чтото')
    return jsonify(post)


@app.errorhandler(404)
def error_404(e):
    return 'Такое не найдено', 404


@app.errorhandler(500)
def error_500(e):
    return 'Internal Server Error ', 500



app.run()
