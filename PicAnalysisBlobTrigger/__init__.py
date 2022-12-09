import logging
import pyodbc
import azure.functions as func

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
###    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:tohokuujaeasqlservertest1.database.windows.net;1433;Database=tohokuujaeasqldatabasetest1;Uid=tohokusqlserveradmin;Pwd=tohokuadmin2023@;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

###    cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tohokuujaeasqlservertest1.database.windows.net;Database=tohokuujaeasqldatabasetest1;Uid=tohokusqlserveradmin;Pwd=tohokuadmin2023@;')
    logging.info("connect success !!!")
###    cursor = cnxn.cursor()
### logging.info(database)
###    cursor.execute("select top(1) * from Todo")
###    while row:
    ###print (str(row[0]) + " " + str(row[1]))
###        row = cursor.fetchone()
###        logging.info(row[0])
### logging.info(username)
    ###cursor.commit()
### logging.info(password)

    logging.info('finished')
