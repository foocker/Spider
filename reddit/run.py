
from scrapy import cmdline

# 命令行启动
cmdline.execute("scrapy crawl redditspider -o data.csv".split())