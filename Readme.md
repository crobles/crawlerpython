Contenedor Crawler's
============

Docker con imagen base **registrysecaas.azurecr.io/secaas/python:3-latest**

**Librerias necesarias:**
* Flask===1.0.2
* Flask-RESTful===0.3.7
* pip===19.0.2
* requests===2.21.0
* bs4
* html5lib

Compilación de contenedor

> docker build -t crawler-python .

Ejecución de contenedor con ip y puerto **(Linux)** :
> docker run -it -v $(pwd):/app -p $(ifconfig |grep "inet "|awk '{print $2}'|grep 192):5004:5004 crawler-python

El contenedor levanta una ***RESTful API*** con Flask



Servicio Flask
------------

~~~python
from servicios.WebCrawlerService import WebCrawler,ListWebCrawler

sys.path.append('../')


app = Flask(__name__)
api = Api(app)


api.add_resource(WebCrawler,'/api/v1/WebCrawler')
api.add_resource(ListWebCrawler,'/api/v1/ListWebCrawler')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='5004')


~~~



### Consumo de Servicio ###
**NodeJs [POST]**
Los campos agregados en el Body son Obligatorios

**/api/v1/ListWebCrawler**
~~~javascript

var request = require("request");

var options = { method: 'POST',
  url: 'http://192.168.40.167:5004/api/v1/ListWebCrawler',
  headers: 
   { 'postman-token': '5414796c-00f5-2bcc-1c43-9cf3d1fb9100',
     'cache-control': 'no-cache' },
  body: '{\n\t"UrlList" : "https://www.amazon.com/s?k=combos&rh=n%3A16310101%2Cn%3A16323081&dc&qid=1570708894&rnid=2941120011&ref=sr_nr_n_2"\n}' };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});



~~~


**Response**
~~~json 
{
    "Status_code": 200,
    "BaseUrl": "https://www.amazon.com",
    "NextPageUrl": "https://www.amazon.com/s?i=specialty-aps&srs=18345430011&page=2&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&ref=sr_pg_1",
    "ListOfUrl": [
        "https://www.amazon.com/Amazon-Brand-Flex-Size-Regular/dp/B074CR89QG/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-1&srs=18345430011",
        "https://www.amazon.com/Xbox-Wireless-Controller-Black-one/dp/B01LPZM7VI/ref=sr_1_2?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-2&srs=18345430011",
        "https://www.amazon.com/OEM-Windows-Home-64-Bit-1-Pack/dp/B00ZSI7Y3U/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-3&srs=18345430011",
        "https://www.amazon.com/TP-Link-HS100-Required-Google-Assistant/dp/B0178IC734/ref=sr_1_4?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-4&srs=18345430011",
        "https://www.amazon.com/AmazonBasics-High-Speed-HDMI-Cable-1-Pack/dp/B014I8SSD0/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-5&srs=18345430011",
        "https://www.amazon.com/Victrola-Bluetooth-Suitcase-Turntable-Turquoise/dp/B00UMVVUOC/ref=sr_1_6?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-6&srs=18345430011",
        "https://www.amazon.com/Victrola-Bluetooth-Suitcase-Turntable-Turquoise/dp/B00UMVVUOC/ref=sr_1_6?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-6&srs=18345430011",
        "https://www.amazon.com/Tumi-Global-Double-Billfold-Blocking/dp/B01N7OQ3BC/ref=sr_1_7?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&qid=1571064290&sr=8-7&srs=18345430011",
        "https://www.amazon.com/Nintendo-Switch-Pro-Controller/dp/B01NAWKYZ0/ref=sr_1_8?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-8&srs=18345430011",
        "https://www.amazon.com/AmazonBasics-Everyday-Alkaline-Batteries-8-Pack/dp/B00MH4QM1S/ref=sr_1_9?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-9&srs=18345430011",
        "https://www.amazon.com/NETGEAR-Wi-Fi-Range-Extender-EX3700/dp/B00R92CL5E/ref=sr_1_10?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-10&srs=18345430011",
        "https://www.amazon.com/Bounty-Quick-Size-Paper-Towels-Family/dp/B079VP6DH6/ref=sr_1_11?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-11&srs=18345430011",
        "https://www.amazon.com/Microsoft-Office-1-year-subscription-users/dp/B009SPTUW2/ref=sr_1_12?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-12&srs=18345430011",
        "https://www.amazon.com/Seiko-SNK809-Automatic-Stainless-Canvas/dp/B002SSUQFG/ref=sr_1_13?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-13&srs=18345430011",
        "https://www.amazon.com/Samsung-MicroSDXC-Adapter-MB-ME128GA-AM/dp/B06XWZWYVP/ref=sr_1_14?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-14&srs=18345430011",
        "https://www.amazon.com/PlayStation-4-Slim-1TB-Console/dp/B071CV8CG2/ref=sr_1_15?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-15&srs=18345430011",
        "https://www.amazon.com/Sonos-Play-Compact-Wireless-Speaker/dp/B00EWCUK1Q/ref=sr_1_16?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1571064290&sr=8-16&srs=18345430011"
    ]
}
~~~
**/api/v1/WebCrawler**
~~~Javascript
var request = require("request");

var options = { method: 'POST',
  url: 'http://192.168.40.167:5004/api/v1/WebCrawler',
  headers: 
   { 'postman-token': 'b04d13a2-7009-7418-ae4b-2580c7758863',
     'cache-control': 'no-cache' },
  body: '{\n\t"Url" : "https://articulo.mercadolibre.cl/MLC-463906296-skis-atomic-expert-hv-series-6-con-fijaciones-_JM"\n}' };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
~~~

**Response**
~~~json
{
    "Status_code": 200,
    "Message": "Dump DONE"
}
~~~


