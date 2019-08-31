# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/all?keyword=Scrapy&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.1']

    def parse(self, response):
        item={}
        item["url"]=response.xpath("//ul[@class = 'video-contain clearfix']/li[@class = 'video matrix']/a/@href").extract()
        #print tr_list
        for i in range(2,20):
            nextUrl=self.start_urls[0]+"&page="+str(i)
            yield scrapy.Request(nextUrl,callback=self.parse1,meta={"thisUrl":nextUrl})

    def parse1(self, response):
        item = {}
        item["thisUrl"] = response.meta["thisUrl"]
        item["url"]=response.xpath("//ul[@class = 'video-contain clearfix']/li[@class = 'video matrix']/a/@href").extract()
        yield item