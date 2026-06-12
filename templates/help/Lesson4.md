title: Lesson4 - Basic process commands

### Lesson4 - Basic process commands 

On `Lesson1`,you learned about directories.
With `Lesson2`,you learned about files.
With `Lesson3`,you have learned about Copying,renaming,deleting files.
Now lets learn basic process-related commands.

Now check this widely used

	ps


----



title: ps

output is nothing but a snapshot of the currently running processes.
lets create  a new process.


	sleep 60 &


title: ps

can you see process id on screen?Now again do
	
	ps

you can see the sleeping process,now-right? lets see how to stop/kill 
this process replace 12345 will your sleeping process id,you got above

	kill 12345

title: kill

Check again the running process list with 
	
	ps

sleeping process is Gone! right? 

	kill 12345


>`Tips and tricks:`

Sometimes process won't die with simple kill command,in such cases 
scream `die!die!die!` while running kill command.(hehe..just kidding)
you have to use "-9" option.

	kill -9 12345 

start two process like 

	sleep 30 &
	sleep 30 &

checking with "ps",we can see we have two process named sleep,now type

	killall sleep 
title: killall

did it gave an output like 
	
	Terminated sleep 30

right?thus `killall` terminates processes by process name.


>`Tips and tricks:`

	killall -u webminal

This kills only processes owned by user "webminal"

	killall -w find

Wait  for  all  find process to die. killall checks once per second if 
any of the  killed  processes  still  exist  and  only returns if none are left.
Note that killall may wait forever if the signal was ignored, had no effect.
To find a process id (pid) of a process you can use,

	pidof bash

title: pidof

provides the process ID of a running program bash

	
>`Tips and tricks:`

	pidof -s bash

returns only one process id , instead of all process running as bash
You can adjust the pripority of your process by starting a process like,

	nice -n 19 sleep 30 &

title: nice

runs a program with modified scheduling priority.
Nice runs  a command  with an adjusted niceness, which affects process 
scheduling.Nicenesses  range  from -20 (most favorable scheduling) to 
19 (least favorable-the affected processes will run only when nothing 
else in the system wants to).Only root can increase the priority ,for
example setting process nice to -20 others can lower the priority of 
processes  they own.


how to adjust priority of currently running process with pid 12345?

	renice -n 19 12345
	
title: renice

changes priority of running processes.

	
	renice +1 3176
	3176: old priority 0, new priority 1

	renice +4 3176
	3176: old priority 1, new priority 4


Only root can increase the priority ,for example setting 
process nice to -20.others can lower the priority of processes 
they own.

note with renice command,Non super-users can not increase 
scheduling priorities of their own processes,even if they were the ones
that decreased the priorities in the first place.

To adjust priority for all process owned by a user "webminal",

	renice +1 -u webminal

to display running process ,you can also use 

	top
title: top

see it provides a dynamic real-time view of a running system.
spend sometime ,examining the output.To quit from the top command,press `q`.
To display commands in a tree like structure,type

	pstree 
title: pstree

display a tree of processes,to display pid ,
use -p option with pstree.

	pstree -p

below command will let us know how long it took to complete
a command.

	time ls -l



title: time


time gives statistics about the program it ran.

real - the elapsed real time between invocation and termination.

user - the user CPU time .

sys  - the  system CPU  time .


Thanks,you have completed `Lesson4`.
