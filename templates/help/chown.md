title: chown

`chown: changing ownership of file1.txt: Operation not permitted`

oh,thats expected error message,you can use chown only as root user,
but anyway thats the syntax/usage of chown command.Now we can change
file owner and group,by `chown root:staff file1.txt`

This does the same, but additionally changes the group to "staff"

>`Tips and tricks:`

To change permission on all files and sub-directories, use the -R switch.

	chown root:staff -R ~/dir2

Use option "--from" to change files that belongs to specific user group.

	chown --from=webminal:webminal root:staff -R ~/dir2

will change the files the belong to webminal user and webminal group to root
and other user files left as it is.Lets change the group alone-

	chgrp root file1.txt
