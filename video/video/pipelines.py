# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.utils.project import get_project_settings

class VideoPipeline(object):
	def process_item(self, item, spider):
		return item

class MovieMysqlPipeline(object):
	def open_spider(self,spider):
		settings=get_project_settings()
		host=settings['HOST']
		port=settings['PORT']
		user=settings['USER']
		passwd=settings['PASSWD']
		db=settings['DB']
		charset=settings['CHARSET']
		self.con=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)

	def close_spider(self,spider):
		self.con.close()

	def process_item(self, item, spider):
		sql='insert into movie (movie_img,movie_name,director,staring,movie_type,area,languages,release_time,update_time,summary,play_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
		self.cursor=self.con.cursor()
		try:
			self.cursor.execute(sql,(item['movie_img'],item['movie_name'],item['director'],item['staring'],item['movie_type'],item['area'],item['languages'],item['release_time'],item['update_time'],item['summary'],item['play_url']))
			self.con.commit()
		except Exception as e:
			self.con.rollback()
		return item

class TvMysqlPipeline(object):
	def open_spider(self,spider):
		settings=get_project_settings()
		host=settings['HOST']
		port=settings['PORT']
		user=settings['USER']
		passwd=settings['PASSWD']
		db=settings['DB']
		charset=settings['CHARSET']
		self.con=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)

	def close_spider(self,spider):
		self.con.close()

	def process_item(self, item, spider):
		play_urls=item['play_urls']
		play_urls=play_urls.strip('[]').replace('\'','').replace(' ','').split(',')
		sql_1='insert into tv (tv_img,tv_name,director,staring,tv_type,area,languages,release_time,update_time,summary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
		sql_2='insert into tv_list (tv_name,num,play_url) values (%s,%s,%s);'
		self.cursor=self.con.cursor()
		try:
			self.cursor.execute(sql_1,(item['tv_img'],item['tv_name'],item['director'],item['staring'],item['tv_type'],item['area'],item['languages'],item['release_time'],item['update_time'],item['summary']))
			for play_url in play_urls:
				num=play_url.split('$')[0]
				play_url=play_url.split('$')[1]
				self.cursor.execute(sql_2,(item['tv_name'],num,play_url))
			self.con.commit()
		except Exception as e:
			self.con.rollback()
		return item

class ShowMysqlPipeline(object):
	def open_spider(self,spider):
		settings=get_project_settings()
		host=settings['HOST']
		port=settings['PORT']
		user=settings['USER']
		passwd=settings['PASSWD']
		db=settings['DB']
		charset=settings['CHARSET']
		self.con=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)

	def close_spider(self,spider):
		self.con.close()

	def process_item(self, item, spider):
		play_urls=item['play_urls']
		play_urls=play_urls.strip('[]').replace('\'','').replace(' ','').split(',')
		sql_1='insert into shows (show_img,show_name,director,staring,show_type,area,languages,release_time,update_time,summary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
		sql_2='insert into show_list (show_name,num,play_url) values (%s,%s,%s);'
		self.cursor=self.con.cursor()
		try:
			self.cursor.execute(sql_1,(item['show_img'],item['show_name'],item['director'],item['staring'],item['show_type'],item['area'],item['languages'],item['release_time'],item['update_time'],item['summary']))
			for play_url in play_urls:
				num=play_url.split('$')[0]
				play_url=play_url.split('$')[1]
				self.cursor.execute(sql_2,(item['show_name'],num,play_url))
			self.con.commit()
		except Exception as e:
			self.con.rollback()
		return item

class AnimationMysqlPipeline(object):
	def open_spider(self,spider):
		settings=get_project_settings()
		host=settings['HOST']
		port=settings['PORT']
		user=settings['USER']
		passwd=settings['PASSWD']
		db=settings['DB']
		charset=settings['CHARSET']
		self.con=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)

	def close_spider(self,spider):
		self.con.close()

	def process_item(self, item, spider):
		play_urls=item['play_urls']
		play_urls=play_urls.strip('[]').replace('\'','').replace(' ','').split(',')
		sql_1='insert into animation (animation_img,animation_name,director,staring,animation_type,area,languages,release_time,update_time,summary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
		sql_2='insert into animation_list (animation_name,num,play_url) values (%s,%s,%s);'
		self.cursor=self.con.cursor()
		try:
			self.cursor.execute(sql_1,(item['animation_img'],item['animation_name'],item['director'],item['staring'],item['animation_type'],item['area'],item['languages'],item['release_time'],item['update_time'],item['summary']))
			for play_url in play_urls:
				num=play_url.split('$')[0]
				play_url=play_url.split('$')[1]
				self.cursor.execute(sql_2,(item['animation_name'],num,play_url))
			self.con.commit()
		except Exception as e:
			self.con.rollback()
		return item

class FuliMysqlPipeline(object):
	def open_spider(self,spider):
		settings=get_project_settings()
		host=settings['HOST']
		port=settings['PORT']
		user=settings['USER']
		passwd=settings['PASSWD']
		db=settings['DB']
		charset=settings['CHARSET']
		self.con=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)

	def close_spider(self,spider):
		self.con.close()

	def process_item(self, item, spider):
		sql='insert into fuli (fuli_img,fuli_name,director,staring,fuli_type,area,languages,release_time,update_time,summary,play_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
		self.cursor=self.con.cursor()
		try:
			self.cursor.execute(sql,(item['fuli_img'],item['fuli_name'],item['director'],item['staring'],item['fuli_type'],item['area'],item['languages'],item['release_time'],item['update_time'],item['summary'],item['play_url']))
			self.con.commit()
		except Exception as e:
			self.con.rollback()
		return item