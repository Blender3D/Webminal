title: Lesson5 - Manipulate or parse file contents

### Lesson5 - Manipulate or parse file contents 

Lets try this widely used

	grep "linux" hello


----
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
title: wc

thus wc counts lines/words/bytes in a file. first field is 
no.of lines , second column is no.of words and third column 
denotes no.of bytes.

>`Tips and tricks:`

	wc -L hello 

to find the length of longest line in the file.Lets create a file 
with some contents with echo.

	echo -e "col1 col2 r1\ncol5 col6 r2\ncol3 col4 r3 " >> new.txt
	echo -e "Hello\nlinux\nProgrammers paradise" >> linux.txt 


Okay,you have two files new.txt,linux.txt now,lets cut it ! :D 
	
	cut -f1 -d' ' new.txt

title: cut

So it  extracted the first column from the file and to 
extract the third column

cut -f3 -d' ' new.txt

As you have noticed -f can be used to mention the column 
number and -d is used to specify the delimiter.now we have 
seen how to cut a file lets check out the another one , 

	paste hello new.txt 


title: paste

paste merges the lines of files

>`Tips and tricks:`

to paste one file at time,

	paste -s hello new.txt 

In order to sort a file content, we could use 

	sort new.txt
title: sort

File contents are sorted.Remember,we have two files
new.txt and linux.txt.lets compare them

	diff hello linux.txt

title: diff

File contents are sorted.Remember,we have two files
new.txt and linux.txt.lets compare them

	diff hello linux.txt


Compare files line by line. < denotes first file(hello) and >
denotes second file(linux.txt). you can compare three files 
with 

	diff3 hello new.txt linux.txt 


title: diff3

I'll let you to analyze the output :D we have 
reached end of lesson5. move on  to lesson6.
