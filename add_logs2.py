# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:57:02 2022

@author: wilamowsse01
"""

from datetime import datetime
from prettytable import PrettyTable

def get_string(self, **kwargs):

    """Return string representation of table in current state.
       ...
    """
    
def add_log(log_list):
    ptable = PrettyTable()
    ptable.field_names = ["Log description: ", "Log value: ", "Date: "]
    now = datetime.now()
    print(now)
    i = 1
    for x in log_list:
        if i % 2 == 1:
            log_desc = x
        else:
            log_val = x
            ptable.add_row([log_desc, log_val, str(now)])
        i = i+1
    
    file1 = open("log.log", "a")  # append mode
    file1.write('\n')
    file1.write(str(now))
    file1.write('\n')
    data = ptable.get_string()
    file1.write(data)
    file1.close()
    print("Log updated \n")
    print(ptable)
        