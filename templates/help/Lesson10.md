### Lesson10 - Background and Foreground Process 

So we know there is a first process named 'init' with pid. This is parent 
of all process in the system. And a process named 'bash' interacts with
Kernel on behalf of user requests or commands.



Now when I log in and type ps - I get below output:

	$ ps
	  PID TTY          TIME CMD
	 5254 pts/1    00:00:00 bash
	 5336 pts/1    00:00:00 ps

See this is different from our previous output. Everytime you login,new
parent bash is created.In case our *Manager* Bash job id is *5254*.
You know each command is a process, right? Lets create few process
for this session.


Type 

	sleep 5

Did it hang for 5 seconds and then provide you the bash prompt again?

The way, our bash creates child process is blocking call. It means,
run the child process and wait for it to complete and then return
to me again.

### Background process
So when we ran our child process (sleep), 'Bash' shell waited for
it to finish.  User request below commands:


	sleep 5

	sleep 2

Shell will run `sleep 5` first and wait for it to end. Then it
runs `sleep 2`. But what if job-2 in this case 'sleep 2' is 
more critical than first job. There is unnecessary delay of
5 seconds right? Shell has an option of running child process
on `background`  - that means it wont wait for child to finish
before accepting inputs from user.

We can put any child process in background by just appending
& character to it!

Lets try that:

	$ sleep 5 &
	[1] 5781
	$ sleep 2


Look, we can ran sleep 2 without hanging for 5 seconds! and the
number you see 5781 is the background child process id.
Its for our reference. How to verify its indeed the pid of child?
Simple just start child process in background and execute 'ps' command.

	$ sleep 5 &
	[1] 6095


	$ ps
	  PID TTY          TIME CMD
	 5254 pts/1    00:00:00 bash
	 6095 pts/1    00:00:00 sleep
	 6099 pts/1    00:00:00 ps

Our sleep 5 pid matches with ps output. Do we have better way to visualize
this? yes do. We have a command named 'pstree' which will tell you the
mapping between child and parent process!!

	Lets try again, note down your Bash shell pid (here its 5254)

	$ pstree 5254
	bash───pstree
	
It tells, we have Bash and one child process named 'pstree'.run our child,

	$ sleep 5 &
	[1] 6208

	$ pstree 5254
	bash─┬─pstree
	     └─sleep

Now it says, 'Bash' has two child named, pstree and out background process 'sleep'
pstree has an option to mention -p which displays pid next to process name. 

	$sleep 5 &
	[1] 6272

	$ pstree -p 5254
	bash(5254)─┬─pstree(6276)
        	   └─sleep(6272)

the pid we got while starting background process is same as what we got
from pstree output.

Lets say we have started 4 long running background jobs each runs for 145 seconds and
1 very long process for 3000 seconds.

	$sleep 45 &
	[1] 6393
	$sleep 45 &
	[2] 6397
	$sleep 45 &
	[3] 6401
	$sleep 45 &
	[4] 6406
	$ sleep 3000 &
	[5] 6557

	$pstree -p 5254
	bash(5254)─┬─pstree(6410)
           ├─sleep(6393)
           ├─sleep(6397)
           ├─sleep(6401)
           └─sleep(6406)
	   ├─sleep(6557)
   	
### List background jobs
pstree gives information about all jobs. We do not need pstree(6410), because are
intereste in only background jobs. How to view only those jobs. 
For this purpose, we have 'jobs' command will give output like:



	 jobs
	[1]   Running                 sleep 145 &
	[2]   Running                 sleep 145 &
	[3]-  Running                 sleep 145 &
	[4]+  Running                 sleep 145 &
	[5]+  Running                 sleep 3000 &

It lists only our background processes and its status. So far good right?

### Foreground process
Our process-[5] runs for 3000 seconds, it takes long time to complete. 
Background will take less CPU time compared to non-background process
.ie foreground process. So lets bring to foreground process.
type, fg <jobid> in our case, we need to bring background job-5.

	fg 5
	sleep 3000

Can you shell hanging now? wait..hanging is a wrong word to use. shell executing
sleep command now? :) Are you going to wait for 3000 seconds? aka 50 minutes?


### Switch between foreground to background

Lets admit it, by mistake without thinking, you (yes, its you :p )brought this 
background process to foreground, now you desperately want to put in on background again!!

Dont worry, Linux is so flexible we can do that too. Just press 'ctrl+z'.You get
output which says job is stopped. 

	^Z
	[5]+  Stopped                 sleep 3000

verify the status by checking output of jobs command.

	$jobs
	[5]+  Stopped                 sleep 3000

Its stopped, we can restart the process again in background  with 'bg <jobid>'

	$bg 5
	[5]+ sleep 3000 &

	$jobs
	[5]+  Running                 sleep 3000 &

Great, Today we learned about background and foreground process and how to move
between them. We will discuss in upcoming lessons.
