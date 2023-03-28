import scrapy

from urllib.parse import urljoin

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index_table = response.css(
            'section#numerical-index')
        pep_links = numerical_index_table.css("a::attr(href)").getall()

        for link in pep_links[1:]:
            pep_link = urljoin(self.start_urls[0], link)
            yield response.follow(pep_link, self.parse_pep)

    def parse_pep(self, response):
        # Извлекаем номер, название и статус документа PEP
        number_and_name = response.css('h1.page-title:first-child::text').get()
        number = number_and_name.split(sep=' – ')[0]
        name = number_and_name.split(sep=' – ')[1]
        status = response.css('abbr::text').get()
        pep_item = PepParseItem(number=number, name=name, status=status)
        yield pep_item
