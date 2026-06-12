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
	
