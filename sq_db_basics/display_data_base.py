import sqlite3


## To Create Database


print("DB Creation started .....")
db=sqlite3.connect('DATABASE_NEW')
print("DB Created successfully")


##To display all values in the database
#a=db.execute("SELECT * FROM DEVICE")
#a=db.cursor()
c=db.execute("SELECT DEVICE_ID, DEVICE_NAME, FEATURE, CPU_UTLIZATION from DEVICE");
print("contents present in DEVICE table of DATABASE_NEW")
for i in c:
	print("DEVICE_ID:",i[0])
	print("DEVICE_NAME:",i[1])
	print("FEATURE:", i[2])
	print("CPU_UTLIZATION", i[3], "\n")
print("Operation done successfully")
#print(a)
