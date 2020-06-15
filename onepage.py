import scrapy


class BlogSpider(scrapy.Spider):
    # nombre del spider
    name = 'blogspider'
    # url objetivo
    start_urls = ['https://blog.scrapinghub.com']
    # funcion extractora
    def parse(self, response):
        # con css selector seleccionamos un div que contengan los items a extraer
        # y creamos un objeto title para recorrer los items con un for
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}


# se ejecuta con el siguiente comando con el formato deseado
# scrapy runspider onepage.py -o resources/blogs.json -t json
# scrapy runspider onepage.py -o resources/blogs.csv -t csv