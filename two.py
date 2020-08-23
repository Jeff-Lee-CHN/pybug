#====================================#
#爬虫第一程序
#抓取ptt电影原始版标题信息
#===================================#
import urllib.request as req
import bs4

url="https://www.ptt.cc/bbs/movie/index.html"
#建立一个request物件附加headers信息
request=req.Request(url,headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#    print(data)
#解析资料
root=bs4.BeautifulSoup(data,"html.parser")
print(root.title.string)#找出标题
titles=root.find("div",class_="title")
print (titles.a.string)

titles=root.find_all("div",class_="title")
for title in titles:
    if title.a!=None:
        print (title.a.string)
