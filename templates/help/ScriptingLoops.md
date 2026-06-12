<p>scripting loops</p>

<h2> Scripting loops </h2> </br> By  `Paul Cobbaut` and this free guide is available at `http://linux-training.be`</br>

<h2>test [ ]</h2>

<p>The <strong>test</strong> command can test whether something is true or false. Let&#39;s start by testing whether 10 is greater than 55.</p>

<pre>
[paul@RHEL4b ~]$ test 10 -gt 55 ; echo $?
1
[paul@RHEL4b ~]$</pre>

<p>The test command returns 1 if the test fails. And as you see in the next screenshot, test returns 0 when a test succeeds.</p>

<pre>
[paul@RHEL4b ~]$ test 56 -gt 55 ; echo $?
0
[paul@RHEL4b ~]$</pre>

<p>If you prefer true and false, then write the test like this.</p>

<pre>
[paul@RHEL4b ~]$ test 56 -gt 55 &amp;&amp; echo true || echo false
true
[paul@RHEL4b ~]$ test 6 -gt 55 &amp;&amp; echo true || echo false
false</pre>

<p>The test command can also be written as square brackets, the screenshot below is identical to the one above.</p>

<pre>
[paul@RHEL4b ~]$ [ 56 -gt 55 ] &amp;&amp; echo true || echo false
true
[paul@RHEL4b ~]$ [ 6 -gt 55 ] &amp;&amp; echo true || echo false
false</pre>

<p>Below are some example tests. Take a look at <strong>man test</strong> to see more options for tests.</p>

