import requests
import bs4
import json
import os
import urllib3

with open("run_results.json",'r') as f:
     fs = json.load(f)

all_link = []
for i in fs["selection1"]:
    all_link.append(i["url"]+"?dl=1")

names = [i for i in range(65)]

names_urls = zip(names, all_link)

def download(url,i):
    r = requests.request(url=url,method='GET')
    with open(str(i)+".pdf",'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       f.write(chunk)
        f.close()
count = 0
for i in all_link:
    download(i,count)
    count+=1

