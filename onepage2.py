import scrapy


class MercadoLibreSpider(scrapy.Spider):
    name = 'mercado_libre'
    start_urls = ['https://listado.mercadolibre.com.ve/portatiles-laptops/laptos_DisplayType_LF']

    def parse(self, response):
        # con xpath seleccionamos un div que contengan los items a extraer
        # y creamos un objeto article para recorrer los items con un for
        for article in response.xpath("//div[@class='item__info item--hide-right-col ']"):
            yield {'title': article.xpath("./h2/a/span/text()").extract_first(),
                   'price': article.xpath(".//div[@class='price__container']/div[@class='item__price ']/span[@class='price__fraction']/text()").extract_first(),
                  }


# se ejecuta con el siguiente comando con el formato deseado
# scrapy runspider onepage.py -o resources/product.json -t json
# scrapy runspider onepage.py -o resources/product.csv -t csv