title: grep

`grep` searches for matching words or line on the file
To search entire directory of files, supply the directory name

	grep -r 'Hello' .	

By default grep is case sensitive (a is not the same as A) but 
you can ignore case by using the i switch

	grep -i 'lINUX' hello

>`Tips and tricks:`

To display line numbers:

	grep -n 'linux' hello 

To display lines that don't match the pattern:

	grep -v 'world' hello

To count no.of words,lines and character on a file use
	wc hello 
