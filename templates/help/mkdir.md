title: mkdir

Did it say?

*`mkdir: created directory dir1`*

Wow,now you created a new  directory. Lets say you want to create more than 
one directory instead of invoking mkdir multiple(three) times-like.

	mkdir -v dir2
	mkdir -v dir2/dir3
	mkdir -v dir2/dir3/dir4
you can simply use 

	mkdir -vp dir2/dir3/dir4

"-p" option will create parent directories for "dir4" as needed.
In this case,it creates dir2,dir3 automatically.Now we have created 
4 directories.How to view them?

To view type 'ls' and press enter

	ls

