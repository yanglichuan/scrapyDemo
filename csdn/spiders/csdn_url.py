# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from csdn.items import CsdnItem

class CsdnUrlSpider(CrawlSpider):
    name = 'csdn_url'
    allowed_domains = ['runoob.com']
    start_urls = ['https://www.runoob.com/python3/python3-tutorial.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.runoob.com/python3/python3-+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        name = response.xpath('//div[@class="article-intro"]/h1/text()').get()
        if response.xpath('//div[@class="article-intro"]/h1/span/text()').get():
            name += response.xpath('//div[@class="article-intro"]/h1/span/text()').get()
        contents = response.xpath('//div[@class="article-intro"]//text()').getall()
        title = []
        title.append(name)
        if response.xpath('//div[@class="article-intro"]/h2/text()').get():
            title_2 = response.xpath('//div[@class="article-intro"]/h2/text()').getall()
            title += title_2
        if response.xpath('//div[@class="article-intro"]/h3/text()').get():
            title_3 = response.xpath('//div[@class="article-intro"]/h3/text()').getall()
            title += title_3
        print("===============")
        print(name)
        print(title)
        content_list = []
        for i in contents:
            # if content=="\r\n":
            #     continue
            if "\t" in i:
                continue
            if "\n" in i:
                continue
            if i in title:
                content_list.append("\n")
            content_list.append(i.strip())
            if i in title:
                content_list.append("\n")
        content = " ".join(content_list)
        print(content)
        item = CsdnItem(name=name, content=content)
        print(item)
        yield item