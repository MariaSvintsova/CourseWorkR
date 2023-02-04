import json


def load_data(file_name):
    with open(file_name) as file:
        data = json.load(file)
    return data


def load_posts():
    data = load_data("data/posts.json")
    return data


def load_post(post_id):
    posts = load_posts()
    for post in posts:
        if post['pk'] == post_id:
            return post

def load_post_by_user_name(user_name):
    posts = load_posts()
    posts1 = []
    for post in posts:
        if post['poster_name'] == user_name:
            posts1.append(post)
    return posts1

def search_posts(word):
    posts = load_posts()

    search_posts = []
    for post in posts:
        if word.lower() in post['content'].lower():
            search_posts.append(post)
    return search_posts


def load_comment(post_id):
    data = load_data('data/comments.json')
    comments = []

    for comment in data:
        if comment['post_id'] == post_id:
            comments.append(comment)

    return comments
