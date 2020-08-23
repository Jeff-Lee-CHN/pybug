#AJAX(XHR)是javasc的技术、会影响爬虫的技术
#先发回一个空网页、浏览器发送第二次清酒，之后返回带有资料的网页
#==================================#
#抓取Medium.com的首页文章列表
#==================================#
import urllib.request as req
import json
url="https://medium.com/_/api/home-feed"
#建立一个request物件附加headers信息
request=req.Request(url,headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")#打开网址获取资料（json格式）
#解析资料
data=data.replace("])}while(1);</x>","")#删除开头的无用文件
data=json.loads(data)#把原始资料变成列表、字典形式
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])
print("over")