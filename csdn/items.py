import scrapy

class CsdnItem(scrapy.Item):
    name = scrapy.Field()
    content = scrapy.Field()