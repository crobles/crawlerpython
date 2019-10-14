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
        import json,re,os
        try:
            logging.basicConfig(level = logging.INFO)
            args = request.get_json(force=True)
            logging.info("request : "+str(args))
            filename=re.findall(r'/\w\d+\w+/',args['Url'])
            header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

            if args['Url'] is not None:
                page = requests.get(args['Url'],headers=header)
                print(page.status_code)
                soup = BeautifulSoup(page.content, 'html.parser')    
            response = {'Status_code' : page.status_code, 'Message':'Dump DONE'}
            print(soup)
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            my_file = os.path.join(THIS_FOLDER, str(args['Url'])+'.html')
            f = open (str(filename).replace(".","").replace("http://","").replace("https://","").replace("/","")+'.html','w')
            f.write(str(soup))
            f.close()
            logging.info("response : "+str(response))
            
        except Exception as e:
            logging.error("Exception {}".format(e))
            
        return response

class ListWebCrawler(Resource):
    def post(self):
        from bs4 import BeautifulSoup
        import logging
        import requests
        import sys
        sys.path.append('../')
        import json,re
        try:
            logging.basicConfig( level = logging.INFO)
            args = request.get_json(force=True)
            logging.info("request : "+str(args))
            NextPage = None
            ListOfUrl = []
            baseUrl = None
            header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
            if args['UrlList'] is not None:
                baseUrl = re.findall(r'^.+?[^\/:](?=[?\/]|$)',args['UrlList'])
                page = requests.get(args['UrlList'],headers=header)
                soup = BeautifulSoup(page.content,'html5lib')
                # '''
                # patron de amazon href = a-link-normal a-text-normal (textos con links)
                # patron para amazon href = a-last (paginacion)
                # esto debe ser una variable y depender de la url base
                # '''
               
                for item in soup.find_all('a',{'class':'a-link-normal a-text-normal'},href=True):
                    ListOfUrl.append(str(baseUrl[0])+item.get('href'))
                for a in soup.findAll('li',{'class':'a-last'}):
                    for b in a.findAll('a'):
                        
                        NextPage=str(baseUrl[0])+b.get('href')
             
            response = {'Status_code' : page.status_code, 'BaseUrl':baseUrl[0],'NextPageUrl':NextPage, 'ListOfUrl':ListOfUrl}
            # print(response)
            return response

        except Exception as e:
            logging.error("Exception {}".format(e))
            


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