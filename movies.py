# -*- coding:utf-8 -*-
"""
电影数据接口接口：
Created on 03/08/2016
@author: Wen Gu
@contact: emptyset110@gmail.com
"""
import requests
import connection as CON

class Maoyan:
	def __init__(self):
		self.session = requests.Session()
		pass

	"""
	获取电影票房数据：数据来源，猫眼
	"""
	def get_box(self, date):
		box = self.session.get(CON.URL_MAOYAN(date), headers = CON.HEADERS_MAOYAN)
		return box.json()