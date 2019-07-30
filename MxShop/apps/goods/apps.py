#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/4/13 23:07
from django.apps import AppConfig



class GoodsConfig(AppConfig):
    name = 'goods'
    # 后台中app的名字是中文显示
    verbose_name = u"商品管理"

