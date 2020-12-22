import scrapy


class QuotesSpider(scrapy.Spider):
    # name of the spider, used by Scrapy
    name = "quotes2"

    # starting point for the spider, automatically called by Scrapy
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # page parser for Scrapy, determines what gets done with the page
    def parse(self, response):
        
        # goes through all of the quotes on the page and finds the text, author, tags associated with the quotes
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            
        # how the spider moves onto the next page
        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)