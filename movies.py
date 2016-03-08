# -*- coding:utf-8 -*-
"""
电影数据接口接口：
Created on 03/08/2016
@author: Wen Gu
@contact: emptyset110@gmail.com
"""
import requests
import connection as CON
from pandas import DataFrame as df

class Maoyan:
	def __init__(self):
		self.session = requests.Session()
		pass

	"""
	获取电影票房数据：数据来源，猫眼
	"""
	def get_box(self, date):
		box = self.session.get(CON.URL_MAOYAN_DATE, params = CON.PARAM_DATE(date) ,headers = CON.HEADERS_MAOYAN)
		return box.json()

	def get_box_dataframe(self, date):
		box_dict = self.get_box(date)
		box_df = df.from_dict(box_dict["data"])
		return box_df

	def export_box_csv(self, date):
		box_df = self.get_box_dataframe(date)
		box_df.to_csv( '%s.csv'% date )

	def get_movie(self, movie):
		movie = self.session.get(CON.URL_MAOYAN_MOVIE, params = CON.PARAM_MOVIEID(movie), headers = CON.HEADERS_MAOYAN)
		return movie.json()

	def get_movie_dataframe(self, movie):
		movie_dict = self.get_movie(movie)
		movie_df = df.from_dict(movie_dict["data"])
		return box_df

	def export_movie_csv(self, movie):
		movie_dict = self.get_movie(movie)
		df.from_dict(movie_dict).to_csv( "%s-%s-%s" % (movie_dict["releaseDate"], movie_dict["movieName"],str(movie) ) )