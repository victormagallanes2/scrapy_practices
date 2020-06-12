import scrapy
#from scrapy.loader import ItemLoader


""" class Product(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field() """


class MercadoLibreSpider(scrapy.Spider):
    # Nombre del spider
    name = 'mercado_libre'
    # Url objetivo
    start_urls = ['https://listado.mercadolibre.com.ve/portatiles-laptops/laptos_DisplayType_LF']
    # funcion extractora
    def parse(self, response):
        # creamos objeto para recorrer los items
        for article in response.xpath("//div[@class='item__info item--hide-right-col ']"):
            yield {'title': article.xpath("./h2/a/span/text()").extract_first(),
                   'price': article.xpath(".//div[@class='price__container']/div[@class='item__price ']/span[@class='price__fraction']/text()").extract_first(),
                  }