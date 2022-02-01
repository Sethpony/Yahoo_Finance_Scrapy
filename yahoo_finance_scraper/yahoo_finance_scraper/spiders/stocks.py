import scrapy

class searchStocks(scrapy.Spider):
    name = "stocks"

    url_base = "https://finance.yahoo.com/quote/"

    def start_requests(self):
        urls = ['https://finance.yahoo.com/quote/TSLA', 'https://finance.yahoo.com/quote/NFLX']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print (page)
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


