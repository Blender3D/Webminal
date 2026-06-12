
### Lesson9 -  Linux Process Basic commands

So far,we have seen about file related commands. Lets start with 
process-related command. 


What's a process? Wiki says "In computing, a process is an instance of a computer 
program that is being executed."

Lets talk about Linux process and its commands.

Can you find name of this system? Without looking bash prompt!?
Okay, I know you looked at the prompt and figured out its named
'fedori'. The proper way is to use 

	hostname

Go ahead and type it. Did it display 

`*fedori`* 

again?

Great!. You will be thinking "Wait a second, we wanted to discuss about 
process not about hostname of system."

Yes, I agree with you.  But again, how did you got the hostname?
Angry response will be *hostname*to be more precise */bin/hostname*
file.

Let me ask one more question, */bin/hostname* is a file or process? 
Of course its a file, always remember *In Linux everything is file*.

Its a special file, go ahead use the 'file' command you learned in
previous lessons.

	file /bin/hostname

It tell you something like 

`*/bin/hostname: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), 
dynamically linked (uses shared libs), for GNU/Linux 2.6.18, stripped`*

Its a ELF 32-bit executable file.  We ignore rest of the output.
So this /bin/hostname is not a process? Yes, its just an executable file.

When we say its executable file. /bin/hostname contains instructions
stored in a binary format. These instruction will be Kernel to do some
task or action.

Lets go ahead view those instructions /bin/hostname. Go ahead (never be 
afraid of Linux commandline)

	cat /bin/hostname

We got combination readable and unreadable characters. Somewhere within
those output, we are telling Kernel to read a file name '/etc/hosts'
and search for entry '127.0.0.1'.(which typically points to host machine
name) and display that content.

When we type an executable '/bin/hostname' on bash prompt, Its content
whatever you saw few lines above is loaded into RAM. Kernel follows those
instruction and takes action.

Finally, here's our definition of a Process.

	"Process is nothing but a  file-content which is residing in RAM"

Now lets revisit the Wiki :

	"In computing, a process is an instance of a computer program 
	that is being executed."

Here, `an instance of a computer program` means its residing in RAM
and `being executed` means Kernel follows its instruction.

I hope it makes some sense now.

Our 'fedori' has lot of Process executed by Users or by Kernel itself.
Each process has different states. Let's display some process currently,
residing at RAM.

To view them we can use command called 'ps'. Its similar to 'ls'
except that ls will show files on disk. 'ps' will show files on RAM

	ps

Gave us below output. Lets spend sometime on these.

	*`
 	 PID TTY          TIME CMD
	27447 pts/9    00:00:00 bash
	29731 pts/9    00:00:00 ps
	`*

###Understanding more about process:

It has 4 field PID,TTY,TIME,CMD

Lets start with easy one, 

CMD as name indicates, its tells what's the executable file
name currently residing in-memory. Its has unique id,which is called 'pid'.


PID - Each process has unique number assigned to it. Since Kernel needs to 
know 'who' is responsiable for these instruction. 

Why can't Kernel get this information from CMD itself? think about it.
We will discuss answer little later :)

TTY - Its terminal allocated to the process. If Kernel needs to ask something
or print something it will use this terminal for this process.

Finally,
TIME - It refers to how time CPU took to execute this process's instruction.
Its denoted in [dd-]hh:mm:ss format

We have two process with id 27447 and 29731.

###Parent process:

We saw 'hostname' was loaded into RAM and executed by Kernel. But who instructed
Kernel to find and load '/bin/hostname' into RAM in the first place?

There must be some process sitting already in RAM, waiting for you
to type characters and press 'Enter' key.  right? So only job of
this guy is to watch for any input (on TTY) and analyze and tell Kernel whether,
Kernel needs to take any action on the input request.

In real world, this looks like a 'Manager' job. Who wants other to do the task.Its like,
BOSS telling, "My work is wait for some work to arrive, when it arrives I'll assign to 
my employee/programmer to complete that task and report it to me" :P

In this case, 'Manager' is Bash shell. He assigns tasks to poor-hardworking Kernel. 
But wait, Kernel is kind of a 'Super Programmer'. HE decides whether to complete the task
or refuse the task depending on this own evaluation. ;)


Okay, so this 'Bash shell' is called parent process which instructed Kernel to load
hostname and execute it. Parent process has its own unique pid. Can we list the
parent process of a process? Yes, we can,that the whole point of above two paragraphs :P
Lets do that:

type:
	bash

Yes, its kind of 'secondary manager'. Now type 'ps' again

	*`
	  PID TTY          TIME CMD
	27447 pts/9    00:00:00 bash
	31400 pts/9    00:00:00 bash
	31414 pts/9    00:00:00 ps
	`*

Can you note the similarity? The process id '27447' remains the same.
He's your primary bash shell. He instructed Kernel to create another Bash shell.
It has id 31400 finally 31414 is the id of  'ps' the command used to print 
above output.

with ps we can pass an option '-o ppid' to get the parent id.Lets get the
parent of 31400 process.

	ps -o ppid 31400
	

	*`
	 PPID
	27447
	`*

Yeah,we got the expected output. If you are not convinced, you can also print
name like

	ps -o ppid,cmd 31400

	*`
	 PPID CMD
	27447 bash
	`*


We call 27447 as parent process and 31400 as child process. Also note
child pid is higher than parent pid. Most often, this will remain true.
Unless Kernel runs out of pid and starts re-using it.


Can we find the Parent of our primary Bash prompt (ie. grandparent of 31400)?

	ps -o ppid,cmd 27447

If you keep repeating this you will end up on '1'. which is the parent of all
process.Its called one and only `init` process. Do you know you created this 
process?, its the Kernel!!!

So our 'Manager' Bash job thinks he assigns job to 'Super Programmer' Kernel,
but that fact is 'Kernel is assigning job to Bash via proxy leader named `init` Cool :)

Okay, Its time for my dinner! We will talk more about process in next lessons.
