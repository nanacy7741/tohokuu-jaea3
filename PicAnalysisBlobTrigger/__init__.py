## libraries
import azure.functions as func
import logging
import os
import pyodbc
import struct
import sys

def main(inputblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputblob.name}\n"
                 f"Blob Size: {inputblob.length} bytes")
    logging.info(f"github actions setting !!!")

### outputblob.set(inputblob)
    
    server = 'tcp:tohokuujaeasqlservertest1.database.windows.net' 
    database = 'tohokuujaeasqlservertest1' 
    username = 'tohokusqlserveradmin' 
    password = 'tohokuadmin2023@' 

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    logging.info(server)
    cursor = cnxn.cursor()
    logging.info(database)
    cursor.execute("INSERT INTO Todo VALUES (?, ?, ?)", "2", "frompython", "2022-12-07T00:00:00")
    logging.info(username)
    cursor.commit()
    logging.info(password)
    logging.info('finished')
