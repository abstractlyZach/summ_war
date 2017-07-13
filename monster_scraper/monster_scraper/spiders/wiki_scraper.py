# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
	name = "wiki"
	allowed_domains = ["summonerswar.wikia.com"]
	start_urls = [r'http://summonerswar.wikia.com/wiki/User_blog:M%CD%A2ystr%CD%A2ile/Monster_data']

	def parse(self, response):
		body = response.css('body')
		table = body.css('table.article-table')[1]
		names = table.css('td a::text').extract()
		stats = table.css('td::text').extract()

		index = 0
		for name in names:
			stats_first_index = index * 9
			yield {
				'Name': name,
				'Element': stats[stats_first_index + 2].strip(),
				'Grade': stats[stats_first_index + 3].strip(),
				'HP': stats[stats_first_index + 4].strip(),
				'ATK': stats[stats_first_index + 5].strip(),
				'DEF': stats[stats_first_index + 6].strip(),
				'SPD': stats[stats_first_index + 7].strip(),
				'Weight': stats[stats_first_index + 8].strip(),
			}

			index = index + 1

