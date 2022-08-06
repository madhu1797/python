import sqlite3 


## To Create Database


print("DB Creation started .....")
db=sqlite3.connect('DATABASE_NEW')
print("DB Created successfully")


## To create table in Database

print("Table creation in DB --> started .....")
#db.execute('''CREATE TABLE DEVICE (DEVICE_ID INT PRIMARY KEY	NOT NULL,
#DEVICE_NAME	TEXT	NOT NULL,
#TYPE_OF_TESTING	TEXT	NOT NULL,
#CPU_UTLIZATION NOT_NULL, );''')
print("TABLE Created in DB successfully")

## To insert values to Database

print("Started inserting the values to database")
#db.execute("INSERT INTO DEVICE (DEVICE_ID,DEVICE_NAME,FEATURE,CPU_UTLIZATION) \
#      VALUES ('DGNU_1', 'HyperSprout', 'STABLITY_TESTING', '70' )");

db.execute("INSERT INTO DEVICE (DEVICE_ID,DEVICE_NAME,FEATURE,CPU_UTLIZATION) \
      VALUES ('DGNU_2', 'Datavine_Meshcard', 'STABLITY_TESTING', '75' )");

print("values inserted in database")

##This method commits the current transaction.
##If you don't call this method, anything you did since the last call to commit() is not visible from other database connections.

db.commit()
db.close()

