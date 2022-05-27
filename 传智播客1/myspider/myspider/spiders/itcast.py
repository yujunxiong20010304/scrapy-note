import scrapy


# 获取文本数据 text 获取二进制数据 body
class ItcastSpider(scrapy.Spider):  # 继承scrapy.spider
    # 爬虫名字
    name = 'itcast'
    # 允许爬取的范围            2.检查域名
    allowed_domains = ['itcast.cn']
    # 开始爬取的url地址         1.修改起始url
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml#ajavaee']

    # 数据提取的方法，接收下载中间件传过来的response(响应)      3.在parse方法中实现爬取逻辑
    def parse(self, response, **kwargs):
        # scrapy的response对象可以直接运行xpath, 但是xpath返回的选择器对象列表, 其他地方和原本的xpath一样
        # xpath数据的提取方法
        # get() , getall()是最新版方法    extract() , extract_first()是旧版本的方法
        # xpath的结果为只含有一个值的列表，可以使用extract_first()
        node_list = response.xpath('/html/body/div[10]/div/div[2]/ul/li')
        # 便=遍历节点列表
        for node in node_list:
            temp = {}
            temp['name'] = node.xpath('./div[@class="main_bot"]/h2/text()')[0].get()
            temp['occupation'] = node.xpath('./div[@class="main_bot"]/h2/span/text()')[0].extract()
            yield temp
