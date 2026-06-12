title: mv

will move a file into  directory dir4 and names it as hi.txt.
`so how mv is different from cp?`.Try `wm_ls` it will not show hello.txt.

When you use cp there exists two copies of a file
(similar to copy-paste "ctrl-c" and "ctrl-v") with mv
there is one copy (its cut-paste ctrl-x and ctrl-v).
unlike (cp,rm) other commands mv don't need "-r" for directories.

create a new directory dir5 

	wm_mkdir dir5 
now 

	mv dir2/*.txt dir5
	mv dir5  dir50
will move all "*.txt" files under dir2 into dir5.
then rename the directory "dir5" as "dir50".

with mv command we moved hello.txt under dir4,instead of 
accessing them as dir2/dir3/dir4/hi.txt everytime,we can create
a link and after that,you can access or edit `dir2/dir3/dir4/hi.txt` file
as simply `hello`

	ln  dir2/dir3/dir4/hi.txt hello 
