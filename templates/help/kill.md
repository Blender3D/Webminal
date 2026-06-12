title: kill

Check again the running process list with 
	
	wm_ps

sleeping process is Gone! right? 

	kill 12345


>`Tips and tricks:`

Sometimes process won't die with simple kill command,in such cases 
scream `die!die!die!` while running kill command.(hehe..just kidding)
you have to use "-9" option.

	kill -9 12345 

start two process like 

	wm_sleep 30 &
	wm_sleep 30 &

checking with "ps",we can see we have two process named sleep,now type

	killall sleep 