<pre>
[ -d foo ]             Does the directory foo exist ?
[ -e bar ]             Does the file bar exist ?
[ &#39;/etc&#39; = $PWD ]      Is the string /etc equal to the variable $PWD ?
[ $1 != &#39;secret&#39; ]     Is the first parameter different from secret ?
[ 55 -lt $bar ]        Is 55 less than the value of $bar ?
[ $foo -ge 1000 ]      Is the value of $foo greater or equal to 1000 ?
[ &quot;abc&quot; &lt; $bar ]       Does abc sort before the value of $bar ?
[ -f foo ]             Is foo a regular file ?
[ -r bar ]             Is bar a readable file ?
[ foo -nt bar ]        Is file foo newer than file bar ?
[ -o nounset ]         Is the shell option nounset set ?</pre>

<p>Tests can be combined with logical AND and OR.</p>

<pre>
paul@RHEL4b:~$ [ 66 -gt 55 -a 66 -lt 500 ] &amp;&amp; echo true || echo false
true
paul@RHEL4b:~$ [ 66 -gt 55 -a 660 -lt 500 ] &amp;&amp; echo true || echo false
false
paul@RHEL4b:~$ [ 66 -gt 55 -o 660 -lt 500 ] &amp;&amp; echo true || echo false
true</pre>

<h2>if then else</h2>

<p>The <strong>if then else</strong> construction is about choice. If a certain condition is met, then execute something, else execute something else. The example below tests whether a file exists, and if the file exists then a proper message is echoed.</p>

<pre>
#!/bin/bash

if [ -f isit.txt ]
then echo isit.txt exists!
else echo isit.txt not found!
fi</pre>

<p>If we name the above script &#39;choice&#39;, then it executes like this.</p>

<pre>
[paul@RHEL4a scripts]$ ./choice 
isit.txt not found!
[paul@RHEL4a scripts]$ touch isit.txt
[paul@RHEL4a scripts]$ ./choice 
isit.txt exists!
[paul@RHEL4a scripts]$</pre>

<h2>if then elif</h2>

<p>You can nest a new <strong>if</strong> inside an <strong>else</strong> with <strong>elif</strong>. This is a simple example.</p>

<pre>
#!/bin/bash
count=42
if [ $count -eq 42 ]
then
  echo &quot;42 is correct.&quot;
elif [ $count -gt 42 ]
then
  echo &quot;Too much.&quot;
else
  echo &quot;Not enough.&quot;
fi</pre>

<h2>for loop</h2>

<p>The example below shows the syntax of a classical <strong>for loop</strong> in bash.</p>

<pre>
for i in 1 2 4
do
   echo $i
done</pre>

<p>An example of a <strong>for loop</strong> combined with an embedded shell.</p>

<pre>
#!/bin/ksh
for counter in `seq 1 20`
do
   echo counting from 1 to 20, now at $counter
   sleep 1
done</pre>

<p>The same example as above can be written without the embedded shell using the bash <strong>{from..to}</strong> shorthand.</p>

<pre>
#!/bin/bash
for counter in {1..20}
do
   echo counting from 1 to 20, now at $counter
   sleep 1
done</pre>

<p>This <strong>for loop</strong> uses file globbing (from the shell expansion). Putting the instruction on the command line has identical functionality.</p>

<pre>
kahlan@solexp11$ ls
count.ksh  go.ksh
kahlan@solexp11$ for file in *.ksh ; do cp $file $file.backup ; done
kahlan@solexp11$ ls                                                 
count.ksh  count.ksh.backup  go.ksh  go.ksh.backup </pre>

<h2>while loop</h2>

<p>Below a simple example of a <strong>while loop</strong>.</p>

<pre>
i=100;
while [ $i -ge 0 ] ;
do
   echo Counting down, from 100 to 0, now at $i;
   let i--;
done</pre>

<p>Endless loops can be made with <strong>while true</strong> or <strong>while :</strong> , where the <strong>colon</strong> is the equivalent of <strong>no operation</strong> in the <strong>Korn</strong> and <strong>bash</strong> shells.</p>

<pre>
#!/bin/ksh
# endless loop
while :
do
 echo hello
 sleep 1
done</pre>

<h2>until loop</h2>

<p>Below a simple example of an <strong>until loop</strong>.</p>

<pre>
let i=100;
until [ $i -le 0 ] ;
do
   echo Counting down, from 100 to 1, now at $i;
   let i--;
done</pre>

<h2>practice: scripting tests and loops</h2>

<p>1. Write a script that uses a <strong>for</strong> loop to count from 3 to 7.</p>

<p>2. Write a script that uses a <strong>for</strong> loop to count from 1 to 17000.</p>

<p>3. Write a script that uses a <strong>while</strong> loop to count from 3 to 7.</p>

<p>4. Write a script that uses an <strong>until</strong> loop to count down from 8 to 4.</p>

<p>5. Write a script that counts the number of files ending in <strong>.txt</strong> in the current directory.</p>

<p>6. Wrap an <strong>if</strong> statement around the script so it is also correct when there are zero files ending in <strong>.txt</strong>.</p>

<h2>solution: scripting tests and loops</h2>

<p>1. Write a script that uses a <strong>for</strong> loop to count from 3 to 7.</p>

<pre>
#!/bin/bash

for i in 3 4 5 6 7
do
 echo Counting from 3 to 7, now at $i
done</pre>

<p>2. Write a script that uses a <strong>for</strong> loop to count from 1 to 17000.</p>

<pre>
#!/bin/bash

for i in `seq 1 17000`
do
 echo Counting from 1 to 17000, now at $i
done</pre>

<p>3. Write a script that uses a <strong>while</strong> loop to count from 3 to 7.</p>

<pre>
#!/bin/bash

i=3
while [ $i -le 7 ]
do
 echo Counting from 3 to 7, now at $i
 let i=i+1
done</pre>

<p>4. Write a script that uses an <strong>until</strong> loop to count down from 8 to 4.</p>

<pre>
#!/bin/bash

i=8
until [ $i -lt 4 ]
do
 echo Counting down from 8 to 4, now at $i
 let i=i-1
done</pre>

<p>5. Write a script that counts the number of files ending in <strong>.txt</strong> in the current directory.</p>

<pre>
#!/bin/bash

let i=0
for file in *.txt
do
	let i++
done
echo &quot;There are $i files ending in .txt&quot;
	</pre>

<p>6. Wrap an <strong>if</strong> statement around the script so it is also correct when there are zero files ending in <strong>.txt</strong>.</p>

<pre>
#!/bin/bash

ls *.txt &gt; /dev/null 2&gt;&amp;1
if [ $? -ne 0 ] 
then echo &quot;There are 0 files ending in .txt&quot;
else
	let i=0
	for file in *.txt
	do
		let i++
	done
	echo &quot;There are $i files ending in .txt&quot;
fi</pre>

<hr />
