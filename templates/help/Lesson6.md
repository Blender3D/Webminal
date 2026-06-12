title: Lesson6 - Changing file attributes

### Lesson6 - Changing file attributes

Lets begin with a command that manipulates pathname,

	dirname dir2/dir3/dir4/hi.txt



----


title: dirname

strip non-directory suffix from path name ,gave you the output

	dir2/dir3/dir4

lets use the same path with different command this time

	basename dir2/dir3/dir4/hi.txt




title: basename

this strips directory and suffix from pathname and gives the last entry.

	hi.txt

Pretty useful commands :D lets change file access permission

	chmod -v 666 file1.txt

title: chmod


You should have seen a output like `mode of file1.txt changed to 0666 (rw-rw-rw-)`

That will set the file "file1.txt" to be "world writeable".This means 
the owner, group and others can read and write into file. The same 
effect can be achived (remember you can verify it by using `stat file1.txt`) 
by

	chmod a+rw file1.txt

where as below makes it so that no one can read or write into this file, not even it's owner!

	chmod a-rw file1.txt

with next command only owner can read or write into this file. `chmod u+rw file1.txt`.
`Tips and tricks:` To change permission for more than one file  use the -R switch

	chmod -R 644 ~/chmod_dir
now to change file owner , `chown root file1.txt`
title: chown

`chown: changing ownership of file1.txt: Operation not permitted`

oh,thats expected error message,you can use chown only as root user,
but anyway thats the syntax/usage of chown command.Now we can change
file owner and group,by `chown root:staff file1.txt`

Note: Rest of commands on lesson6 are expected to fail with below message,
they are listed here for sake of completeness.

`chown: changing ownership of file1.txt: Operation not permitted`

This does the same, but additionally changes the group to "staff"

>`Tips and tricks:`

To change permission on all files and sub-directories, use the -R switch.

	chown root:staff -R ~/dir2

Use option "--from" to change files that belongs to specific user group.

	chown --from=webminal:webminal root:staff -R ~/dir2

will change the files the belong to webminal user and webminal group to root
and other user files left as it is.Lets change the group alone-

	chgrp root file1.txt
title: chgrp

	chgrp: changing group of `file1.txt': Operation not permitted

hehe..again thats expected error message :) ,you can use chgrp only as root user,
but anyway thats the syntax/usage of chgrp command.

>`Tips and tricks:`

To change the group of dir2 and subfiles to "root". 

	chgrp -hR root dir2

Thats it we have completed lesson6.

