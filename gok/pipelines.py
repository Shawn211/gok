# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class GokPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        heroes=item['hero']
        for hero in heroes:
            
