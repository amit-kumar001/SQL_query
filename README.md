# SQL_query
## Key features
<ol>
<li>class cursor:- Allows Python code to execute <strong>SQL</strong> commands in a database session. Cursor contains information on a selected statements written in sql. It executes statements accordingly.
<ol> 
  <li>How do you make a connection cursor in Python
  First:- Establish a connection to the <strong>SQL database</strong> by creating a connection object <strong>(db.cursor())</strong>. Next, create a cursor object using connection object <strong>(db.cursor())</strong>. Then, execute the statements.</li> 
</li>
</ol></br> 

<li><strong>connection.commit()</strong>: Refer to the statement <strong>db.commit()</strong> for understanding <strong>connection.commit()</strong>. It is required to make the changes, otherwise no changes are made to the table.
<ol>
<li>This method sends a <strong> COMMIT</strong> statement to the <strong>MySQL server</strong>,<strong> Python/SQL</strong> does not have autocommit, it is important to call this method after every transaction that modifies data for tables which uses transactional storage engines. </li>
</ol></br> 
<li><strong>rollback</strong> used to restore the database to its original state.</li>
<ol>
<li><strong>Connection.rollback</strong>- It refers to statement <strong>db.rollback()</strong>. It reverts the changes made by the current transaction.</li>
</ol></br> 

<li>To insert a single row into the table, we can use <strong>connection.execute().</strong> When we have to insert two or more than two rows into the table on that case we have to use <strong>connection.executemany()</strong> method.</li></br>
<li>fetch:-
<ol>
<li><strong>fetchall()</strong> method used to fetch all rows from the database table.</br>
Let see the example below.</br>
<strong>Output:-</strong></br>
(1, 'Mayank', 'Kandhari', 998889988, datetime.datetime(2019, 3, 8, 10, 53))</br>
(2, 'Sakshi', 'Rekhi', 889998899, datetime.datetime(2019, 3, 8, 10, 53))</br>
(3, 'Rajan', 'Raj', 776688667, datetime.datetime(2019, 3, 8, 10, 55, 19))</br>
</li></br> 

<li><strong>fetchone()</strong>:- This method returns one record as a tuple, If there are no more records then it returns None.</br>
<strong>Output:-</strong></br>
1</br>
Mayank</br>
Kandhari</br>
998889988</br>
2019-03-08 10:53:00</br>
</li></br> 

<li><strong>fetchmany(number_of_records)</strong>:-This method accepts number of records to fetch and returns tuple where each records itself is a tuple. If there are not more records then it returns an empty tuple.</br>
<strong>Output:-</strong></br>
(1, 'Mayank', 'Kandhari', 998889988, datetime.datetime(2019, 3, 8, 10, 53))</br>
(2, 'Sakshi', 'Rekhi', 889998899, datetime.datetime(2019, 3, 8, 10, 53))</br>
</li></li></br> 
</ol>
<li>Data type
<ol>
<li><strong>varchar</strong>:-It can be store 65,535 characters. But it has a limitation of maximum row size of 65,535 bytes. It means including all columns, it must not be more than 65,535 bytes.</li></br> 

<li><strong>MySQL TIMESTAMP</strong> is a data type that holds the combination of date and time. The format of a <strong>TIMESTAMP</strong> column is <strong>YYYY-MM-DD HH:MM:SS</strong> which is fixed at 19 characters. The TIMESTAMP value has a range from <strong>'1970-01-01 00:00:01'</strong> UTC(Coordinated Universal Time) to <strong>'2038-01-19 03:14:07'</strong> UTC</li></br>
<li>integer is a data type, by default value is int(11).</li></li>
</ol></br>

<li>Constraints:-
<ol>
<li>
  The <strong>NOT NULL</strong> constraint impose a column to not accept NULL values. which means that you cannot insert a new record, or update a record without adding a value to this field.
<ol>  
<li>syntax for NOT NULL in new table:-</br>
     CREATE TABLE table_name (column_name1 datatype NOT NULL, column_name2 datatype NOT NULL, column_name3 datatype , column_name4 datatype)</li></br>
<li>syntax to define NOT NULL in existing table:-</br>
    ALTER TABLE table_name MODIFY column_name3 datatype NOT NULL</li>
</ol>
</li></br>

<li><strong>UNIQUE</strong> and <strong>PRIMARY KEY</strong> constraints provide a guarantee for uniqueness for a column or set of columns. We can have many <strong>UNIQUE</strong> constraints in one table, but only one <strong>PRIMARY KEY</strong> constraint in one table.
<ol>
<li>syntax for UNIQUE key in new table:-</br>
    CREATE TABLE table_name (column_name1 datatype NOT NULL UNIQUE, column_name2 datatype NOT NULL,column_name3 datatype,column_name4 datatype)</li>
<li>syntax to define UNIQUE in existing table:-</br> 
   ALTER TABLE table_name add UNIQUE(column_name2), add UNIQUE (column_name4)</li>
<li> syntax to delete UNIQUE constraints:-</br>
    ALTER TABLE Persons DROP INDEX column_name4</li>
</ol>
</li>

<li><strong>primary key</strong> is a field in a table which uniquely identifies each row or record in a database table. Primary keys must contain unique values. A primary key column cannot have NULL values.
<ol>
<li> syntax for primary key in new table:-</br>
      CREATE TABLE table_name (column_name1 datatype NOT PRIMARY KEY, column_name2 datatype NOT NULL,column_name3 datatype,column_name4 datatype)</li>

<li> syntax to define primary key in existing table.:-</br>
       ALTER TABLE table_name ADD PRIMARY KEY (column_name1)</li>

<li> syntax to delete primary key:-</br>
     ALTER TABLE table_name DROP PRIMARY KEY</li>
</ol>     
</li>

</ol>
</li>
</ol>






 

  
