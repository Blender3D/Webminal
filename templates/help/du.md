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

