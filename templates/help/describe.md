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


