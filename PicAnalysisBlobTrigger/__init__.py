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
    logging.info(f"output set !!!")
    ### DB connectionしときます
    cursor = db_connection()
    logging.info(f"connection set !!!")
    ### SalesLT.Customerはテンプレートとしてあるテーブル
    sql = 'select count(*) from sales;' 
    logging.info(f"sql do !!!")
    logging.info(f"sql result : %d", query_output(sql))
    
### DB connectionを定義
def db_connection(sv=server, db=database, un=username, pw=password):    
    logging.info("sv", sv)
    logging.info("db", db)
    logging.info("un", un)
    logging.info("pw", pw)
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=tohokuujaeasqlservertest1.database.windows.net;DATABASE=tohokuujaeasqldatabasetest1;UID=tohokusqlserveradmin;PWD=tohokuadmin2023@')
    ### cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+sv+';DATABASE='+db+';UID='+un+';PWD='+ pw)
    return cnxn.cursor()

### SQLを発行
def query_output(sql):
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:  
        row = cursor.fetchone()
        logging.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        logging.info(row[0])
        return row[0]
