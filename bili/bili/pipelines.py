# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline


class BiliPipeline(object):
    def process_item(self, item, spider):

        return item

class BaiduPipeline(ImagesPipeline):
    #使用settings.py中的设置
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    # 此函数的第一个对象request就是当前下载对应的scrapy.Request对象，这个方法永汉返回保存的文件名，将图片链接的最后一部分党文文件名，确保不会重复
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    # 第一个item对象是爬取生成的Item对象，可以将他的url字段取出来，直接生成scrapy.Request对象,此Request加入到调度队列，等待被调度，然后执行下载
    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        print image_url
        yield scrapy.Request(image_url)

    # 这是单个Item完成下载时的处理方法，各种原因，并不是每张图片都会下载成功，此方法可以剔除下载失败的图片
    # result是该Item对应的下载结果，是一个列表形式，列表每个元素是一个元组，其中包含了下载成功与失败的信息，这里遍历下载结果，找出所有下载成功的列表，如果列表为空，那么此Item对应的图片链接下载失败，随即跑出异常DropItem，该Item忽略，否则返回Item，该Item有效
    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        if not image_path:
            raise DropItem('Image Dowload Failed')
        return item