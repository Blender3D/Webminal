title: pidof

provides the process ID of a running program bash

	
>`Tips and tricks:`

	pidof -s bash

returns only one process id , instead of all process running as bash
You can adjust the pripority of your process by starting a process like,

	nice -n 19 sleep 30 &

