# ====================================#
# 爬虫第二程序
# 抓取ptt八卦版标题信息（18岁以上观看）
# ===================================#
import urllib.request as req
import bs4  # 导入 beautifulsoup 用于解析文本
def getdata(url):
    # 建立一个request物件附加headers信息
    request = req.Request(url, headers={
        "cookie": "over18=1",  # 判断18岁以上的特征\判断机制
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #    print(data)
    # 解析资料
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root.title.string)  # 找出标题(标题为root的属性)
    titles = root.find("div", class_="title") #找到第一个 class_="title" 的div标签
    print(titles)
    print(titles.a)
    print(titles.a.string)

    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink=root.find("a",string="‹ 上頁")#内容包含“上页”
    print(nextLink)
    print(nextLink["href"])
    return nextLink["href"]
pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"
Npage=3#抓取页数
for i in range(Npage):
    pageurl="https://www.ptt.cc"+getdata(pageurl)
print("over")
