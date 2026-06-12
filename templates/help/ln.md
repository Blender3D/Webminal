title: ln

Great! you have created a link. There are two types of links, hardlinks.
where a same inode pointed by two different names and softlinks which 
work more like shortcuts.

Hard links are created by default.

	stat hello
and perform 

	stat dir2/dir3/dir4/hi.txt
see both uses same inode and link count shown as 2.
Soft links are created using the s switch.

	ln -s  dir2/dir3/dir4/hi.txt  softlink
again do 

	stat softlink
and examine its output.New inode is created for this new symbolic link "softlink" but link count remains as 1.
To remove individual file use

	 rm -i file2.txt 


