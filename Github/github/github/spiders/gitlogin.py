import scrapy


class GitloginSpider(scrapy.Spider):
    name = 'gitlogin'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/yujunxiong20010304']

    def start_requests(self):      # 重写start_requests方法
        cookie_str = '''_octo=GH1.1.1269237224.1630754307; _device_id=119eba40b8d6757932207bf778687f19;
         user_session=eIjx3aP_V6eVHTvZjA89Af9_JL9q477LBKZPilm64PIpyllz;
          logged_in=yes; dotcom_user=yujunxiong20010304;
           color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_them
           e%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%2C
           %22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D;
            tz=Asia%2FShanghai; has_recent_activity=1;
             _gh_sess=NUK7hbCd7PSIuYpPHssoZgD0RKTUs%2BKnhONpVL504uDHThrrqUedUVVzXkaxeD9luhUCXjH1
             6%2FjbZCISp2UzOndMn7u8cYKH%2Fd7yK1IKEZelHmcjyiVORBrSUkLum82QLEdYWUJZugv3kdzSZ8Hsh%2B
             sRt3T5kTwHP8daJD21%2F1G5%2BTIkfAszIeS4a%2Fkh0gpck8%2B2Ns8zd763nkrFs8SIy70%2F3d6xtlnL
             ZK8oHLF1CuooKyoYhQjMzQv2fdIfGq74mkomYFuvCRVSUubIhRz3s7jZpleRamnaSewajXKsP9P5A%2BpO0e%2
             BX4m%2FYCYcAzWf6H32by0GWVeMjNX2BipaooQkMC76IhReNn8D12KgQBz3R3%2BxcA4W%2Frx62900%3D--LW91
             wNBtSL6z%2BGVn--EIhwhLgSFk0YmRjlZoM8hA%3D%3D'''
        cookie_dict = {data.split('=')[0]: data.split('=')[1] for data in cookie_str.split(";")}
        yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies=cookie_dict)

    def parse(self, response, **kwargs):
        title = response.xpath('/html/head/title/text()').extract()
        print(title)
