import sqlite3


## To Create Database


print("DB Opened .....")
db=sqlite3.connect('DATABASE_NEW')

## To update the particular values of table based on primary key
db.execute("UPDATE DEVICE set CPU_UTLIZATION=80 where DEVICE_ID='DGNU_1'")
print("DB Updated successfully")
db.commit()
db.close()




