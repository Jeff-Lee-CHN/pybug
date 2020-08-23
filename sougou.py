#-*- encoding='utf-8' -*-
#@Time : 2020/8/19 20:18
#@Author : you
#@File : sougou.py
#@software : PyCharm

import requests
if __name__== "__main__":
    #step1:指定url
    url = "https://www.sogou.com/"
    #step2:发起请求
    response = requests.get(url=url)
    # step3:获取响应数据(text返回字符串形式的响应数据）
    page_text = response.text
    print(page_text)
    #持久化存储
    with open('./sougou.html',"w",encoding='utf-8') as fp: #./当前路径，不需要
        fp.write(page_text)
    print('爬取数据结束')
print("over")#输出over，以示庆祝