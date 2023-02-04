import pytest

from app import app


def test_app():
    response = app.test_client().get('/api/post')
    assert response.status_code == 200
    assert len(response.data) > 1, 'ошибка апи'

def test_():
    response = app.test_client().get('/api/post/5')
    assert response.status_code == 200
    assert len(response.data) > 1, 'ошибка апи2'
