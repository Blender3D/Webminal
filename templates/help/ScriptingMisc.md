<p>More scripting</p>

<h2> More Scripting </h2> </br> By  `Paul Cobbaut` and this free guide is available at `http://linux-training.be`</br>

<h2>eval</h2>

<p><strong>eval</strong> reads arguments as input to the shell (the resulting commands are executed). This allows using the value of a variable as a variable.</p>

<pre>
paul@deb503:~/test42$ answer=42
paul@deb503:~/test42$ word=answer
paul@deb503:~/test42$ eval x=\$$word ; echo $x
42</pre>

<p>Both in <strong>bash</strong> and <strong>Korn</strong> the arguments can be quoted.</p>

<pre>
kahlan@solexp11$ answer=42
kahlan@solexp11$ word=answer
kahlan@solexp11$ eval &quot;y=\$$word&quot; ; echo $y
42</pre>

<p>Sometimes the <strong>eval</strong> is needed to have correct parsing of arguments. Consider this example where the <strong>date</strong> command receives one parameter <strong>1 week ago</strong>.</p>

<pre>
paul@debian6~$ date --date=&quot;1 week ago&quot;
Thu Mar  8 21:36:25 CET 2012
</pre>

<p>When we set this command in a variable, then executing that variable fails unless we use <strong>eval</strong>.</p>

<pre>
paul@debian6~$ lastweek=&#39;date --date=&quot;1 week ago&quot;&#39;
paul@debian6~$ $lastweek
date: extra operand `ago&quot;&#39;
Try `date --help&#39; for more information.
paul@debian6~$ eval $lastweek
Thu Mar  8 21:36:39 CET 2012
</pre>

<h2>(( ))</h2>

<p>The <strong>(( ))</strong> allows for evaluation of numerical expressions.</p>

<pre>
paul@deb503:~/test42$ (( 42 &gt; 33 )) &amp;&amp; echo true || echo false
true
paul@deb503:~/test42$ (( 42 &gt; 1201 )) &amp;&amp; echo true || echo false
false
paul@deb503:~/test42$ var42=42
paul@deb503:~/test42$ (( 42 == var42 )) &amp;&amp; echo true || echo false
true
paul@deb503:~/test42$ (( 42 == $var42 )) &amp;&amp; echo true || echo false
true
paul@deb503:~/test42$ var42=33
paul@deb503:~/test42$ (( 42 == var42 )) &amp;&amp; echo true || echo false
false</pre>

<h2>let</h2>

<p>The <strong>let</strong> built-in shell function instructs the shell to perform an evaluation of arithmetic expressions. It will return 0 unless the last arithmetic expression evaluates to 0.</p>

<pre>
[paul@RHEL4b ~]$ let x=&quot;3 + 4&quot; ; echo $x
7
[paul@RHEL4b ~]$ let x=&quot;10 + 100/10&quot; ; echo $x
20
[paul@RHEL4b ~]$ let x=&quot;10-2+100/10&quot; ; echo $x
18
[paul@RHEL4b ~]$ let x=&quot;10*2+100/10&quot; ; echo $x
30
		</pre>

<p>The <strong>shell</strong> can also convert between different bases.</p>

<pre>
[paul@RHEL4b ~]$ let x=&quot;0xFF&quot; ; echo $x
255
[paul@RHEL4b ~]$ let x=&quot;0xC0&quot; ; echo $x
192
[paul@RHEL4b ~]$ let x=&quot;0xA8&quot; ; echo $x
168
[paul@RHEL4b ~]$ let x=&quot;8#70&quot; ; echo $x
56
[paul@RHEL4b ~]$ let x=&quot;8#77&quot; ; echo $x
63
[paul@RHEL4b ~]$ let x=&quot;16#c0&quot; ; echo $x
192
		</pre>

<p>There is a difference between assigning a variable directly, or using <strong>let</strong> to evaluate the arithmetic expressions (even if it is just assigning a value).</p>

<pre>
kahlan@solexp11$ dec=15 ; oct=017 ; hex=0x0f 
kahlan@solexp11$ echo $dec $oct $hex 
15 017 0x0f 
kahlan@solexp11$ let dec=15 ; let oct=017 ; let hex=0x0f
kahlan@solexp11$ echo $dec $oct $hex
15 15 15</pre>

<h2>case</h2>

<p>You can sometimes simplify nested if statements with a <strong>case</strong> construct.</p>

