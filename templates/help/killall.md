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

