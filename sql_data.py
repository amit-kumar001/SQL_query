import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="Server@123", database="joins" )
print("connection successful")

cursor = db.cursor()
#*********************************************************
sql="CREATE TABLE final (id int NOT NULL AUTO_INCREMENT PRIMARY KEY , f_name varchar(10),l_name varchar(10),contact_no int,Time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP  )"
cursor.execute(sql)
db.commit()
#*********************************************************

sql="INSERT INTO final (f_name, l_name, contact_no) VALUES (%s, %s, %s)"
val=("Sushant", "Mishra",666688667,)
cursor.execute(sql, val) #Execute method executes a specified query
db.cursor()# store data into database
db.rollback()# rollback is an operation which returns the database to some previous state

#*********************************************************

cursor.execute("SELECT * FROM final")
result = cursor.fetchmany(2)#fetch() method, which fetches all rows from the the table.
result= cursor.fetchone()
result= cursor.fetchone()
for x in result:
  print(x)



#*********************************************************
# not null:- column can hold NULL values.
sql= "CREATE TABLE Persons (ID int NOT NULL, LastName varchar(25) NOT NULL, FirstName varchar(25) NOT NULL, Age int)"
sql= "ALTER TABLE Persons MODIFY Age int NOT NULL"
cursor.execute(sql)
db.commit()

#*********************************************************
#unique:- Ensures that all values in a column are different
sql= "CREATE TABLE Persons (ID int NOT NULL UNIQUE,LastName varchar(255) NOT NULL,FirstName varchar(255),Age int)"
sql= "ALTER TABLE Persons add UNIQUE(Age), add UNIQUE (id) " #to add UNIQUE constraints
sql= "ALTER TABLE Persons DROP INDEX Age " #to delete UNIQUE constraints
cursor.execute(sql)
db.commit()

#**********************************************************

#PRIMARY KEY:- constraint uniquely identifies each record in a table
sql= "CREATE TABLE Persons (ID int NOT NULL PRIMARY KEY,LastName varchar(255) NOT NULL,FirstName varchar(255),Age int)"
sql= "ALTER TABLE Persons ADD PRIMARY KEY (ID) " #to add PRIMARY KEY constraints
sql= "ALTER TABLE Persons DROP PRIMARY KEY " #to delete PRIMARY KEY constraints
cursor.execute(sql)
db.commit()



