import scrapy
import json

class qouteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        with open("data_file.json", "w") as filee:
            filee.write('[')
            for index, quote in enumerate(response.css('div.quote')):
                json.dump({
                    'text': quote.css('span.text::text').extract_first(),
                    'author': quote.css('.author::text').get(),
                    'tags': quote.css('.tag::text').getall()
                }, filee) 
                if index < len(response.css('div.quote')) - 1:
                    filee.write(',')
            filee.write(']')