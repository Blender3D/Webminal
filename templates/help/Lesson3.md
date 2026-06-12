title: Lesson3 - Copy,rename,delete files 

### Lesson3 - Copy,rename,delete files 

On `Lesson1`,you learned about directories.
With `Lesson2`,you learned about files.
Now lets learn general file operations.

Now check this command

	du


----



title: du

it displays the disk usage of current directory.(Please note the current 
total of du output).Use  the h switch to output in a human readable format
and the x switch to exclude other file systems and ~ denotes your home. 

	du -xh ~

>`Tips and tricks:`

du can take a long time so you can specify the max.directory depth
using "--max-depth" option.

	du --max-depth 3 ~

Now lets copy  `hello.txt` to `dir2` directory.

	cp -v hello.txt dir2

title: cp

now file is copied to new location.Now compute the usage again using,
`du` now you should see usage has been increased by file size.

>`Tips and tricks:`

	 cp -v hello.txt dir2/file2.txt

This will copy hello.txt into dir2 at the same time, rename it as "file2.txt".


	cp  -vr dir2/*.txt dir2/dir3 

This will copy all files ending with ".txt" from dir2 into dir2/dir3.

	cp -vr dir2/dir3  .

This will copy the directory named "dir3" to current directory.

Use `ls`,it should show you dir3.

now we have copied few files,how do we verify its file integrity?simple 
`cat` should be enough.But If its large file or binary file,we can't use
cat.We have to use,

	md5sum hello.txt 
title: md5sum

`b8d5079c5d6a9dbb3294b31d318d74c0` is the calculated checksum
for a file.This helps with detecting accidental or deliberate 
file corruption.

When transfering a file from machine to another or downloading 
files from internet,to verify the file integrity compare md5sum 
on source and destination machines,

	md5sum dir2/hello.txt
should be same as 

	md5sum hello.txt

now lets move to another command,

	mv hello.txt dir2/dir3/dir4/hi.txt

title: mv

will move a file into  directory dir4 and names it as hi.txt.
`so how mv is different from cp?`.Try `ls` it will not show hello.txt.

When you use cp there exists two copies of a file
(similar to copy-paste "ctrl-c" and "ctrl-v") with mv
there is one copy (its cut-paste ctrl-x and ctrl-v).
unlike (cp,rm) other commands mv don't need "-r" for directories.

create a new directory dir5 

	mkdir dir5 
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


title: rm

will prompt you with a message.`rm: remove regular empty file 'file2.txt'?`
type `y` to delete the file.To remove directory,
first remove it's contents using option "r",

	rm -ri dir50/*


>`Tips and tricks:`

If you want to remove files content without begin prompted for confirmation use -f option.
It's extremely dangerous to use "rm -rf",because you may delete very important files by
mistake-so make sure you delete correct files before running rm -rf"


	rm -rf junk/*
	rmdir  dir50

rmdir will remove an empty directory. so thats end of lesson3.
Good keep going :) Time for
lesson4.
