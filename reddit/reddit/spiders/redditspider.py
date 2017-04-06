import scrapy
from scrapy.spider import Spider


class RedditSpider(Spider):
    name = 'redditspider'
    start_urls = ['https://www.reddit.com/r/MachineLearning/',]

    def parse(self, response):

        for i in response.xpath('//*[@id="siteTable"]/div'):  # 从取出的标签找内容
            if i.xpath('div[2]/p[1]/span[1]/text()') and i.xpath('div[2]/p[1]/span[1]/text()').extract_first() == 'Discussion':
                yield {
                    'num': i.xpath('div[1]/div[3]/text()').extract(),  # 评论数，最关心的放前面
                    'title': i.xpath('div[2]/p[1]/a/text()').extract(),  # 标题
                    'author': i.xpath('div[2]/p[2]/a/text()').extract(),  # 作者
                    # 属性，用来筛选分类的，你特可以改上面的if来选其他比如 Research 这一类的都是论文
                    # 'attr':i.xpath('div[2]/p[1]/span[1]/text()'),
                    'url':'https://www.reddit.com/r/MachineLearning'+'   '+i.xpath('@data-url').extract_first(),  # 链接
                }

        for i in range(25,1999,25):
            next_page = 'https://www.reddit.com/r/MachineLearning/?count=%d' %i
            yield scrapy.Request(next_page,callback=self.parse)