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
