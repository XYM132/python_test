# -*- coding: utf-8 -*-
import re

import scrapy


class CsbSpider(scrapy.Spider):
    name = 'csb'
    allowed_domains = ['image.baidu.com']
    url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%B5%B5%E4%B8%BD%E9%A2%96&cl=2&lm=&hd=&latest=&copyright=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E8%B5%B5%E4%B8%BD%E9%A2%96&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=" #30&rn=30
    start_urls = ['https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%B5%B5%E4%B8%BD%E9%A2%96&cl=2&lm=&hd=&latest=&copyright=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E8%B5%B5%E4%B8%BD%E9%A2%96&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='+'0&rn=30']

    def parse(self, response):
        pattern = re.compile(r'"middleURL":"(.*?)",', re.S)
        # 此datas返回的是一个正则表达式列表，可迭代取出里面的url
        datas = re.findall(pattern, response.text)
        response.meta.setdefault("num", 0)
        for val in datas:
            item = {}
            item['imageLink'] = val

            yield item


        if response.meta["num"]>1000:
            return
        next_urls=self.url+str(response.meta["num"])+"&rn=30"
        yield scrapy.Request(next_urls,callback=self.parse,meta={"num":response.meta['num']+30},dont_filter=True)