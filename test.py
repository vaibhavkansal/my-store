import sqlite3
def createtable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
        Type VARCHAR(40),
        DATE DATE,
        STATUS VARCHAR(30));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()
#createtable('qwea')
connection = sqlite3.connect("mytables4.db")
crsr = connection.cursor()
sa = f'''INSERT INTO qwea VALUES ('rtaqa','','es')'''
crsr.execute(sa)
connection.commit()
crsr.execute(f"SELECT * FROM qwea")
sele=crsr.fetchall()
print(sele)
crsr.execute(f"SELECT * FROM qwea WHERE DATE < '2013-01-17' AND DATE > '2009-1-17'")
sele=crsr.fetchall()
print(sele)
