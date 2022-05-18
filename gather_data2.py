# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:23:37 2022

@author: wilamowsse01
"""

import os
import pandas as pd
from datetime import datetime
import query_maker
import file_name2
import add_logs2
import oracle_cn_encr

# Make a SQL query
country = input('Country: ')
table = input('Table name: ')
a = input('If selected column type 1/ If all columns type 0: ')
c = input('If where conditon type 1/ If no where condition type 0: ')
if int(a) == 1:
    columns = input('Type column names, separated by comma: ')
else:
    columns = ""
if int(c) == 1:
    condition = input('Type where condition: ')
else:
    condition = ""

query_maker.qry(country,table,a,c,columns,condition)
print(query_maker.q_table)

# Connect to Oracle
oracle_cn_encr.oracle_connect_encripted()
curs01 = oracle_cn_encr.orcl.cursor()

os.chdir('c:/dane/Python/gather_data2/Output')
results_table = curs01.execute(query_maker.q_table)

col = len(curs01.description)
col_names = [i[0] for i in curs01.description]
print(col_names)
table_out=pd.DataFrame(results_table.fetchall(),columns=col_names)
table_out_nrec = len(table_out)

oracle_cn_encr.orcl.close() 

# Create the uniqu name and save the files
now = datetime.now()
n = now.strftime("%Y%m%d%H%M%S")
file_name2.output_file_name(country,table,str(n),"","_")
print(file_name2.fl_n_txt)
print(file_name2.fl_n_csv)
table_out.to_csv(file_name2.fl_n_csv, index=False)
table_out.to_csv(file_name2.fl_n_txt, sep="\t", index=False)

# Keep the log
log_list = ['Country',country,'Table exported', table,'Columns_selected', columns, 'Where condition',condition, 'Records exported', str(table_out_nrec)]
add_logs2.add_log(log_list)
