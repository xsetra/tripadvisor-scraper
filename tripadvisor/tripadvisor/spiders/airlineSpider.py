import scrapy


class AirlineSpider(scrapy.Spider):
    name = "AirlineSpider"

    def start_requests(self):
        urls = [
            'https://www.tripadvisor.com.tr/Airline_Review-d8729174-Reviews-Turkish-Airlines',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titles = response.css('span.noQuotes::text').extract()
        entries = response.css('div.entry p.partial_entry::text').extract()
        rates = response.css('div.innerBubble div.wrap div.reviewItemInline span.ui_bubble_rating').extract()
        return {
            'page_1': {
                'titles': titles,
                'entries': entries,
                'rates': rates
            }
        }
