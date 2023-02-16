import sqlite3
conn=sqlite3.connect('Mitmidmorn.db')
print("Open Database Successfully")
conn.execute("CREATE TABLE Wanafunzi("
             "ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print( "Tables created successfully")
conn.close()