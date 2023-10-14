# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from xvideo.settings import MONGODB
from xvideo.spiders import mongoclient

class XvideoPipeline:
    def __init__(self):
        # 检测名称是否存在        
        self.gomongo = mongoclient()[MONGODB["MONGO_TABLE"]]
        self.gomongodetail = mongoclient()[MONGODB['MONGO_TABLEDetail']]
    def process_item(self, item, spider):
        boolinfo = item['boolinfo']
        site = item['site']
        if boolinfo:
            # DETAIL 
            videoinfo = item['videoinfo']
            self.gomongodetail.insert_many(videoinfo)
            pass
        else:
            #
            # 表是否存在
            tables = mongoclient().list_collection_names()
            if MONGODB["MONGO_TABLE"] in tables:
                resRow = self.gomongo.find_one({'site': int(site)})
                if resRow:                    
                    return item
            newclass = []
            for info in item['classinfo']:
                info["site"] = site
                newclass.append(info)
            self.gomongo.insert_many(newclass)
            
            return item