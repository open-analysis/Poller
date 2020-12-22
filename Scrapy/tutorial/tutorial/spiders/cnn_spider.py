import scrapy

from scrapy.exporters import CsvItemExporter

class QuotesSpider(scrapy.Spider):
    # name of the spider, used by Scrapy
    name = "cnn"

    # starting point for the spider, automatically called by Scrapy
    start_urls = [
        #'https://www.cnn.com/2020/06/01/world/coronavirus-newsletter-06-01-20-intl/index.html',
        #'https://www.cnn.com/2011/01/31/tv/be-in-the-know-todays-political-bullet-points-163/index.html',
        'https://www.cnn.com/sitemap.html',
    ]        
    
    def close_spider(self, spider):
        exporter.finish_exporting()
    
    # page parser for Scrapy, determines what gets done with the page
    def parse(self, response):
        
        # goes through all of the quotes on the page and finds the text, author, tags associated with the quotes
        title = response.css('title::text').get()
        url = response.url
        
        # packaging the parts of the site that I want to save
        item = {'title' : title}
        item2 = {'url' : url}
    
        f = open('cnn.csv', 'ab')
        exporter = CsvItemExporter(f, include_headers_line=False)
    
        exporter.start_exporting()
        exporter.export_item(item)
        exporter.export_item(item2)
            
        # how the spider moves onto the next page
        #yield from response.follow_all(css="ul.pager a", callback=self.parse)
        
        # within the sitemap, getting the different year sitemaps
        try :
            '''
            Try:
                for highest level sitemap:
                    li.date a
                    ul.sitemap-year a
                for within a section:
                    for month:
                        ul.sitemap-month a
                        li.month a
                    for section:
                        li.section a
                        ul.sections-names a
                        
                        for within both:
                            span.sitemap-link a
            '''
            # for href in response.css('ul.sitemap-year a::attr(href)'):
            for href in response.css('ul.sitemap-year a::attr(href)').getall():
                if href.count('article') is not 0:
                    yield response.follow(href, callback=self.parse)
            
            '''
            # this doesn't work for some reason, idk why
            anchors = response.css('ul.sitemap-year a')
            #yield from response.follow_all(anchors, callback=self.parse)
            response.follow_all(anchors, callback=self.parse)
            '''
            
        except:
            pass
        
        # within the year, checking the months portion
        try:
            for href in response.css('ul.sitemap-month a::attr(href)'):
                yield response.follow(href, callback=self.parse)
                
        except:
            pass
        
        '''
        # within the year, checking the sections portion
        try:
            for href in response.css('ul.sections-names a::attr(href)'):
                yield response.follow(href, callback=self.parse)
                
        except:
            pass
        '''
        # within the articles layer, getting the individual articles
        try:
            for href in response.css('span.sitemap-link a::attr(href)'):
                yield response.follow(href, callback=self.parse)
        except:
            pass