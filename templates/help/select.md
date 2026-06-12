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

