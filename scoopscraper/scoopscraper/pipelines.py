# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScoopscraperPipeline(object):
    def process_item(self, item, spider):
        # calling DjangoItem.save() stores the item in the database
        item.save()
        return item
