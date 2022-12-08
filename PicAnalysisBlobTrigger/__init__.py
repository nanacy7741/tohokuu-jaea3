## libraries

import azure.functions as func
import logging
import os
import struct
import sys

import pyodbc

def main(inputblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputblob.name}\n"
                 f"Blob Size: {inputblob.length} bytes")
    logging.info(f"github actions setting !!!")

### outputblob.set(inputblob)
    
### server = 'tcp:tohokuujaeasqlservertest1.database.windows.net' 
### database = 'tohokuujaeasqlservertest1' 
### username = 'tohokusqlserveradmin' 
### password = 'tohokuadmin2023@' 

### cnxn = pyodbc.connect("Server=tcp:tohokuujaeasqlservertest1.database.windows.net,1433;Initial Catalog=tohokuujaeasqldatabasetest1;Persist Security Info=False;User ID=tohokusqlserveradmin;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;")
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:tohokuujaeasqlservertest1.database.windows.net,1433;Database=tohokuujaeasqldatabasetest1;Uid=tohokusqlserveradmin;Pwd=tohokuadmin2023@;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
### logging.info(server)
    cursor = cnxn.cursor()
### logging.info(database)
    cursor.execute("INSERT INTO Todo VALUES (?, ?, ?)", "2", "frompython", "2022-12-07T00:00:00")
### logging.info(username)
    cursor.commit()
### logging.info(password)
    logging.info('finished')
