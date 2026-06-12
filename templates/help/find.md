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

After you have practised above commands,move to our final lesson 

	lesson8
see you later.
