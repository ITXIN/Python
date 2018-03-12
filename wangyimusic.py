#coding=utf-8

from urllib import request
import json
import string
import urllib
# with request.urlopen('http://music.163.com/api/playlist/detail?id=3779629') as f:
#     data = f.read()
    # print('Status:', f.status, f.reason,f.info())
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))

    # print('Data:', data.decode('utf-8'))

with request.urlopen('http://music.163.com/api/playlist/detail?id=3779629') as f:
    data = f.read()
    result = json.loads(data.decode('utf-8'))
    arr = result['result']['tracks']

    print('arr:',arr)
    for i in range(10):
        name = arr[i]['album']['name']
        pic = arr[i]['album']['picUrl']
        print('name',pic)
        path =  str(name)+'.jpg'
        # urllib.request.urlretrieve(str(name),'/Users/avazuholding/Desktop/Python/网易云音乐/'+path)
        urllib.request.urlretrieve(str(pic),'网易云音乐/'+path)




        
