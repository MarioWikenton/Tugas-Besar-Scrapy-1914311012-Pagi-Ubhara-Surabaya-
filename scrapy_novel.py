# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:53:42 2021

@author: mario wikenton
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/atw-id/',
	    'https://www.worldnovel.online/novel/unrivaled-medicine-god/',
	    'https://www.worldnovel.online/novel/let-me-game-in-peace/',
	    'https://www.worldnovel.online/novel/the-mightiest-little-peasant/',
	    'https://www.worldnovel.online/novel/warriors-promise/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')