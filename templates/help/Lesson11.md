
###   Linux Process states 

Lets discuss about process states. `man ps` shows process can be any one of the following states

       D    Uninterruptible sleep (usually IO)
       R    Running or runnable (on run queue)
       S    Interruptible sleep (waiting for an event to complete)
       T    Stopped, either by a job control signal.
       X    dead (should never be seen)
       Z    Defunct ("zombie") process, terminated but not reaped by its parent.

We try to reproduce some of the above states to understand it better. We will begin by listing existing process and its states via command :

    ps -S
    PID TTY      STAT   TIME COMMAND
    16454 pts/4    Ss     0:03 bash
    28682 pts/4    R+     0:00 ps -S
    
As you can see STAT `S` stands for `Interruptible sleep`. Here, Our bash/shell is waiting for its child 28682 to complete. 28682 is in `running` state.
`s` - stands for session leader  and `+` tells it runs in foreground. 

Lets move a process to `Stopped` state.

    ps S
     PID TTY      STAT   TIME COMMAND
    16454 pts/4    Ss     0:05 bash
    29789 pts/4    R+     0:00 ps S

Now type `sleep 100` then and press `Ctrl+z`

     sleep 100
    ^Z
Now running ps shows the below output. Can you find out the meaning for `T` ?

     ps S
    PID TTY      STAT   TIME COMMAND
    16454 pts/4    Ss     0:05 bash
    29796 pts/4    T      0:00 sleep 10
    29846 pts/4    R+     0:00 ps S

Note this process is stopped its not terminated. That means, we can resume this 
stopped process. To prints upto 50000 on the screen we can perform

    seq 1 500000

After running it - I stopped it via `ctrl+z`

    19957
    19958
    19959
    19960
    ^Z
    
As you can its stopped at 19960.  Go ahead verify the process status via `ps S`
command. Now its resume this stopped process via `fg` command. You can see its continues to print from 19961 to 50000. What? too fast and can't see its started from 19961? thats pretty bad, you need to go for eye-checkup :-)

###Zombie process

Zombie is a terminated process but not reaped by its parent. When we say not reaped by its parent, we means "parent is yet to collect the exit status from child". Child is completed its execution ready with the exit status and waiting for parent to ask for it. This is tricky case to reproduce lets try:We have our session leader 2249

        ps
          PID TTY          TIME CMD
         2249 pts/1    00:00:00 bash
         2294 pts/1    00:00:00 ps

Lets create subshell:

     bash
     
Our subshell has pid 2498

        ps
          PID TTY          TIME CMD
         2249 pts/1    00:00:00 bash
         2498 pts/1    00:00:00 bash
         2540 pts/1    00:00:00 ps
What we going to do is create two more subshells and from there stop this subshell.
with command like :

    ( ( kill -STOP 2498 ) )
    [1]+  Stopped                 bash

Our subshell (2498) is stopped from its grandchild shell. So 2498 yet to collect the exit state of its child:

         ps S
          PID TTY      STAT   TIME COMMAND
         2249 pts/1    Ss     0:00 bash
         2498 pts/1    T      0:00 bash
         2547 pts/1    Z      0:00 [bash] <defunct>
         2551 pts/1    R+     0:00 ps S
         
As you can see `T` shows our process subshell is stopped without collecting exit status from its child. Apparently its child 2547 is in `Zombie` state `Z`

Note we only stopped the subshell, we can see them with command:

    $ jobs
    [1]+  Stopped                 bash
    
If you start this bash shell, it will collect the exit status from 2547 and reap its child. Thus the zombie process will disappear. Lets start our stopped shell:

     fg
    bash

Now lets check the status:

     ps S
    PID TTY      STAT   TIME COMMAND
    2249 pts/1    Ss     0:00 bash
    2498 pts/1    S      0:00 bash
    2561 pts/1    R+     0:00 ps S
    
See Zombie process is disappeared!

###Orphaned process
Orphaned is running process which with no parents. Parent is died without reaping the child (getting the exit status from child). These child process without parents are named `orphaned process`. These process are adopted by `init` which has pid `1`.
Lets try to create orphaned process similar to above steps:

         ps S
      PID TTY      STAT   TIME COMMAND
     2249 pts/1    Ss     0:01 bash
     3325 pts/1    R+     0:00 ps S

Create our subshell

    bash
     ps
      PID TTY          TIME CMD
     2249 pts/1    00:00:00 bash
     3329 pts/1    00:00:00 bash
     3371 pts/1    00:00:00 ps
     
From grandchild skill our sub-shell 3329 where as his child is still running.

     ( sleep 100 & ( kill -9 3329 ))
    Killed

Now verify that subshell with 3329 is indeed dead. 

     ps S
    PID TTY      STAT   TIME COMMAND
    2249 pts/1    Ss     0:01 bash
    3376 pts/1    S      0:00 sleep 100
    3381 pts/1    R+     0:00 ps S
    

Go ahead verify the parent of our orphaned child. 

     ps -o ppid 3376
    PPID
    1
    
Its our `init` process. It adopted it!

This marks end of this session. We used `kill` command without exploring further in our next session will discuss them. See you!
