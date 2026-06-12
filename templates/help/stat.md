title: stat

carefully examine few important fields the output. The first line
shows the `filename`.second line says its a `regular file` with
size as `18`.Third  line shows `Inode` number and no.of `links`
to that inode.

Fourth one,says `owner(Uid),group(Gid)` who has read-write permission
but other have read permission.Final three lines show `access,modified 
and change` time.They mean:

	access - when the file was last accessed/read.
	modified - when the contents was last 
		 modified written.
	change - denotes changes to files metadata
		like changing user permission.


Now lets do a `stat` on directory.

	stat dir1

Compare the previous `stat` "hello.txt" output with "dir1",before you move.
especially find out "dir1" type.That marks the end of lesson2!.Well done.

	lesson3
to move to lesson3.

