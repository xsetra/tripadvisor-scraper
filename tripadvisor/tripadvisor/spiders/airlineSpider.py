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
        filename = 'turkish-airlines.html'
        with open(filename, 'wb') as fp:
            fp.write(response.body)
        self.log('Saved file {}'.format(filename))
