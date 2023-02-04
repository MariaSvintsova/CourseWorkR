import pytest
from utils import *


def test_load_data():
    assert type(load_data('data/posts.json')) == list, 'ошибка для ф1'
    assert type(load_data('data/posts.json')[0]) == dict, 'ошибка для ф1'

def test_load_posts():
    assert type(load_posts()) == list, 'ошибка для ф2'
    assert type(load_posts()[0]) == dict, 'ошибка для ф2'

def test_search_posts():
    assert type(load_post(3)) == dict, 'ошибка для ф3'

def test_load_post_by_user_name():
    assert type(load_post_by_user_name('leo')) == list, 'ошибка для ф4'
    assert type(load_post_by_user_name('leo')[0]) == dict, 'ошибка для ф4'

def test_search_post():
    assert type(search_posts('еда')) == list, 'ошибка для ф5'
    assert type(search_posts('еда')[0]) == dict, 'ошибка для ф5'

def test_load_comment():
    assert type(load_comment(3)) == list, 'ошибка для ф6'

