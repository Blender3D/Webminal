title: A Quick mysql tutorial in 7394 hours!

So you are one of those tranditional/rigid user who  believe 
in SQL and arguing/fighting against NOSQL?

Welcome to a Quick mysql tutorial in 7394 hours!! 
(if you don't know mysql and computer and english.)

yeah, recently conducted Bogus inc scientific research results show 
that you'll need approx.7394 hours to complete this tutorial 
especially if you don't have any clue about what's mysql and 
computer and english!


Lets login to mysql client, simply type

	mysql

Now press Enter key then see what happens.

ps: To make login simple for you, we used an alias for mysql so
above command will get expanded like `mysql -u yourname -p password`
automagically!
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
title: use

Did it say?

*`Database changed`*

great!.You are ready to record some
data into this database.

To store information,you must provide
a name and format.This is known as 
table. To create a table named 'planets'
type,

		create table planets(name varchar(15), 
		  position int, has_moon boolean);

Press enter key it should display 
*`Query OK, 0 rows affected `*

title: use

Congrats! you successfully created table
with format.

To see list of tables available on this
database type 

        	show tables;

title: show

Wait a second, let me guess .hmm..

*thinking*

It should have displayed something like 


		+-------------------+
		| Tables_in_universe|
		+-------------------+
		| planets           |
		+-------------------+

right?,yes I know I know , I have IQ 180!
(+ or - 170 :P)

to view the format/structure of this
table.do  type,

        describe planets;


title: describe

Did you see the following?

		+----------+-------------+------+-----+---------+-------+
		| Field    | Type        | Null | Key | Default | Extra |
		+----------+-------------+------+-----+---------+-------+
		| name     | varchar(15) | YES  |     | NULL    |       |
		| position | int(11)     | YES  |     | NULL    |       |
		| has_moon | tinyint(1)  | YES  |     | NULL    |       |
		+----------+-------------+------+-----+---------+-------+
		3 rows in set

This is what we used in create table command 
right?If you find anything missing report a 
bug to mysql community :P

So we created a 'directory/folder' (read as  database)
and 'filename' (read as table) with specfic
'extention' (read as format).Now its time
to 'write' (read as insert) some 'data' (read as record).

Lets first add our home (earth).We know its 
at third position from sun and has a moon.

        insert into planets values ('earth',3,1);


title: insert

Now lets add our possible future home,

        insert into planets values ('mars',4,2);

mars has 2 moons ! Just take a break, imagine
how is it to live in a place with two moons!  :)

yes,that would be cool ;)

okay,now we wrote two records into the table.

To retrieve these data from table,type

        select * from planets;


title: select

it shows

		+-------+----------+----------+
		| name  | position | has_moon |
		+-------+----------+----------+
		| earth |        3 |        1 |
		| mars  |        4 |        2 |
		+-------+----------+----------+
great!
(still dreaming about 2 moons sight? get
back to earth!)

Lets assume,you like to retrieve only those
record which has only one moon.For this
just append `where` condition to above
select query.

        select * from planets where has_moon=1;
		
we can modify the above query a little bit more,
we know we are selecting records with has_moon=1,
so ignore that last field in the output,replace `*`
with column names like

        select name,position from planets 
          where has_moon=1;

See - Its simple!. Now do `update planet;`

title: update 

that should have displayed some error message.

Because you (yes,its you not my fault :P) didn't 
tell 'what' column to update and 'where' to 
update.

OMG,we entered some wrong data for earth,It appears recently
it  moved to 2 place in our solar system! need proof? go 
outside at 13:00.So we need to edit that record. How to do 
that? Here comes 'update' to your rescue.

        update planets set position=2 
	  where name="earth";

Now go and view results again via select query.
Now its time to trash something.Lets delete mars!

Say good bye to "Spirit".We going to destory it.

        delete from planets where name="mars";

title: delete 

RIP Spirit (2003-2013)


Thats it for a short tutorial on mysql!
Type 
        exit;

to quit the MySQL prompt.

Stayed tuned for more and play around
with mysql commands.!

Happy learning, No hacking please :D 

