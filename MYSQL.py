import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='myuser', passwd='mypass', db='mydb')
conn.autocommit(True)

cursor = conn.cursor()
# 1.
#cursor.execute('CREATE TABLE `test_table` (`id` INT NULL, `users` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));')
#cursor.execute('CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)  ')

# Create a table in your remote database named “dogs”
# with three columns all NN (not null):
# - VARCHAR (40) – name
# - INT – age
# - VARCHAR  (30) – breed
'''''''''
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
'''''''''
def create_table():
    cursor.execute('CREATE TABLE dogs(name varchar(40) NOT NULL, age int NOT NULL, breed varchar(30) NOT NULL) ')
    cursor.close()
#create_table()

# 2. Insert 3 dogs with different values
'''''''''
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
'''''''''
def add_values():
    cursor.execute("INSERT INTO Rv5gjY4CsZ.dogs (name, age, breed) VALUES ('Eshel', 11, 'zeev')")
    cursor.execute("INSERT INTO Rv5gjY4CsZ.dogs (name, age, breed) VALUES ('Bony', 3, 'pincher')")
    cursor.execute("INSERT INTO Rv5gjY4CsZ.dogs (name, age, breed) VALUES ('Shun', 5, 'pincher')")
    cursor.close()
#add_values()


# 3. Update second dog age from one value to another
'''''''''
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
'''''''''
def update_val():
    cursor.execute("UPDATE dogs SET age  = 5 WHERE name = 'Bony'")
    cursor.close()
# update_val()


# 4. Delete the third dog from table
'''''''''
DELETE FROM table_name WHERE condition;
'''''''''
def delete_row():
    cursor.execute("DELETE FROM dogs WHERE name = 'Shun'")
    cursor.close()
#delete_row()

# 5. Query table and print all dogs names
def select_table():
    cursor.execute("SELECT * FROM dogs;")
    for row in cursor:
        print(row)
        cursor.close()

select_table()
conn.close()

