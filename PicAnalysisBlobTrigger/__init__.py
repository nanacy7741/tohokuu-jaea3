import logging
import pyodbc
import azure.functions as func

def main(inputblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    
    logging.info(f"functions start !!!")
### outputblob.set(inputblob)
### cnxn = pyodbc.connect("Server=tcp:tohokuujaeasqlservertest1.database.windows.net,1433;Initial Catalog=tohokuujaeasqldatabasetest1;Persist Security Info=False;User ID=tohokusqlserveradmin;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;")
### cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:tohokuujaeasqlservertest1.database.windows.net;1433;Database=tohokuujaeasqldatabasetest1;Uid=tohokusqlserveradmin;Pwd=tohokuadmin2023@;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

    cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:tohokuujaeasqlservertest1.database.windows.net;Database=tohokuujaeasqldatabasetest1;Uid=tohokusqlserveradmin;Pwd=tohokuadmin2023@;')
    cursor = cnxn.cursor()
    logging.info("connect success !!!")

    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        logging.info(row[0])
        row = cursor.fetchone()

    logging.info('finished !!!')
