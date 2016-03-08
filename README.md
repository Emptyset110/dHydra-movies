# dHydra-movies
dHydra电影票房数据模块

## Prerequisite
 - python 3.4+
 - 你还需要`requests`模块，可以采用`pip install requests`安装

## Getting Started
进入movies.py目录，运行python
```
import movies 	#导入movies.py

movies = movies.Maoyan()	#实例化Maoyan类

movies.get_box("2014-03-07")	#获取某一日票房，日期格式YYYY-MM-DD
```
返回格式为json