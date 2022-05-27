# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MyspiderPipeline:
    def __init__(self):
        self.fiel = open("itcast.json","w")

    def process_item(self, item, spider):  # item是爬虫文件中解析函数(parse)返回的数据,spider就是哪一个爬虫运行就是那一个爬虫
        # 不能在这里创建文价，如果在这里创建文件那么每调用一次就会创建一次文件
        print('itcast:',item)  # 查看一下信息
        # 将item对象强转字典,该操作只能在scrapy中使用
        item = dict(item)

        json_data = json.dumps(item,ensure_ascii=False)+',\n'    #将字典数据序列化,ensure_ascii设置保存结果为中文
        self.fiel.write(json_data)   #将数据写入文件

        return item   # 默认使用完管道需要将数据返回给引擎
    def __del__(self):
        self.fiel.close()
