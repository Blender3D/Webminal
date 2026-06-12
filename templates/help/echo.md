title: echo

Cool! the message is displayed on the screen.
Lets redirect the message to a new file instead 
of screen.

	echo "hello" > hello.txt 

To append  data you must use &gt;&gt; not just &gt;

	echo "linux" >> hello.txt 
	echo "world" >> hello.txt

Done.To view the file content ,do 

	cat hello.txt 

