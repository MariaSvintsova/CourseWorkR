import pytest

from app import app


def test_app():
    response = app.test_client().get('/api/post')
    assert response.status_code == 200
    assert type(response.json) == list, 'ошибка апи_1'
    assert set(list(response.json[0].keys())) == {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

def test_():
    response = app.test_client().get('/api/post/5')
    assert response.status_code == 200
    assert type(response.json) == dict, 'ошибка апи_2'
    assert set(list(response.json.keys())) == {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

