import json
from xvideo.items import XvideoItem
from scrapy import Spider,Request

class Xvideo1Spider(Spider):
    name = "xvideo1"
    allowed_domains = ["hhzyapi.com"]
    start_urls = ["https://hhzyapi.com/api.php/provide/vod/"]
    site = 1
    def parse(self, response):        
        datainfo = (response.body).decode('utf-8')        
        jsoninfo = json.loads(datainfo)
        classinfo = jsoninfo['class']        
        yield XvideoItem(boolinfo=False,classinfo=classinfo,site=self.site)
        for info in classinfo:
            type_id = info['type_id']
            type_pid = info['type_pid']
            # if type_pid > 0:
                
            #     yield Request(f"https://hhzyapi.com/api.php/provide/vod/?ac=detail&t={type_id}",callback=self.getDetail,cb_kwargs=dict(type_id=type_id))
                
    def getDetail(self,response,type_id):
        datainfo = (response.body).decode('utf-8')        
        jsoninfo = json.loads(datainfo)
        code = jsoninfo['code']
        page = int(jsoninfo['page'])
        pagecount = int(jsoninfo['pagecount'])
        total = jsoninfo['total']
        videoinfo = jsoninfo['list']
        print(f"获取数量:{total} 当前页码：{page }  获取页数{pagecount} info {type_id}")
        if videoinfo:
            yield XvideoItem(boolinfo=True,videoinfo=videoinfo,site=self.site)

        if page <= pagecount:
            page = page+1
            yield Request(f"https://hhzyapi.com/api.php/provide/vod/?ac=detail&t={type_id}&pg={page}",callback=self.getDetail,cb_kwargs=dict(type_id=type_id))
        
        print("END")