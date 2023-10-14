# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XvideoItem(scrapy.Item):
    boolinfo = scrapy.Field()
    classinfo = scrapy.Field()
    videoinfo = scrapy.Field()
    site = scrapy.Field()
