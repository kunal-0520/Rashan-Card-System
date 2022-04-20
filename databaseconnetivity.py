
import pyodbc as odbc

# Trusted Connection to Named Instance
connection = odbc.connect('DRIVER={SQL Server};'
                            'SERVER=server name;'
                            'UID=SA;'
                            'PWD=perficient@123;'
                            'DATABASE=database name;'
                            'Trusted_Connection=no;')

cursor=connection.cursor()
cursor.execute("SELECT * FROM tablename")

while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row)

cursor.close()
connection.close()



