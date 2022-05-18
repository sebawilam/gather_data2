# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:08:33 2022

@author: Seba
"""

def output_file_name (N_part1,N_part2,N_part3,N_part4,sep):
    global fl_n_txt, fl_n_csv
    if sep == '':
        fl_n_1 = N_part1 + N_part2 + N_part3 + N_part4
    else:
        fl_n_1 = N_part1 + sep + N_part2 + sep + N_part3 + sep + N_part4
    fl_n_txt =  fl_n_1 + '.txt'
    fl_n_csv =  fl_n_1 + '.csv'
    return fl_n_txt, fl_n_csv