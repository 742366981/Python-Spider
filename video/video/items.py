# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 详情页地址
    detail_url=scrapy.Field()
    # 图片
    movie_img=scrapy.Field()
    tv_img=scrapy.Field()
    show_img=scrapy.Field()
    animation_img=scrapy.Field()
    fuli_img=scrapy.Field()
    # 片名
    movie_name=scrapy.Field()
    tv_name=scrapy.Field()
    show_name=scrapy.Field()
    animation_name=scrapy.Field()
    fuli_name=scrapy.Field()
    # 导演
    director=scrapy.Field()
    # 主演
    staring=scrapy.Field()
    # 类型
    movie_type=scrapy.Field()
    tv_type=scrapy.Field()
    show_type=scrapy.Field()
    animation_type=scrapy.Field()
    fuli_type=scrapy.Field()
    # 制片地区
    area=scrapy.Field()
    # 语言
    languages=scrapy.Field()
    # 上映时间
    release_time=scrapy.Field()
    # 最后更新
    update_time=scrapy.Field()
    # 剧情介绍
    summary=scrapy.Field()
    # 播放地址
    play_url=scrapy.Field()
    play_urls=scrapy.Field()
