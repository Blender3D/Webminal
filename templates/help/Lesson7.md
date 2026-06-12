title: Lesson7 - Locate file and its type

### Lesson7 - Locate file and its type

Often we need  to figure out a file type,for such task,
we can use

	file linux.txt

----


title: file

determines the type of a file as ASCII text

	file /dev/null
`/dev/null:   characater special` says,its a character device.

>`Tips and tricks:`

You can also find about file system details of special devices.
(below command listed here for sake of completeness, you will
get permission denied error message)

	file -s /dev/sda2

says
	/dev/sda2: x86 boot sector, code offset 0x52, OEM-ID "NTFS    ", 
	sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, 
	heads 255, hidden sectors 161792, dos &lt; 4.0 BootSector (0x80)

often we need to find the location of a certain file

	whereis ls
title: whereis

you should see an output

	ls: /bin/ls /usr/share/man/man1p/ls.1p.gz /usr/share/man/man1/ls.1.gz 

`whereis` command will locate source files and binaries,lets
see another example,finding source file 

	whereis stdio.h

will give you

	stdio: /usr/include/stdio.h /usr/share/man/man3/stdio.3.gz

Assume,you have installed two version a php (php4 and php5),when you simply type 

	php
which version will get executed?we don't know. In order to find it out,we use

	which php

title: which

To locate a binary file or if you have two version of a binary 
file installed ,you can find "which"  one is currently used with 
this command.

Can we use which command to search for a  file on a given directory?
No,we can't.  "which" searches only pre-defined directories shown 
by 
	echo $PATH. 

so in order to search a file on any directory,

	find ~ -name "linux.txt"

title: find

Searches for files in a directory hierarchy.

>`Tips and tricks:`

To find regular files and invoke the file command on the results, run

	find . -type f -exec file '{}' \;

To find regular files and display their attributes using the ls command, run

	
	find . -type f -exec ls -l '{}' \;

To find files over 20 bytes in size and list them out, run


	find ~ -type f -size +20c -exec ls -hl {} \;

What this last command does is left as an exercise for you.

	find ~ -type f -size +20c -exec cp dir1 {} \;

After you have practised above commands,move to our final lesson see you later.
