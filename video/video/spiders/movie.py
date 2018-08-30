# -*- coding: utf-8 -*-
import scrapy
from video.items import VideoItem
import pymysql

class MjyySpider(scrapy.Spider):
	name = 'movie'
	allowed_domains = ['www.ziyuanpian.com']
	start_urls = ['http://www.ziyuanpian.com/?m=vod-type-id-1.html']
	url='http://www.ziyuanpian.com/?m=vod-type-id-1-pg-{}.html'
	page=1
	def parse(self, response):
		detail_url_list=response.xpath('//div[@class="xing_vb"]//li//a[contains(@href,"?m=vod-detail")]/@href').extract()
		for detail_url in detail_url_list:
			item=VideoItem()
			detail_url='http://www.ziyuanpian.com'+detail_url
			item['detail_url']=detail_url
			yield scrapy.Request(url=detail_url,callback=self.detail_parse,meta={'item':item})


		if self.page<1:
			self.page+=1
			url=self.url.format(self.page)
			yield scrapy.Request(url=url,callback=self.parse)

	def detail_parse(self,response):
		item=response.meta['item']
		item['movie_img']=response.xpath('//div[@class="vodImg"]/img/@src')[0].extract()
		item['movie_name']=response.xpath('//div[@class="vodInfo"]//h2/text()')[0].extract()
		try:
			item['director']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[2]/span/text()')[0].extract()
		except Exception as e:
			item['director']='未知'
		item['staring']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[3]/span/text()')[0].extract()
		item['movie_type']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[4]/span/text()')[0].extract()
		try:
			item['area']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[5]/span/text()')[0].extract()
		except Exception as e:
			item['area']='未知'
		item['languages']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[6]/span/text()').extract()
		item['release_time']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[7]/span/text()')[0].extract()
		item['update_time']=response.xpath('//div[@class="vodInfo"]//div[@class="vodinfobox"]//li[9]/span/text()')[0].extract().split()[0]
		try:
			item['summary']=response.xpath('//div[4]/div[3]/div[2]/text()')[0].extract()
		except Exception as e:
			item['summary']='暂无。'
		item['play_url']=response.xpath('//div[4]/div[4]/div[2]/div/ul//@value').extract()
		# 去除后缀为m3u8的链接地址
		if 'm3u8' in item['play_url'][0]:
			item['play_url']=item['play_url'][1]
		else:
			item['play_url']=item['play_url'][0]
		yield item