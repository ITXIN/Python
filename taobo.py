#coding=utf-8
from urllib import request
import json
import string
import urllib
# http://www.cnblogs.com/dearvee/p/6565688.html
#Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
def getCommodityComments(url):
    print(url[url.find('id=')+14])
    if url[url.find('id=')+14] != '&':
        id = url[url.find('id=')+3:url.find('id=')+15]
    else:
        id = url[url.find('id=')+3:url.find('id=')+14]
    print('id',id)
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+id+'&currentPageNum=1'

    print('url',url)
    with request.urlopen(url) as f:
            res = f.read()
            res = res.decode('gbk')
            jc = json.loads(res.strip().strip('()'))
            getUserComments(jc,url)


def getUserComments(jc,url):
    max = jc['total']
    users = []
    comments = []
    count = 0
    page = 1
    print('该商品共有评论'+str(max)+'条,具体如下: loading...')
    while count<max:
        with request.urlopen(url[:-1]+str(page)) as f1:
            res1 = f1.read()
            res1 = res1.decode('gbk')
            page = page + 1
            jc1 = json.loads(res1.strip().strip('()'))
            jc1 = jc1['comments']
            for j in jc1:
                users.append(j['user']['nick'])
                comments.append( j['content'])
                getUserCommentsPhoto(j)
                getAvatar(j)
                # print(count+1,'>>',users[count],'\n        ',comments[count])
                count = count + 1

def getUserCommentsPhoto(j):
    imageEntityArr = j['photos']
    i = 0
    for image  in imageEntityArr:
        link = 'https:'+image['url']
        userName = j['user']['nick']
        imageName = userName + '_' + str(i)
        i  = i + 1
        imageName= imageName.replace('/','／') .replace('\\','＼')
        filesavepath = '淘宝/'+'%s.jpg'%imageName
        urllib.request.urlretrieve(str(link),filesavepath)
        # print('phot path',filesavepath)

def getAvatar(j):
    userName = j['user']['nick']+'_avatar'
    avatar = 'https:'+j['user']['avatar']
    avatarName =  userName.replace('/','／') .replace('\\','＼')
    avatarPath = '淘宝/'+'%s.png'%avatarName
    print(avatar)
    urllib.request.urlretrieve(str(avatar),avatarPath)

getCommodityComments('https://item.taobao.com/item.htm?id=39595400262&')
