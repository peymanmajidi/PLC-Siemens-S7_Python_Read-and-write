import pyodbc # remember: port number is so important!!!
print("Connecting...")
cnxn = pyodbc.connect(driver = "{FreeTDS}", server = "192.168.2.82", port = 1433, database="prototypedb", user="sa", password="server@1314")
print("Connected")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM [BarcodeTBL]')
for row in cursor:
    print('row = %r' % (row,))
