#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    import requests
    from bs4 import BeautifulSoup
except:
    print("some modules are missing")

class google_image_url:
    user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',}
    Google_Image =     'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
    def __init__(self,query, n):
        """""
            query = image name
            n = no of img url
        """""
        self.search_url = self.Google_Image+"q="+query
        response = requests.get(self.search_url,headers = self.user_agent)
        html = response.text
        soup = BeautifulSoup(html,"html.parser")
        self.output = soup.findAll("img",{"class":"rg_i Q4LuWd"})
    def get_imageurl(self):
        links = []
        c = 0
        for res in self.output:
            try:
                l = res['data-src']
                if c < 1:
                    c+=1
                    links.append(l)
            except:
                continue
        
        return links[0]

