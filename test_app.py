from app import app
import pytest,json
from flask import g, session


def test_WebCrawler():
    response = app.test_client().post(
        '/api/v1/WebCrawler', 
        data=json.dumps({'Url': 'https://www.google.com'}),
        content_type='application/json'
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['Message'] == 'Dump DONE'


def test_WebCrawler_Exception():
    response = app.test_client().post(
        '/api/v1/WebCrawler', 
        data=json.dumps({'Url': 'hola'}),
        content_type='application/json'
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 500
    


def test_ListWebCrawler():
    response = app.test_client().post(
        '/api/v1/ListWebCrawler',
        data = json.dumps({'UrlList':'https://www.amazon.com/s?k=comb&rh=n%3A16323081&ref=nb_sb_noss'}),
        content_type = 'application/json'
    )
    data = json.loads(response.get_data(as_text = True))
    assert response.status_code == 200
    assert data['BaseUrl'] == "https://www.amazon.com"

def test_ListWebCrawler_Exception():
    response = app.test_client().post(
        '/api/v1/ListWebCrawler', 
        data=json.dumps({'UrlList': 'hola'}),
        content_type='application/json'
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 500 
 