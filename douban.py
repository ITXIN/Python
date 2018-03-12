#coding=utf-8
#http://www.cocoachina.com/programmer/20150227/11198.html 原文
from urllib import request
import json
import string
import urllib

from bs4 import BeautifulSoup

def getAllImageLink():
    L = list(range(11,21))
    print(L)
    for i  in L:
        url = 'https://www.dbmeinv.com/?pager_offset=%s'%str(i)
        print('url------',url)
        with request.urlopen(url) as r:
            html = r.read().decode('utf-8')
            soup = BeautifulSoup(html)
            liResult = soup.findAll('li',attrs={"class":"span3"})
            for li  in liResult:
                imageEntityArr = li.findAll('img')
                # print(imageEntityArr)
                for image  in imageEntityArr:
                    link = image.get('src')
                    imageName = str(i)+ str(image.get('title'))
                    imageName= imageName.replace('/','／') .replace('\\','＼')
                    filesavepath = '豆瓣/'+'%s.jpg'%imageName
                    print('link',link,'path',filesavepath)
                    urllib.request.urlretrieve(str(link),filesavepath)


if __name__ == '__main__':
    getAllImageLink()
