<p>scripting parameters</p>

<h2> Scripting parameters </h2>
By `Paul Cobbaut` and this free guide is available at `http://linux-training.be`

<h2><a name="idp7592448"></a>script parameters</h2>

<p>A <strong>bash</strong><a name="idp7593808"></a> shell script can have parameters. The numbering you see in the script below continues if you have more parameters. You also have special parameters containing the number of parameters, a string of all of them, and also the process id, and the last return code. The man page of <strong>bash</strong> has a full list.</p>

<pre>
#!/bin/bash
echo The first argument is $1
echo The second argument is $2
echo The third argument is $3

echo \$ $$  PID of the script
echo \# $#  count arguments
echo \? $?  last return code
echo \* $*  all the arguments</pre>

<p>Below is the output of the script above in action.</p>

<pre>
[paul@RHEL4a scripts]$ ./pars one two three
The first argument is one
The second argument is two
The third argument is three
$ 5610 PID of the script
# 3 count arguments
? 0 last return code
* one two three all the arguments
</pre>

<p>Once more the same script, but with only two parameters.</p>

<pre>
[paul@RHEL4a scripts]$ ./pars 1 2
The first argument is 1
The second argument is 2
The third argument is
$ 5612 PID of the script
# 2 count arguments
? 0 last return code
* 1 2 all the arguments
[paul@RHEL4a scripts]$
</pre>

<p>Here is another example, where we use <strong>$0</strong>. The <strong>$0</strong> parameter contains the name of the script.</p>

<pre>
paul@debian6~$ cat myname 
echo this script is called $0
paul@debian6~$ ./myname 
this script is called ./myname
paul@debian6~$ mv myname test42
paul@debian6~$ ./test42 
this script is called ./test42</pre>

<h2><a name="idp7602464"></a>shift through parameters</h2>

<p>The <strong>shift</strong><a name="idp7603872"></a> statement can parse all <strong>parameters</strong> one by one. This is a sample script.</p>

<pre>
kahlan@solexp11$ cat shift.ksh 
#!/bin/ksh                                
                                          
if [ &quot;$#&quot; == &quot;0&quot; ] 
 then
  echo You have to give at least one parameter.
  exit 1
fi

while (( $# ))
 do
  echo You gave me $1
  shift
 done
</pre>

<p>Below is some sample output of the script above.</p>

<pre>
kahlan@solexp11$ ./shift.ksh one  
You gave me one
kahlan@solexp11$ ./shift.ksh one two three 1201 &quot;33 42&quot;
You gave me one                           
You gave me two
You gave me three
You gave me 1201
You gave me 33 42
kahlan@solexp11$ ./shift.ksh                           
You have to give at least one parameter.
</pre>

<h2><a name="idp7608096"></a>runtime input</h2>

<p>You can ask the user for input with the <strong>read</strong><a name="idp7609520"></a> command in a script.</p>

<pre>
#!/bin/bash
echo -n Enter a number:
read number
		</pre>

<h2><a name="idp7611600"></a>sourcing a config file</h2>

<p>The <strong>source</strong><a name="idp7612992"></a> (as seen in the shell chapters) can be used to source a configuration file.</p>

<p>Below a sample configuration file for an application.</p>

<pre>
[paul@RHEL4a scripts]$ cat myApp.conf 
# The config file of myApp

# Enter the path here
myAppPath=/var/myApp

# Enter the number of quines here
quines=5
</pre>

<p>And her an application that uses this file.</p>

<pre>
[paul@RHEL4a scripts]$ cat myApp.bash 
#!/bin/bash
#
# Welcome to the myApp application
# 

. ./myApp.conf

echo There are $quines quines
</pre>

<p>The running application can use the values inside the sourced configuration file.</p>

<pre>
[paul@RHEL4a scripts]$ ./myApp.bash 
There are 5 quines
[paul@RHEL4a scripts]$</pre>

<h2><a name="idp7618192"></a>get script options with getopts</h2>

<p>The <strong>getopts</strong><a name="idp7619600"></a> function allows you to parse options given to a command. The following script allows for any combination of the options a, f and z.</p>

<pre>
kahlan@solexp11$ cat options.ksh 
#!/bin/ksh

while getopts &quot;:afz&quot; option;
do
 case $option in
  a)
   echo received -a
   ;;
  f)
   echo received -f
   ;;
  z)
   echo received -z
   ;;
  *)
   echo &quot;invalid option -$OPTARG&quot; 
   ;;
 esac
done
</pre>

<p>This is sample output from the script above. First we use correct options, then we enter twice an invalid option.</p>

<pre>
kahlan@solexp11$ ./options.ksh        
kahlan@solexp11$ ./options.ksh -af
received -a
received -f
kahlan@solexp11$ ./options.ksh -zfg
received -z
received -f
invalid option -g
kahlan@solexp11$ ./options.ksh -a -b -z
received -a
invalid option -b
received -z
</pre>

<p>You can also check for options that need an argument, as this example shows.</p>

<pre>
kahlan@solexp11$ cat argoptions.ksh 
#!/bin/ksh

while getopts &quot;:af:z&quot; option;
do
 case $option in
  a)
   echo received -a
   ;;
  f)
   echo received -f with $OPTARG
   ;;
  z)
   echo received -z
   ;;
  :)
   echo &quot;option -$OPTARG needs an argument&quot;
   ;;
  *)
   echo &quot;invalid option -$OPTARG&quot; 
   ;;
 esac
done</pre>

<p>This is sample output from the script above.</p>

<pre>
kahlan@solexp11$ ./argoptions.ksh -a -f hello -z
received -a
received -f with hello
received -z
kahlan@solexp11$ ./argoptions.ksh -zaf 42       
received -z
received -a
received -f with 42
kahlan@solexp11$ ./argoptions.ksh -zf   
received -z
option -f needs an argument</pre>

<h2><a name="idp7626288"></a>get shell options with shopt</h2>

<p>You can toggle the values of variables controlling optional shell behaviour with the <strong>shopt</strong><a name="idp7627760"></a> built-in shell command. The example below first verifies whether the cdspell option is set; it is not. The next shopt command sets the value, and the third shopt command verifies that the option really is set. You can now use minor spelling mistakes in the cd command. The man page of bash has a complete list of options.</p>

<pre>
paul@laika:~$ shopt -q cdspell ; echo $?
1
paul@laika:~$ shopt -s cdspell
paul@laika:~$ shopt -q cdspell ; echo $?
0
paul@laika:~$ cd /Etc
/etc</pre>

<h2><a name="idp7630240"></a>practice: parameters and options</h2>

<p>1. Write a script that receives four parameters, and outputs them in reverse order.</p>

<p>2. Write a script that receives two parameters (two filenames) and outputs whether those files exist.</p>


<h2><a name="idp7633312"></a>solution: parameters and options</h2>

<p>1. Write a script that receives four parameters, and outputs them in reverse order.</p>

<pre>
echo $4 $3 $2 $1</pre>

<p>2. Write a script that receives two parameters (two filenames) and outputs whether those files exist.</p>

<pre>
#!/bin/bash

if [ -f $1 ]
then echo $1 exists!
else echo $1 not found!
fi

if [ -f $2 ]
then echo $2 exists!
else echo $2 not found!
fi
	</pre>

<hr />
