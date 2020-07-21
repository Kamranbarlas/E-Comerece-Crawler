import scrapy


class BestSellingAmazonDevicesSpider(scrapy.Spider):
    name = 'Best_Selling_Amazon_devices'
    allowed_domains = ['www.amazon.com']
    start_urls = ['http://www.amazon.com/Best-Sellers/zgbs/amazon-devices/']

    def parse(self, response):
        for products in response.xpath("//ol[@id='zg-ordered-list']/li[@class='zg-item-immersion']"):
            yield{
                "Title":products.xpath(".//span[@class='a-list-item']/div/span/a/div/text()").get().strip('\n           ')

                    
                }
