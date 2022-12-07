## libraries
import logging
import azure.functions as func
import pyodbc

## initial setting
server = 'tohokuujaeasqlservertest1.database.windows.net'  
database = 'tohokuujaeasqldatabasetest1'  
username = 'tohokusqlserveradmin'  
password = 'tohokuadmin2023@'
cursor = ""

def main(inputblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputblob.name}\n"
                 f"Blob Size: {inputblob.length} bytes")
    logging.info(f"github actions setting !!!")
    outputblob.set(inputblob)
    
    ### DB connectionしときます
    cursor = db_connection()

    ### SalesLT.Customerはテンプレートとしてあるテーブル
    sql = 'select count(*) from sales;' 
    logging.info(f"sql result : %d", query_output(sql))
    
### DB connectionを定義
def db_connection(sv=server, db=database, un=username, pw=password):    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+sv+';DATABASE='+db+';UID='+un+';PWD='+ pw)
    return cnxn.cursor()

### SQLを発行
def query_output(sql):
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:  
        row = cursor.fetchone()
    return row[0]
