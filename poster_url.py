#!/usr/bin/env python
# coding: utf-8

# In[70]:


try:
    import requests, lxml, re, json, urllib.request
    from bs4 import BeautifulSoup
except:
    print("Modules Missing")
    
class get_data(object):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }

    params = {
        "q": "",
        "tbm": "isch", 
        "hl": "en",
        "ijn": "0",
    }
    def __init__(self,query):
        self.params = get_data.params
        self.query = query
        self.params["q"] = self.query
        self.html = requests.get("https://www.google.com/search", params=self.params, headers=get_data.headers)
        self.soup = BeautifulSoup(self.html.text, 'lxml')
class img_data:
    def __init__(self,query):
        self.query = query
        self.soup = get_data(self.query)
        self.all_script_tags = self.soup.soup.select('script')
        self.matched_images_data = ''.join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(self.all_script_tags)))
        self.matched_images_data_fix = json.dumps(self.matched_images_data)
        self.matched_images_data_json = json.loads(self.matched_images_data_fix)
class img_links:
    def __init__(self,no_of_links,query):
        self.query =query
        self.img_data = img_data(self.query)
        self.n = no_of_links
        self.matched_google_image_data = re.findall(r'\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",',self.img_data.matched_images_data_json)
        self.matched_google_images_thumbnails = ', '.join(re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                                                                     str(self.matched_google_image_data))).split(', ')
    def get_url(self):
        google_image_links = []
        links = []
        remove_thumbnails = re.sub(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', '',str(self.matched_google_image_data))
        original_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",remove_thumbnails)
        
        for ori_img in original_images:
            ori_img_not_fixed = bytes(ori_img, 'ascii').decode('unicode-escape')
            ori_img_fixed = bytes(ori_img_not_fixed, 'ascii').decode('unicode-escape')
            google_image_links.append(ori_img_fixed)
        for i in range(self.n):
            links.append(google_image_links[i])
        return links