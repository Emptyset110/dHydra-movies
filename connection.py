# -*- coding: utf8 -*-
"""
Config
Created on 03/08/2016
@description:	Connection for movie.py
@author: 		Wen Gu
@contact: 		emptyset110@gmail.com
"""

HEADERS_MAOYAN = {
	'Accept' : '*/*'
,	'Accept-Encoding'	:	'gzip, deflate, sdch'
,	'Accept-Language'	:	'en-US,en;q=0.8'
,	'Connection'		:	'keep-alive'
,	'Host'				:	'pf.maoyan.com'
,	'Referer'			:	'http://pf.maoyan.com/'
,	'User-Agent'		:	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
,	'X-Requested-With'	:	'XMLHttpRequest'
}

URL_MAOYAN = lambda date : 'http://pf.maoyan.com/history/date/box.json?date=%s&cnt=10' % date
