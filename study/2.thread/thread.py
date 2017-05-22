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

import threading
from time import ctime, sleep

number = 0

def music(func):
    print("this is music")
    number = 1
    # for i in range(2):
        # print("I was listening to", func,ctime())
        # sleep(1)

def move(func):
    print("this is move")
    number = 2
    # for i in range(2):
        # print("I was at the",func,ctime())
        # sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

def main():
    for t in threads:
        t.setDaemon(True)
        t.start()
    
    t.join()
    print("number = ", number)
    print("all over", ctime())

if __name__ == '__main__':
    main()
