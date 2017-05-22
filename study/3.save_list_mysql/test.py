#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import xlrd

# print("start open excel file")
# data = xlrd.open_workbook("list.xlsx")
# print("start read excel file")
# table = data.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# print("there have",nrows,"finance")
# # print(nrows)
# # print(ncols)
# print("end program")

from sqlalchemy import create_engine
import tushare as ts

df = ts.get_stock_basics()
print(df.head())
print(df.dtypes)
print(df.index)
df['code'].astype(int)
print(df.dtypes)
# engine = create_engine('mysql://root:123456@127.0.0.1/finance?charset=utf8')
# df.to_sql('tick_data',engine)
# df.to_csv('./finance_list.csv')
