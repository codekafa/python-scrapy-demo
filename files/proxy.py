
import requests
from lxml.html import fromstring
import random

class Proxies:
    def __init__(self,header):
        super(Proxies,self).__init__()
        self.header=header
        
    def getProxies(self):
        
        url = 'https://free-proxy-list.net/'
        headers = self.header.getRandomChoiceHeader()
        response = requests.get(url,headers=headers)
        parser = fromstring(response.text)
        proxies = []
        for i in parser.xpath('//tbody/tr')[:20]:
            #if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.append(proxy)
        return proxies
        '''
        url = 'https://www.proxynova.com/proxy-server-list/country-tr/'
        headers = self.header.getRandomChoiceHeader()
        response = requests.get(url,headers=headers)
        #print(response.text)
        parser = fromstring(response.text)
        proxies = []
        trs = parser.xpath('//tbody/tr')
        for i in trs:
            try:
                #print(i.xpath('//td')[0].xpath('//abbr/@title')[0])
                #
                ip = i.xpath('./td/abbr/@title')[0]
                port = i.xpath('./td')[1].text
                port = port.strip()
                #print("FİRST :  " + port)
                
                if port == "Turkey":
                    port = i.xpath('./td/a')[1].text
                
                #print(port)
                
                proxy = ip + ":" + port.strip()
                #print(i.xpath('td')[1].text.strip())
                #if i.xpath('.//td[7][contains(text(),"yes")]'):
                #proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                #p = {"http": proxy, "https": proxy}
                proxies.append(proxy)
            except:
                continue
        '''
        return proxies
        
    def getRandomProxy(self):
        proxies = self.getProxies()
        proxy = random.choice(proxies)
        p = {"http": proxy, "https": proxy}
        return p
        
    def getRandomProxyText(self):
        proxies = self.getProxies()
        proxy = random.choice(proxies)
        return proxy
    
    