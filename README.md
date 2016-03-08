# dHydra-movies
dHydra电影票房数据模块

## Prerequisite
 - python 3.4+
 - 你还需要`requests`模块，可以采用`pip install requests`安装
 - 还需要`pandas`模块，可以采用`pip install pandas`安装

## Getting Started
进入movies.py目录，运行python
```python
#导入movies.py
import movies

#实例化Maoyan类
m = movies.Maoyan()

#获取某一日票房,日期格式YYYY-MM-DD,返回格式为dict
m.get_box("2014-03-07")

#获取某一日票房,日期格式YYYY-MM-DD,返回格式为pandas.DataFrame
m.get_box_dataframe("2014-03-07")

#将某日电影票房数据导出为当前文件夹下的csv文件,文件名为"日期.csv"
m.export_box_csv("2014-03-07")

#获取某电影数据,参数为电影ID,返回数据为dict
m.get_movie(246286)

#获取某电影数据,参数为电影ID,返回数据为pandas.DataFrame
m.get_movie_dataframe(246286)

#将某电影导出为当前文件夹下的csv文件，文件名命名规则为"上映日期-电影名-电影id"
m.export_movie_csv(246286)

#通过查询导演,演员,或者电影名字来获取电影id,返回值是一个List
m.get_movie_id("孙红雷")
['342871', '246439', '245935', '78171', '78082', '245967', '789', '748', '3', '402', '79', '14142', '492', '247524', '686', '178', '59305', '230', '294', '246589', '146', '959', '23732', '226931', '17618', '239255']
m.get_movie_id("夏洛特烦恼")
['246082']
```