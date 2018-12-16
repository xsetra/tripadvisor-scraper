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
        for review in response.css('div.review_collection div.reviewSelector'):
            yield {
                'title': review.css('span.noQuotes::text').extract_first(),
                'entry': review.css('div.entry p.partial_entry::text').extract_first(),
                'rate': review.css('div.reviewItemInline span.ui_bubble_rating').extract_first(),
            }

        next_page = response.css('a.nav.next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
