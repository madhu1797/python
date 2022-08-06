import sqlite3


## To Create Database


print("DB Opened .....")
db=sqlite3.connect('DATABASE_NEW')

#### To delete the particular row of table based on primary key
print("Started Deleting row=DGNU_2")
db.execute("DELETE from DEVICE where DEVICE_ID='DGNU_2'")
print("deleted successfully")
db.commit()
db.close()

