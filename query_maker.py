# -*- coding: utf-8 -*-
"""
Created on Mon May 16 22:17:05 2022

@author: wilamowsse01
"""

def qry (country,table,a,c,columns,condition):
    global q_table
    if int(a) == 1:
        select = columns
    else:
        select = " * "
    if int(c) == 1:
        wh = "where " + condition
    else:
        wh = ""
    print ("Exporting table: " + table)     
    q_table = "SELECT " + select + " FROM VLDSYS_" + country + "." + table + " " + wh
    # print(q_table)
    return q_table

# qry("FR","stores","1","0","ac_nshopid, ac_shopdescription","")