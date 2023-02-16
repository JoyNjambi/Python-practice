import sqlite3
conn=sqlite3.connect('Mitmidmorn.db')

conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'JOY',18,'MA-HILL','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(2,'CAROL',15,'eMOBILIS','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(3,'JOHN',17,'MANGU','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(4,'MATTHEW',25,'MKU','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(5,'FRIDAH',19,'ALLIANCE','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(6,'KEITH',19,'SUNSHINE','Male')")

conn.commit()
print("Records added successfully")
conn.close()