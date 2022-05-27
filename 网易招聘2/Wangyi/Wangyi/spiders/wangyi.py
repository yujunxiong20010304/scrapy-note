import scrapy
from Wangyi.items import WangyiItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response, **kwargs):
        item = WangyiItem()
        node_list = response.xpath('//table[@class="position-tb"]/tbody/*')[::2]
        for node in node_list:
            item['Job_title'] = node.xpath('./td[1]/a/text()').extract_first()
            item['Department'] = node.xpath('./td[2]/text()').extract_first()
            item['Position_category'] = node.xpath('./td[3]/text()').extract_first()
            item['Type_work'] = node.xpath('./td[4]/text()').extract_first()
            item['Duty_station'] = node.xpath('./td[5]/text()').extract_first()
            item['Number_recruits'] = node.xpath('./td[6]/text()').extract_first().strip()
            # strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
            item['Release_time'] = node.xpath('./td[7]/text()').extract_first()
            item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').extract_first())
            # response.urljoin用于将相对地址与绝对地址拼接起来,可以理解自动补全地址
            yield scrapy.Request(item['link'], callback=self.parse_detail, meta={'item': item})
            # 模拟翻页
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[9]/@href').extract_first()
        if part_url != 'javascript:void(0)':
            url = response.urljoin(part_url)
            yield scrapy.Request(url, callback=self.parse)  # 不写callback那么默认也是parse去解析

    @staticmethod
    def parse_detail(response):
        item = response.meta['item']
        item['Job_requirements'] = response.xpath('/html/body/div[3]/div/div[1]/a[2]')
        item['Job_description'] = response.xpath('/html/body/div[3]/div/div[1]/a[2]')
        yield item
