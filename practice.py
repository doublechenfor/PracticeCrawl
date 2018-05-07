import urllib.request
import os
import re

def gethtml(href):
    req=urllib.request.urlopen(href)  #传入url，获取该URL的数据资源
    readhtml=req.read()
    return readhtml                   #返回读取到的网页信息
def getpic(html):
    reg=r'src="(.+?\.jpg)"'           #需要获取的img的正则表达式
    cpmreg=re.compile(reg)            #将正则表达式reg转为正则表达式对象comreg，实现更有效率的匹配
    imglist=cpmreg.findall(html.decode('utf-8'))  #python3里要将获取到的页面信息用decode对页面信息按UTF-8进行解码
    if not os.path.isdir("D:\\test"):
      os.makedirs("D:\\test")         #创建目录
    x=0
    for url in imglist:
        urllib.request.urlretrieve(url,'{}{}.jpg'.format(("D:\\test\\"),x))   #将imglist里的图片下载到本地，通过format给每个图片命名
        x=x+1
    return imglist
html5=gethtml("http://tieba.baidu.com/f?kw=ps&fr=ala0&tpl=5")       
print (getpic(html5))
# https://tieba.baidu.com/p/2460150866?red_tag=2785439023
