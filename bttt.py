#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
import re
import string
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class BtttSpider(scrapy.spiders.Spider):
    name = "bttt"
    allowed_domains = ["bttt.la"]
    start_urls = [
        "http://www.bttt.la/subject/3629.html",
    ]
 
    def parse(self, response):
        current_url = response.url #爬取时请求的url
        print current_url
        
        hxs = HtmlXPathSelector(response)
        names = hxs.select('//div[@class="moviedteail"]/div[@class="moviedteail_tt"]/h1/text()').extract()
        for name in names:  
          print name.encode('utf-8')
          
        imdb = hxs.select('//div[@class="moviedteail"]/ul[@class="moviedteail_list"]/li/a[@title="imdb"]/text()').extract()
        print "".join(imdb)
        
        torrents = hxs.select('//div[@class="tinfo"]/a/@href').extract()
        for torrent in torrents:
          torrent_url = "http://www.bttt.la/download.php"
          action = "download"
          id = "".join(re.findall(r"id=(.+?)&", torrent))
          uhash = "".join(re.findall(r"uhash=(.+?)$", torrent))
          print torrent_url, action, id, uhash
        
        print "***************************************************************\n\n\n"
        
        count = re.findall(r"^http://www.bttt.la/subject/(.+?).html$", current_url)
        num = "".join(count)
        count = str(string.atoi(num) + 1)
        url = "http://www.bttt.la/subject/" + count + ".html"
        yield Request(url, callback=self.parse)