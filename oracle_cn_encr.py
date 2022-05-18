# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:40:05 2022

@author: wilamowsse01
"""

# change in case different path to Oracle client
import os
os.chdir('C:/Oracle/instantclient_18_3')
import cx_Oracle
from cryptography.fernet import Fernet

pth_f = 'c:/dane/Python/Crypto/'
fl_key = 'key.key'
pth = pth_f + fl_key

def load_key():
    return open(pth, "rb").read() #Opens the file, reads and returns the key stored in the file


# decryption the connection string
def oracle_connect_encripted():
        
    key = load_key() # Loads the key and stores it in a variable
    f = Fernet(key)
    
    try:
        server_n = input("Type server name for connection decoding: ") # Takes the server name
        server_ne = server_n.upper() + '.ocn'
        
        pth_ocn = pth_f + server_ne
        
        with open(pth_ocn, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
    except:
        print("The server name encripted file do not exist")
    else:
        decrypted_data = f.decrypt(encrypted_data).decode()
        # connect to Sirval Oracle server
        ORACLE_CONNECT = decrypted_data
        global orcl
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)
        return orcl