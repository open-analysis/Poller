# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

'''
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

'''    

    
''' 
import scrapy
    
class CsvItemPipeline(object):
    def __init__(self):
        self.file = open("cnn.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, unicode)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        create_valid_csv(item)
        self.exporter.export_item(item)
        return item
    
    def create_valid_csv(self, item):
        for key, value in item.items():
            is_string = (isinstance(value, basestring))
            if (is_string and ("," in value.encode('utf-8'))):
                item[key] = "\"" + value + "\""
                
'''
                
                
'''
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class DuplicatesPipeline:

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['id'])
            return item
            
            
'''