title: Lesson1 - Basic commands to navigate directories 

### Lesson1 - Basic commands to navigate directories

Simply type 

    $ pwd


and press enter key and read on :)
title: pwd

Can you see the output similar to */home/yourname* ? cool,you have found your
current working directory.Congrats,You have joined exclusive club of
linux commandline users :)

As you realized typing


     pwd


will display your current working directory.Yeah,your home is a directory.
Now lets try to create a new directory.type the following  on the prompt 

    mkdir -v dir1

and press enter key.
title: mkdir

Did it say?

*`mkdir: created directory dir1`*

Wow,now you created a new  directory. Lets say you want to create more than 
one directory instead of invoking mkdir multiple(three) times-like.

	mkdir -v dir2
	mkdir -v dir2/dir3
	mkdir -v dir2/dir3/dir4
you can simply use 

	mkdir -vp dir2/dir3/dir4

"-p" option will create parent directories for "dir4" as needed.
In this case,it creates dir2,dir3 automatically.Now we have created 
4 directories.How to view them?

To view type 'ls' and press enter

	ls

title: ls

listed `dir1 dir2` as directory content right? Thats exactly what we wanted

	`dumb tutor: yes,the guy with blue-t-shirt,
		   Yeah, you ,why you look so confused?`
	`blue-t-shirt:I created 4 directories,
                   where is the missing dir3,dir4?`

Good question.They are created inside dir2 they won't be listed with 
simple command like `ls`.you need to use "complex" command to view them. Try this:

	ls -R 

really "complex" isn't it  :P ,btw -R stands for recursive.

Okay,we have created a new directories and listed them.Now lets 
move into a new directory.

	cd dir2





title: cd

cool,you have changed to dir2 Now confirm this
location by using previously learned `pwd`
command.To move into next directory dir3

	cd dir3
will place you under "dir3" directory.

>`Tips and tricks:` Typing 

        cd ..

will move to parent directory.i.e dir2.
Now type,

	cd -
will move you to previous working directory 
i.e dir3 Cool ,isn't it? and a simple

	cd 
will move to the your home directory.

That's it.You have successfully completed lesson1
Now to start next lesson.


