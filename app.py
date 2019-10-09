from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
import logging
import sys
import json
from servicios.WebCrawlerService import WebCrawler,ListWebCrawler

sys.path.append('../')


app = Flask(__name__)
api = Api(app)


api.add_resource(WebCrawler,'/api/v1/WebCrawler')
api.add_resource(ListWebCrawler,'/api/v1/ListWebCrawler')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='5004')
