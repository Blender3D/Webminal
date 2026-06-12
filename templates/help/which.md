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

