import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

    """funcion para hacer click en el articulo y continuar
       recomipando informacion"""

        #for next_page in response.css('a.next-posts-link'):
            #yield response.follow(next_page, self.parse)



# se ejecuta con el siguiente comando con el formato deseado
# scrapy runspider onepage.py -o resources/blogs.json -t json
# scrapy runspider onepage.py -o resources/blogs.csv -t csv






        #for article in response.xpath("//div[@class='item__info item--hide-right-col ']"):
            #yield {'title': article.response.xpath('/h2/a/span').get(),
                   #'price': article.xpath(/h2/a/span.text()).extract(),
                   #'location': article.xpath(/h2/a/span.text()
                  #}