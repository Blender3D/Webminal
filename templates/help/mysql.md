title: mysql

Did it say?

*`Welcome to the MySQL monitor`*
and more info like mysql version and others?

Now you are logged into interactive mysql prompt.
Normally prompt will be of the form
`mysql>` here we use `mysql$`. Just for fun!
(white lies are good!)

Lets first create a database: but wait, before that if you don't know what's a
database. Assume database as directory or folder where you store critical 
information in a specific format.
you can simply use 

        create database universe;

will create it.(you can't run create database
command, since we already created one just for 
you!..ok..ok..stop clapping your Hands)

Now inorder to use that database; type 

        use db_yourname;


For example,if `abc` is your login name, you've to type `use db_abc`
