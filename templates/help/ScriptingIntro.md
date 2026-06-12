<p> Bash Scripting </p>

<h2> Scripting introduction </h2> </br> By  `Paul Cobbaut` and this free guide is available at `http://linux-training.be`</br>

<p>Shells like <strong>bash</strong> and <strong>Korn</strong> have support for programming constructs that can be saved as <strong>scripts</strong>. These <strong>scripts</strong> in turn then become more <strong>shell</strong> commands. Many Linux commands are <strong>scripts</strong>. <strong>User profile scripts</strong> are run when a user logs on and <strong>init scripts</strong> are run when a <strong>daemon</strong> is stopped or started.</p>

<p>This means that system administrators also need basic knowledge of <strong>scripting</strong> to understand how their servers and their applications are started, updated, upgraded, patched, maintained, configured and removed, and also to understand how a user environment is built.</p>

<p>The goal of this chapter is to give you enough information to be able to read and understand scripts. Not to become a writer of complex scripts.</p>

<h2>hello world</h2>

<p>Just like in every programming course, we start with a simple <strong>hello_world</strong> script. The following script will output <strong>Hello World</strong>.</p>

<pre>
echo Hello World</pre>

<p>After creating this simple script in <strong>vi</strong> or with <strong>echo</strong>, you&#39;ll have to <strong>chmod +x hello_world</strong> to make it executable. And unless you add the scripts directory to your path, you&#39;ll have to type the path to the script for the shell to be able to find it.</p>

<pre>
[paul@RHEL4a ~]$ echo echo Hello World &gt; hello_world
[paul@RHEL4a ~]$ chmod +x hello_world 
[paul@RHEL4a ~]$ ./hello_world 
Hello World
[paul@RHEL4a ~]$</pre>

<h2>she-bang</h2>

<p>Let&#39;s expand our example a little further by putting <strong>#!/bin/bash</strong> on the first line of the script. The <strong>#!</strong> is called a <strong>she-bang</strong> (sometimes called <strong>sha-bang</strong>), where the <strong>she-bang</strong> is the first two characters of the script.</p>

<pre>
#!/bin/bash
echo Hello World</pre>

<p>You can never be sure which shell a user is running. A script that works flawlessly in <strong>bash</strong> might not work in <strong>ksh</strong>, <strong>csh</strong>, or <strong>dash</strong>. To instruct a shell to run your script in a certain shell, you can start your script with a <strong>she-bang</strong> followed by the shell it is supposed to run in. This script will run in a bash shell.</p>

<pre>
#!/bin/bash
echo -n hello
echo A bash subshell `echo -n hello`
		</pre>

<p>This script will run in a Korn shell (unless <strong>/bin/ksh</strong> is a hard link to <strong>/bin/bash</strong>). The <strong>/etc/shells</strong> file contains a list of shells on your system.</p>

<pre>
#!/bin/ksh
echo -n hello
echo a Korn subshell `echo -n hello`
		</pre>

<h2>comment</h2>

<p>Let&#39;s expand our example a little further by adding comment lines.</p>

<pre>
#!/bin/bash
#
# Hello World Script
#
echo Hello World</pre>

<h2>variables</h2>

<p>Here is a simple example of a variable inside a script.</p>

<pre>
#!/bin/bash
#
# simple variable in script
#
var1=4
echo var1 = $var1</pre>

<p>Scripts can contain variables, but since scripts are run in their own shell, the variables do not survive the end of the script.</p>

<pre>
[paul@RHEL4a ~]$ echo $var1

[paul@RHEL4a ~]$ ./vars
var1 = 4
[paul@RHEL4a ~]$ echo $var1

[paul@RHEL4a ~]$</pre>

<h2>sourcing a script</h2>

<p>Luckily, you can force a script to run in the same shell; this is called <strong>sourcing</strong> a script.</p>

<pre>
[paul@RHEL4a ~]$ source ./vars
var1 = 4
[paul@RHEL4a ~]$ echo $var1
4
[paul@RHEL4a ~]$ 
		</pre>

<p>The above is identical to the below.</p>

<pre>
[paul@RHEL4a ~]$ . ./vars
var1 = 4
[paul@RHEL4a ~]$ echo $var1
4
[paul@RHEL4a ~]$ 
		</pre>

<h2>troubleshooting a script</h2>

<p>Another way to run a script in a separate shell is by typing <strong>bash</strong> with the name of the script as a parameter.</p>

<pre>
paul@debian6~/test$ bash runme
42</pre>

<p>Expanding this to <strong>bash -x</strong> allows you to see the commands that the shell is executing (after shell expansion).</p>

<pre>
paul@debian6~/test$ bash -x runme
+ var4=42
+ echo 42
42
paul@debian6~/test$ cat runme
# the runme script
var4=42
echo $var4
paul@debian6~/test$</pre>

<p>Notice the absence of the commented (#) line, and the replacement of the variable before execution of <strong>echo</strong>.</p>

<h2>prevent setuid root spoofing</h2>

<p>Some user may try to perform <strong>setuid</strong> based script <strong>root spoofing</strong>. This is a rare but possible attack. To improve script security and to avoid interpreter spoofing, you need to add <strong>--</strong> after the <strong>#!/bin/bash</strong>, which disables further option processing so the shell will not accept any options.</p>

<pre>
#!/bin/bash -
or
#!/bin/bash --</pre>

<p>Any arguments after the <strong>--</strong> are treated as filenames and arguments. An argument of - is equivalent to --.</p>

<h2>practice: introduction to scripting</h2>

<p>0. Give each script a different name, keep them for later!</p>

<p>1. Write a script that outputs the name of a city.</p>

<p>2. Make sure the script runs in the bash shell.</p>

<p>3. Make sure the script runs in the Korn shell.</p>

<p>4. Create a script that defines two variables, and outputs their value.</p>

<p>5. The previous script does not influence your current shell (the variables do not exist outside of the script). Now run the script so that it influences your current shell.</p>

<p>6. Is there a shorter way to <strong>source</strong> the script ?</p>

<p>7. Comment your scripts so that you know what they are doing.</p>

<h2>solution: introduction to scripting</h2>

<p>0. Give each script a different name, keep them for later!</p>

<p>1. Write a script that outputs the name of a city.</p>

<pre>
$ echo &#39;echo Antwerp&#39; &gt; first.bash
$ chmod +x first.bash 
$ ./first.bash 
Antwerp</pre>

<p>2. Make sure the script runs in the bash shell.</p>

<pre>
$ cat first.bash
#!/bin/bash
echo Antwerp</pre>

<p>3. Make sure the script runs in the Korn shell.</p>

<pre>
$ cat first.bash
#!/bin/ksh
echo Antwerp</pre>

<p>Note that while first.bash will technically work as a Korn shell script, the name ending in .bash is confusing.</p>

<p>4. Create a script that defines two variables, and outputs their value.</p>

<pre>
$ cat second.bash
#!/bin/bash

var33=300
var42=400

echo $var33 $var42</pre>

<p>5. The previous script does not influence your current shell (the variables do not exist outside of the script). Now run the script so that it influences your current shell.</p>

<pre>
source second.bash</pre>

<p>6. Is there a shorter way to <strong>source</strong> the script ?</p>

<pre>
. ./second.bash</pre>

<p>7. Comment your scripts so that you know what they are doing.</p>

<pre>
$ cat second.bash
#!/bin/bash
# script to test variables and sourcing

# define two variables
var33=300
var42=400

# output the value of these variables
echo $var33 $var42</pre>

<hr />

