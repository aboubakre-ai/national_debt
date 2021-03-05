import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        
        rows= response.xpath("//table[@class='jsx-1487038798 table table-striped tp-table-body']/tbody/tr")
        for row in rows:
            name=row.xpath("./td[1]/a/text()").get()
            gdp= row.xpath("./td[2]/text()").get()
            population=row.xpath("./td[3]/text()").get()
            yield{
                'name':name,
                'gdp':gdp,
                'population':population
            }