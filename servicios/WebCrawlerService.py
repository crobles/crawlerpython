from flask_restful import Resource, Api, abort,reqparse
from flask import jsonify, request
import json

class WebCrawler(Resource):
    def post(self):
        from bs4 import BeautifulSoup
        import logging
        import requests
        import sys
        sys.path.append('../')
        import json
        try:
            logging.basicConfig(level = logging.INFO)
            args = request.get_json(force=True)
            logging.info("request : "+str(args))
            if args['Url'] is not None:
                page = requests.get(args['Url'])
                print(page.status_code)
                soup = BeautifulSoup(page.content, 'html.parser')    
            response = {'Status_code' : page.status_code, 'Message':'Dump DONE'}
            logging.info("response : "+str(response))
            
        except Exception as e:
            logging.error("Exception {}".format(e))
            
        return response


# ----------------
# import requests
# from bs4 import BeautifulSoup

# url = "https://articulo.mercadolibre.cl/MLC-463906296-skis-atomic-expert-hv-series-6-con-fijaciones-_JM"
# page = requests.get(url)

# # print(page.status_code)

# # print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())

# print(soup)