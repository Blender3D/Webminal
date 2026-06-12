
[Source](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/sect-Configuring_the_Date_and_Time-date.html "Permalink to 2.2.&nbsp;Using the date Command")
#### This tutorial requires sudo access.
### &nbsp;Using the date Command

The `date` utility is available on all Linux systems and allows you to display and configure the current date and time. It is frequently used in scripts to display detailed information about the system clock in a custom format. 


###  1.&nbsp;Displaying the Current Date and Time

To display the current date and time, run the `date` command with no additional command line options: 
    
    
    date

This displays the day of the week followed by the current date, local time, abbreviated time zone, and year. 

By default, the `date` command displays the local time. To display the time in UTC, run the command with the `--utc` or `-u` command line option: 
    
    
    date --utc

You can also customize the format of the displayed information by providing the `+"_format_"` option on the command line: 
    
    
    date +"_format_"

Replace _format_ with one or more supported control sequences.



**&nbsp;Commonly Used Control Sequences**

| Control Sequence | Description                                                                                               |  
| ---------------- | --------------------------------------------------------------------------------------------------------- |  
| `%H`             | The hour in the _HH_ format (for example, `17`).                                                          |  
| `%M`             | The minute in the _MM_ format (for example, `30`).                                                        |  
| `%S`             | The second in the _SS_ format (for example, `24`).                                                        |  
| `%d`             | The day of the month in the _DD_ format (for example, `16`).                                              |  
| `%m`             | The month in the _MM_ format (for example, `09`).                                                         |  
| `%Y`             | The year in the _YYYY_ format (for example, `2013`).                                                      |  
| `%Z`             | The time zone abbreviation (for example, `CEST`).                                                         |  
| `%F`             | The full date in the _YYYY-MM-DD_ format (for example, `2013-09-16`). This option is equal to `%Y-%m-%d`. |  
| `%T`             | The full time in the _HH:MM:SS_ format (for example, 17:30:24). This option is equal to `%H:%M:%S`        |  



**Example:&nbsp;Displaying the Current Date and Time**

To display the current date and local time, type the following at a shell prompt: 
    
    
    ~]$date
    Mon Sep 16 17:30:24 CEST 2013

To display the current date and time in UTC, type the following at a shell prompt: 
    
    
    ~]$date --utc
    Mon Sep 16 15:30:34 UTC 2013

To customize the output of the `date` command, type: 
    
    
    ~]$date +"%Y-%m-%d %H:%M"
    2013-09-16 17:30

###  2.&nbsp;Changing the Current Time

To change the current time, run the `date` command with the `--set` or `-s` option as `root`: 
    
    
    date --set _HH:MM:SS_

Replace _HH_ with an hour, _MM_ with a minute, and _SS_ with a second, all typed in two-digit form. 

By default, the `date` command sets the system clock to the local time. To set the system clock in UTC, run the command with the `--utc` or `-u` command line option: 
    
    
    date --set _HH:MM:SS_ --utc



**Example:&nbsp;Changing the Current Time**

To change the current time to 11:26 p.m., run the following command as `root`: 
    
    
    ~]#date --set 23:26:00

###  3.&nbsp;Changing the Current Date

To change the current date, run the `date` command with the `--set` or `-s` option as `root`: 
    
    
    date --set _YYYY-MM-DD_

Replace _YYYY_ with a four-digit year, _MM_ with a two-digit month, and _DD_ with a two-digit day of the month. 

Note that changing the date without specifying the current time results in setting the time to 00:00:00. 



**Example:&nbsp;Changing the Current Date**

To change the current date to 2 June 2013 and keep the current time (11:26 p.m.), run the following command as `root`: 
    
    
    ~]#date --set 2013-06-02 23:26:00
