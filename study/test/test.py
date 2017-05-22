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

import tushare as ts

df = ts.get_stock_basics()
df.to_csv('./finance_list.csv')
