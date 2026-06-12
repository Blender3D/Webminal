title: Lesson8 - System and user details

### Lesson8 - System and user details

Use below command to find out how long this system has
been up and running,

	uptime


----

title: uptime

uptime gives ,the current time, how long the system has been running, 
how  many  users  are currently  logged  on,  and the system load 
averages for the past 1, 5,and 15 minutes.

To know current date and time simply use

	date


title: date

Okay that display the current time of server running
webminal.org website.

To display details about currently logged users

	who

title: who

can you see other linux users ? :) 

	who -a 
print information about users who are currently logged into the system.
You can also use a single letter command,

	w

title: w

see it gives more detailed informatio than `who`. `w` can 
display  information  about the users currently on the machine,
and their processes.The header shows, in this order,the current
time,how long  the system  has  been running, how many users are
currently logged on, and the system load averages for the past 
1, 5, and 15 minutes.

Displays list of mounted file system

	mount
title: mount

provides list of mounted file systems.

>`Tips and tricks:`

to view only ext4 file system,

	mount -t ext4 
to display free disk space on mounted devices.

	df -h
title: df

-h switch makes the output more headable for humans.
so we found  df finds disk usage,but to find memory 
usage,we need to use

	free -m
title: free

displays the total amount of free and used physical and swap memory 
in the system, as well as the buffers  used  by  the  kernel.

	Wow!Cool,

	You have completed the lesson.
