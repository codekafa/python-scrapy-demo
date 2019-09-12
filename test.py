
from files.header import MainHeader
from files.res import Response
from files.proxy import Proxies
from files.req import URLlib
from files.store import SQLStore
from files.scrapingmain import MainScparer
import requests
import datetime
import urllib
import sys
import random


store= SQLStore()
header = MainHeader()
response = Response(store)
proxy = Proxies(header)
ulib = URLlib(header,proxy,response)




result = proxy.getProxies()


#print(result)

referers = []
f = open("refererlinks.txt", "r")
for x in f:
  referers.append(x)


for pr in result:
    try:
        print("QUERY PROXY ---->" + pr)
        
        pro = {
                "http":pr,
                "hhtps":pr
                }
        
        referer = random.choice(referers)
        
        headers = header.getRandomChoiceHeader()
        headers["Accept"] = 'application/json, text/javascript, */*; q=0.01'
        headers["Referer"] ='https://' + referer.strip() + '/'
        #headers["Referer"] = 'https://www.sahibinden.com/bmw'
        headers["Sec-Fetch-Mode"] ='navigate'
        headers["Sec-Fetch-User"] ='?1'
        headers["Upgrade-Insecure-Requests"] ='1'
        headers["Sec-Fetch-Site"] ='same-origin'
        headers["Accept-Encoding"] ='gzip, deflate, br'
        headers["Accept-Language"] ='tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'
        headers["Cache-Control"] ='no-cache'
        headers["Connection"] ='keep-alive'
        headers["Host"] ='www.sahibinden.com'
        headers["Pragma"] ='no-cache'
        #headers["Accept-Charset"] ='ISO-8859-1,utf-8;q=0.7,*;q=0.7'
        #headers["Keep-Alive"] = '300'
        #headers["Connection"] = 'keep-alive'
        #headers["Pragma"] = 'no-cache'
        #headers["Cache-Control"] = 'no-cache'
        #headers["Referer"] = referer
        #headers["Cookie"] = 'vid=812; cdid=RKKXhSakjGYp79DV5ccfe7ef; nwsh=std; showPremiumBanner=false; MS1=https://www.google.com/; __gfp_64b=yJaFj8VURe56YIkZCxEEupuX2hTYxWqtuLXAycW0r27.27; __gads=ID=49ac671ea6f41416:T=1557129201:S=ALNI_MbyZtnU1DfwswphTcO_lQM1A4R3lg; _fbp=fb.1.1557129202517.618818475; _ga=GA1.2.1162165870.1557129201; userLastSearchSplashClosed=true; showCookiePolicy=true; priceHistorySplashClosed=true; _fbc=fb.1.1566368935111.IwAR0TvSRjGC7ioPQErHyucc-g8WpufaXiKGuEUnYUGdMpe_BMPsOU6iZw3mo; usercity=34; _hjid=7b4c4cea-6e46-4f96-8a4a-9f333cf5a3b9; _gid=GA1.2.594725473.1568013052; bannerClosed=false; exser_ind_user_enabled=true; xsrf-token=6687ced0e350c4d23d795244ca907b38a7b04252; myPriceHistorySplashClosed=1; jsid=C68E777A06E25D418624BE90102F7C60; exser=true; exser_land_page_version=1; exser_user_type=STANDARD; st=a18cdf96c18f94388a1fb5b9000eef721f295ca19206cdc5c83a0a0bb5dabb053aa60464d4c4077f27ba895b5023e576e659b0ba232499594; geoipCity=istanbul; geoipIsp=turk_telekom; segIds=348748|348734|348730|331123|261576|155733|348729|348737|348772|348746|348731|348732|348754|348753|348751|361396|348745|344557|348744|348740|348739|348747|156474|348738|348752|348741|348726;'
        #headers["Server"] ='AWS'
        resultpage = requests.get("https://www.sahibinden.com/bmw-7-serisi-725d-long",proxies=pro,headers=headers,timeout=8)
        
        result = response.isSuccessRequest(resultpage)
        
        print(str(result))
        
        if result == True:
            print("SUCCESS PROXY -- --  >" + pr)
        else:
            print("ERROR PROXY -- --  >" + pr)
        #request = requests.get("https://www.sahibinden.com/bmw-7-serisi-725d-long", headers=headers,proxies=pr)
        
    except:
        print("EXCEPT Proxy : " + str(pr) + " --- >  " + str(sys.exc_info()[0])) 

#print(result)









