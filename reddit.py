"""需要的库 resquest lxml 都可以pip安装"""
import requests
from lxml import etree
import time

# 主爬虫函数，传入url，输出Discussion的相关数据
def redditspider(url):
    # 这个网站需要user-agent就可以了
    headers = {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }
    web = requests.get(url,headers=headers).text
    web_data = etree.HTML(web)

    # 先取出大的标签也是三每一栏
    divs = web_data.xpath('//*[@id="siteTable"]/div')
    for i in divs:  # 从取出的标签找内容
        if  i.xpath('div[2]/p[1]/span[1]/text()') and i.xpath('div[2]/p[1]/span[1]/text()')[0] == 'Discussion':
            data={
                'num': i.xpath('div[1]/div[3]/text()'),  # 评论数，最关心的放前面
                'title':i.xpath('div[2]/p[1]/a/text()'),# 标题
                'author':i.xpath('div[2]/p[2]/a/text()'),# 作者
                # 属性，用来筛选分类的，你特可以改上面的if来选其他比如 Research 这一类的都是论文
                # 'attr':i.xpath('div[2]/p[1]/span[1]/text()'),
                'url':'https://www.reddit.com/r/MachineLearning/'+i.xpath('@data-url')[0],# 链接
            }
            # print(data)
            # 字典排序
            x = sorted(data.items(),key=lambda asd:asd[0],reverse=True)
            print(x)

# 先打印当前日期，万一你想手动复制粘贴也可以带上信息
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

# 起始链接，把你想要的前页的的链接找来装进去就OK,这里取前三页
# 这个网站每页25条 可以自己用字符串格式化来构造链接
# 如果构造过多链接记得接受错误
start_urls = ['https://www.reddit.com/r/MachineLearning/',
              'https://www.reddit.com/r/MachineLearning/?count=25',
              'https://www.reddit.com/r/MachineLearning/?count=50',]
# 取链接爬去
for url in start_urls:
    redditspider(url)
    print('换页')
# ?
