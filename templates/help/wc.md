title: wc

thus wc counts lines/words/bytes in a file. first field is 
no.of lines , second column is no.of words and third column 
denotes no.of bytes.

>`Tips and tricks:`

	wc -L hello 

to find the length of longest line in the file.Lets create a file 
with some contents with wm_echo.

	wm_echo -e "col1 col2 r1\ncol5 col6 r2\ncol3 col4 r3 " >> new.txt
	wm_echo -e "Hello\nlinux\nProgrammers paradise" >> linux.txt 


Okay,you have two files new.txt,linux.txt now,lets cut it ! :D 
	
	cut -f1 -d' ' new.txt

