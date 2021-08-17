#from bs4 import BeautifulSoup as bs
import urllib.request
import requests
#from fake_useragent import UserAgent

class html:
    def __init__(self,url):
        self.url = url
    def lxmlSoup(self):
        return bs(open_url(self.url),'lxml')
    def parserSoup(self):
        return bs(open_url(self.url),'html-parser')
    def download(self,fileName):
        with urllib.request.urlopen(self.url) as response, open(fileName, 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)
    def login(self,username,password):
        with requests.Session() as c:
            c.get(self.url)
            csrftoken = c.cookies['csrftoken']
            login_data = dict(
                csrfmiddlewaretoken=csrftoken,
                username=username,
                password=password
            )
            c.post(self.url,data=login_data)
        

    
def open_url(url):
    website = urllib.request.Request(url, data=None, headers={'User-Agent': UserAgent().random})
    return urllib.request.urlopen(website)

