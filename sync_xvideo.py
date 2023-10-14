"""
执行对应的数据同步操作
"""

from xvideo.spiders import mongoclient
from xvideo.settings import MONGODB

class checksite:

    def __init__(self):
        table = MONGODB['MONGO_TABLE']
        self.gomongo = mongoclient()[MONGODB["MONGO_TABLE"]]

        self.gomongodetail = mongoclient()[MONGODB["MONGO_TABLEDetail"]]
    def getsite(self,nums):
        site = self.gomongo.find({"site":int(nums)})
        return site
    # 同步site = 2的数据信息
    def syncsite2(self):
        """
        获取site2 下的分类
        """
        site2 = self.getsite(2)        
        for site2info in site2:
            type_pid = int(site2info['type_pid'])
            type_name= site2info['type_name']
            type_id_2 = int(site2info['type_id'])
            site_id_2 = int(site2info['site'])
            if type_pid > 0 :
                # 执行匹配验证
                print(type_name)
                """
                获取site1 下的分类
                """
                site1 = self.getsite(1)
                for site1info in site1:
                    name = site1info['type_name']
                    type_id = site1info['type_id']
                    site_id = int(site1info['site'])
                    if type_name == name:
                        print(f" site{site_id_2}: {type_id_2} name : {type_name}   site{site_id}:{type_id} name : {name}")                        
                        self.gomongo.update_one({ "site":2, "type_id":int(type_id_2)},{"$set":{"site_id":int(type_id)}})
                        self.gomongodetail.update_many({"site":2, "type_id":int(type_id_2)},{"$set":{"site_id":int(type_id)}})
if __name__ == "__main__":
    sitemodel = checksite()
    sitemodel.syncsite2()