<pre>
[paul@RHEL4b ~]$ ./help
What animal did you see ? lion
You better start running fast!
[paul@RHEL4b ~]$ ./help
What animal did you see ? dog
Don&#39;t worry, give it a cookie.
[paul@RHEL4b ~]$ cat help
#!/bin/bash
#
# Wild Animals Helpdesk Advice
#
echo -n &quot;What animal did you see ? &quot;
read animal
case $animal in
        &quot;lion&quot; | &quot;tiger&quot;)
                echo &quot;You better start running fast!&quot;
        ;;
        &quot;cat&quot;)
                echo &quot;Let that mouse go...&quot;
        ;;
        &quot;dog&quot;)
                echo &quot;Don&#39;t worry, give it a cookie.&quot;
        ;;
        &quot;chicken&quot; | &quot;goose&quot; | &quot;duck&quot; )
                echo &quot;Eggs for breakfast!&quot;
        ;;
        &quot;liger&quot;)
                echo &quot;Approach and say &#39;Ah you big fluffy kitty...&#39;.&quot;
        ;;
        &quot;babelfish&quot;)
                echo &quot;Did it fall out your ear ?&quot;
        ;;
        *)
                echo &quot;You discovered an unknown animal, name it!&quot;
        ;;
esac
[paul@RHEL4b ~]$ 			
		</pre>

<h2>shell functions</h2>

<p>Shell <strong>functions</strong> can be used to group commands in a logical way.</p>

<pre>
kahlan@solexp11$ cat funcs.ksh 
#!/bin/ksh
                                          
function greetings {
echo Hello World!
echo and hello to $USER to!
}

echo We will now call a function
greetings
echo The end</pre>

<p>This is sample output from this script with a <strong>function</strong>.</p>

<pre>
kahlan@solexp11$ ./funcs.ksh              
We will now call a function
Hello World!
and hello to kahlan to!
The end</pre>

<p>A shell function can also receive parameters.</p>

<pre>
kahlan@solexp11$ cat addfunc.ksh 
#!/bin/ksh

function plus {
let result=&quot;$1 + $2&quot;
echo  $1 + $2 = $result
}

plus 3 10
plus 20 13
plus 20 22</pre>

<p>This script produces the following output.</p>

<pre>
kahlan@solexp11$ ./addfunc.ksh 
3 + 10 = 13
20 + 13 = 33
20 + 22 = 42</pre>

<h2>practice : more scripting</h2>

<p>1. Write a script that asks for two numbers, and outputs the sum and product (as shown here).</p>

<pre>
Enter a number: 5
Enter another number: 2

Sum:       5 + 2 = 7
Product:   5 x 2 = 10
	</pre>

<p>2. Improve the previous script to test that the numbers are between 1 and 100, exit with an error if necessary.</p>

<p>3. Improve the previous script to congratulate the user if the sum equals the product.</p>

<p>4. Write a script with a case insensitive case statement, using the shopt nocasematch option. The nocasematch option is reset to the value it had before the scripts started.</p>


<h2>solution : more scripting</h2>

<p>1. Write a script that asks for two numbers, and outputs the sum and product (as shown here).</p>

<pre>
Enter a number: 5
Enter another number: 2

Sum:       5 + 2 = 7
Product:   5 x 2 = 10
	</pre>

<pre>
#!/bin/bash

echo -n &quot;Enter a number : &quot;
read n1

echo -n &quot;Enter another number : &quot;
read n2

let sum=&quot;$n1+$n2&quot;
let pro=&quot;$n1*$n2&quot;

echo -e &quot;Sum\t: $n1 + $n2 = $sum&quot; 
echo -e &quot;Product\t: $n1 * $n2 = $pro&quot;</pre>

<p>2. Improve the previous script to test that the numbers are between 1 and 100, exit with an error if necessary.</p>

<pre>
echo -n &quot;Enter a number between 1 and 100 : &quot;
read n1

if [ $n1 -lt 1 -o $n1 -gt 100 ]
then
       echo Wrong number... 
       exit 1
fi</pre>

<p>3. Improve the previous script to congratulate the user if the sum equals the product.</p>

<pre>
if [ $sum -eq $pro ] 
then echo Congratulations $sum == $pro
fi</pre>

<p>4. Write a script with a case insensitive case statement, using the shopt nocasematch option. The nocasematch option is reset to the value it had before the scripts started.</p>

<pre>
#!/bin/bash
#
# Wild Animals Case Insensitive Helpdesk Advice
#

if shopt -q nocasematch; then
  nocase=yes;
else
  nocase=no;
  shopt -s nocasematch;
fi

echo -n &quot;What animal did you see ? &quot;
read animal

case $animal in
		&quot;lion&quot; | &quot;tiger&quot;)
				echo &quot;You better start running fast!&quot;
		;;
		&quot;cat&quot;)
				echo &quot;Let that mouse go...&quot;
		;;
		&quot;dog&quot;)
				echo &quot;Don&#39;t worry, give it a cookie.&quot;
		;;
		&quot;chicken&quot; | &quot;goose&quot; | &quot;duck&quot; )
				echo &quot;Eggs for breakfast!&quot;
		;;
		&quot;liger&quot;)
				echo &quot;Approach and say &#39;Ah you big fluffy kitty.&#39;&quot;
		;;
		&quot;babelfish&quot;)
				echo &quot;Did it fall out your ear ?&quot;
		;;
		*)
				echo &quot;You discovered an unknown animal, name it!&quot;
		;;
esac

if [ nocase = yes ] ; then
        shopt -s nocasematch;
else
        shopt -u nocasematch;
fi</pre>


<hr />
