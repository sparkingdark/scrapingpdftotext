import os 
import json


def getlinesasjson(paths,jsonfile):
    all_pdfs = os.listdir(paths)
    content = None
    dic = {}
    for i in all_pdfs:
        with open(paths+i,'r') as f:
            content = f.readlines()
            for i in content:
                if i==" \n" or i=="  \n" or "\n":
                   content.remove(i)
            dic.update({i:content[:31]})
        f.close()
    with open(jsonfile,'w+') as p:
        json.dump(dic,fp=p)

if __name__ == "__main__":
    getlinesasjson('texts/','data.json')       