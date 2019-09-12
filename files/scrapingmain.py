import threading
from files.basescrape import Scraper, xpathSafeRead
from files.store import SQLStore




class MainScparer(Scraper,object):
    def __init__(self,n_jobs,uutils,header,proxies,response,lowerdelay=1,upperdelay=3,current_date="",main_url=""):
        super(MainScparer,self).__init__(url=main_url,njobs=n_jobs,lowerdelay=lowerdelay,upperdelay=upperdelay)
        self.brandList=[]
        self.modelList = []
        self.versionList =[]
        self.n_jobs = n_jobs
        self.uutils = uutils
        self.lock = threading.Lock()
        self.header=header
        self.url=main_url
        self.proxies = proxies
        self.response=response
        
    def getBrands(self):
        brandpage = self.uutils._readURL(self.url)
        self.response.crawlBrands(brandpage)
        
    def getModels(self):
        store = SQLStore()
        brandList= store.getBrands()
        for i in brandList:
            print(self.url + i[2])
            brand_page = self.uutils.delayedreadURL(self.url + i[2],self.lowerdelay,self.upperdelay)
            self.response.crawlModels(brand_page,i[0])
            
    def getVersions(self):
        store = SQLStore()
        modelList= store.getModels()
        for i in modelList:
            model_page = self.uutils.delayedreadURL(self.url + i[3],self.lowerdelay,self.upperdelay)
            self.response.crawlVersions(model_page,i[0])
            
    def getSubVersions(self):
        store = SQLStore()
        versionList = store.getVersions()
        links = []
        for l in versionList:
            links.append(l[3])

        
        self._crawlsubversionpage(links)
        #self._batchrunwithid(self._crawlsubversionpage,links)
        
    
    def _crawlsubversionpage(self, links):
        #print(links)
        
        for i in range(len(links)):
            try:
                #print(links[i])
                version_page = self.uutils._readURL(self.url + links[i],True)
                self.response.crawlSubVersions(version_page,1)
            except:
                continue
    
    
    def _batchrunwithid(self, func, links):
        for begin in range(0, len(links), self._njobs):
            end = begin + self._njobs
            splitted = links[begin:end]
            self._threader(func, splitted)
            progress = end
            if progress > len(links):
                progress = len(links)