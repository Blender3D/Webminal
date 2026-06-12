## A Beginner's Python Tutorial - Table of Contents

*   [Acknowledgments](#Copyright "A Beginner's Python Tutorial/Copyright")
*   [Lesson 0: What is Python](#Whatis_Python "A Beginner's Python Tutorial/Installing Python")
*   [Lesson 1: Very Simple Programs](#Very_Simple_Programs "A Beginner's Python Tutorial/Very Simple Programs")
*   [Lesson 2: Variables, Scripts](#Variables,_Scripts "A Beginner's Python Tutorial/Variables, Scripts")
*   [Lesson 3: Loops, Conditionals](#Loops,_Conditionals "A Beginner's Python Tutorial/Loops, Conditionals")
*   [Lesson 4: Functions](#Functions "A Beginner's Python Tutorial/Functions")
*   [Lesson 5: Tuples, Lists, Dictionaries](#Tuples,_Lists,_Dictionaries "A Beginner's Python Tutorial/Tuples, Lists, Dictionaries")
*   [Lesson 6: for Loop](#for_loop "A Beginner's Python Tutorial/for Loop")
*   [Lesson 7: Classes](#Classes "A Beginner's Python Tutorial/Classes")
*   [Lesson 8: Importing Modules](#Importing_Modules "A Beginner's Python Tutorial/Importing Modules")
*   [Lesson 9: File I/O](#File_I/O "A Beginner's Python Tutorial/File I/O")
*   [Lesson 10: Exception Handling](#Exception_Handling "A Beginner's Python Tutorial/Exception Handling")
<a name="Copyright" />
## Acknowledgments

Content from the work **A Beginner's Python Tutorial** Copyright © 2011 Steven Thurlow, available at [https://github.com/stoive/pythontutorial](https://github.com/stoive/pythontutorial)and dual licensed under the Creative Commons Attribution 2.5 Australia license and MIT License was used on the creation of this book.

<a name="Whatis_Python" />
## What is Python?

Python is an [interpreted programming language](https://en.wikipedia.org/wiki/interpreted_programming_language "w:interpreted programming language") For those who don't know, a programming language is what you write down to tell a computer what to do. However, the computer doesn't read the language directly—there are hundreds of programming languages, and it couldn't understand them all. So, when someone writes a program, they will write it in their language of choice, and then  [compile](https://en.wikipedia.org/wiki/compiler "w:compiler") it—that is, turn it into lots of 0s and 1s, that the computer can easily and quickly understand. A Windows program that you buy is already compiled for Windows—if you opened the program file up, you'd just get a mass of weird characters and rectangles. Give it a go— open it up in nano . See what garbled mess you get.If you don't understand this, don't worry. Just skip it and move on.

But that Windows program is compiled for Windows—no other machine can run that program, unless it has Windows. What Python is, is a language which is never actually compiled in full—instead, an interpreter turns each line of code into 0s and 1s that your computer can understand. And it is done on the fly—it compiles the bits of the program you are using as you are using them. If you were to quit the program and come back another day, it would compile the bits you are using, as you are using them, again. Seems a waste of time? Maybe, but the fact is that when you come back another day, you might be using a Windows PC instead of a Mac. You might send the program to a friend, who uses another type of computer. Or you might post your program on the internet, where everyone using all different types of systems might download it. That is the wonder of an interpreted programming language—it is like a language that _everyone_ can understand.
<a name="Very_Simple_Programs" /> 
## Lesson 1: Very Simple Programs
<pre> 
Introduction
Invoking Python
Math in Python
Order of Operations
Comments, Please
</pre>


### Introduction

OK! here, we already installed Python, now what? Well, we program!

And it is that simple (at least for now!). Python makes it easy to run single lines of code—one-liner programs. Let's give it a go.

### Invoking Python

Run the program labelled  **python** .

<pre >$ python </pre>

Now, you are at python interpreter This is the place you will be spending most time in. Here you can simply mess around with single lines of code, which is what we are going to do.

Type the following line and press <kbd style="font-family: monospace, Courier;">Enter</kbd>. Don't type the `>>>` part, it will already be there. Also note that in Python 2 the parentheses are optional after `print`, but in Python 3.0 they are required.

`Code Example 1 - Hello, world!`
Go ahead and type 
<pre> >>> print "Hello, world! </pre>

What happened? You just created a program, that prints the words 'Hello, world'. The interpreter that you are in immediately compiles whatever you have typed in. This is useful for testing things, e.g., defining a few variables, and then testing to see if a certain line will work. That will come in a later lesson though.

### Math in Python

Now try the following examples. I've given explanations in parentheses.

`Code Example 2 – Maths`



<pre> >>> 1 + 1
2

>>> 20 + 80
100

>>> 18294 + 449566
467860
(These are additions.)

>>> 6 - 5
1
(Subtraction)

>>> 2 * 5
10
(Multiplication)

>>> 5 ** 2
25
(Exponentials; e.g., this one is 5 squared)

>>> print ("1 + 2 is an addition")
1 + 2 is an addition
(The print statement, which writes something onscreen. Notice that 1 + 2 is left unevaluated.)

>>> print ("One kilobyte is 2^10 bytes, or", 2 ** 10, "bytes.")
One kilobyte is 2^10 bytes, or 1024 bytes.
(You can print sums and variables in a sentence.
        The commas separating each section are a way of
        separating clearly different things that you are printing.)

>>> 21 / 3
7

>>> 23 / 3
7
(Division; note that Python ignores remainders/decimals.)

>>> 23.0 / 3.0
7.666666666666667
(This time, since the numbers are decimals themselves, the answer
        will be a decimal.)

>>> 23 % 3
2

>>> 49 % 10
9
(The remainder from a division)
</pre>

As you see, there is the code, then the result of that code. I then explain them in brackets. These are the basic commands of Python, and what they do. Here is a table to clarify them.

<table border="1" ><caption>Table 1 – Python operators</caption>

<tbody>

<tr>

<th>Command</th>

<th>Name</th>

<th>Example</th>

<th>Output</th>

</tr>

<tr>

<td>+</td>

<td>Addition</td>

<td>4 + 5</td>

<td>9</td>

</tr>

<tr>

<td>-</td>

<td>Subtraction</td>

<td>8 - 5</td>

<td>3</td>

</tr>

<tr>

<td>*</td>

<td>Multiplication</td>

<td>4 * 5</td>

<td>20</td>

</tr>

<tr>

<td>/</td>

<td>Division</td>

<td>19 / 3</td>

<td>6</td>

</tr>

<tr>

<td>%</td>

<td>Remainder ([modulo](https://en.wikipedia.org/wiki/modulous "w:modulous"))</td>

<td>19 % 3</td>

<td>1</td>

</tr>

<tr>

<td>**</td>

<td>Exponent</td>

<td>2 ** 4</td>

<td>16</td>

</tr>

</tbody>

</table>

Remember that thing called [order of operations](https://en.wikipedia.org/wiki/order_of_operations "w:order of operations") that they taught in maths? Well, it applies in Python, too. Here it is, if you need reminding:

	1.  parentheses ()
	2.  exponents **
	3.  multiplication *, division /, and remainder %
	4.  addition + and subtraction -

### Order of Operations

Here are some examples that you might want to try, if you're rusty on this:

`Code Example 3 – Order of operations`

<pre >>>> 1 + 2 * 3
7
>>> (1 + 2) * 3
9
</pre>

In the first example, the computer calculates 2 * 3 first, then adds 1 to it. This is because multiplication has the higher priority (at 3) and addition is below that (at a lowly 4).

In the second example, the computer calculates 1 + 2 first, then multiplies it by 3\. This is because parentheses (brackets, like the ones that are surrounding this interluding text ;) ) have the higher priority (at 1), and addition comes in later than that.

Also remember that the math is calculated from left to right, _unless_ you put in parentheses. The innermost parentheses are calculated first. Watch these examples:

`Code Example 4 – Parentheses`

<pre>>>> 4 - 40 - 3
-39
>>> 4 - (40 - 3)
-33
</pre>

In the first example, 4 - 40 is calculated,then - 3 is done.

In the second example, 40 - 3 is calculated, then it is subtracted from 4.

### Comments, Please

The final thing you'll need to know to move on to multi-line programs is the [comment](https://en.wikipedia.org/wiki/comment_(computer_programming) "w:comment (computer programming)"). You should always add comments to code to show others who might be reading your code what you've done and why. Type the following (and yes, the output is shown):

`Code Example 5 – Comments`

</dl>

<pre >>>> #I am a comment. Fear my wrath!

>>>
</pre>

A comment is a piece of code that is not run. In Python, you make something a comment by putting a hash (#) in front of it. A hash comments everything after it in the line, and nothing before it. So you could type this:

`Code Example 6 – Comment examples`

<pre >>>> print ("food is very nice") #eat me
food is very nice
(A normal output, without the smutty comment,
thank you very much)

>>># print "food is very nice"

(Nothing happens, because the code was after a comment)

>>> print "food is very nice" eat me

(You'll get a fairly harmless error message,
because you didn't put your comment after a hash)
</pre>

Comments are important for adding necessary information for another programmer to read, but not the computer; for example, an explanation of a section of code, saying what it does, or what is wrong with it. You can also comment out bits of code if you don't want them to compile, but can't delete them because you might need them later.

<a name="Variables,_Scripts"></a>

# Lesson 2: Variables, Scripts

<pre>
Introduction
Editing in Nano
Executing our code
Variables
Strings
</pre>

### Introduction

Well, we can make one-liner programs. So what? You want to send programs to other people, so that they can use them, without knowing how to write them. Still in python interpreter? you can exit the python interpreter by typing 'quit()' or exit()

### Editing in Nano

Writing programs in Python to a file is _very_ easy. Python programs are simply text documents—you can open them up in nano or vim text editor, and have a look at them, just like that. So, go and open nano.


`Code Example 1 – mary.py`

<pre >$ nano  </pre> and Type the following:
<pre>
print("Mary had a little lamb,")
print("its fleece was white as snow;")
print("and everywhere that Mary went"),
print("her lamb was sure to go.")
</pre>

Keep this exactly the same, down to where the commas are placed. Type 'ctrl+O' and type <tt style="font-family: monospace, Courier;">mary.py</tt>— for the prompt 'File Name to Write'  

### Executing our code

Its time to execute our file. type 'python mary.py' output will look like

`Code Example 2 mary.py output`

<pre >Mary had a little lamb,
its fleece was white as snow;
and everywhere that Mary went her lamb was sure to go.
</pre>

There are a couple of things to notice here:

First of all, the comment wasn't shown. That is good, because remember—comments aren't compiled. (Try compiling it after removing the #—it comes out messy.)

Second, is that the 3rd and 4th line got joined. This is because there is a comma just outside the inverted commas that surround the text. In the <tt style="font-family: monospace, Courier;">print</tt> command, this stops the program from starting a new line on the screen when showing text. (This might not work with Python 3.0 version onwards. Check your installed version).
### Variables

Now let's start introducing variables. Variables store a value, that can be looked at or changed at a later time. Let's make a program that uses variables. Open up IDLE and click 'File > New Window'. A new window now appears, and it is easy to type in programs. Type the following (or just copy and paste—just read very carefully, and compare the code to the output that the program will make):


`Code Example 3 – Variables`


<pre>
#Variables demonstrated
print ("This program is a demo of variables.")
v = 1
print("The value of v is now", v)
v = v + 1
print("v now equals itself plus one, making it worth", v)
v = 51
print("v can store any numerical value, to be used elsewhere.")
print("For example, in a sentence. v is now worth", v)
print("v times 5 equals", v * 5)
print("But v still only remains", v)
print("To make v five times bigger, you would have to type v = v * 5")
v = v * 5
print("There you go, now v equals", v, "and not", v / 5)
</pre>

</div>

Note that if you just want to modify a variable's value with respect to itself, there are shortcuts. These are called [augmented assignment operators](https://en.wikipedia.org/wiki/augmented_assignment "w:augmented assignment"):

<table ><caption>Table 1 – Augmented operators</caption>

<tbody>

<tr>

<th>Standard form</th>

<th>Augmented</th>

</tr>

<tr>

<td>v = v + 5</td>

<td>v += 5</td>

</tr>

<tr>

<td>v = v - 5</td>

<td>v -= 5</td>

</tr>

<tr>

<td>v = v * 5</td>

<td>v *= 5</td>

</tr>

<tr>

<td>v = v / 5</td>

<td>v /= 5</td>

</tr>

</tbody>

</table>

### Strings

As you can see, variables store values, for use at a later time. You can change them at any time. You can put in more than numbers, though. Variables can hold things like text. A variable that holds text is called a string. Try this program:


`Code Example 4 – Strings`

<pre>
#Giving variables text, and adding text.
word1 = "Good"
word2 = "morning"
word3 = "to you too!"
print(word1, word2)
sentence = word1 + " " + word2 + " " + word3
print(sentence)
</pre>

The output will be:

`Code Example 5 – String output`

<pre >Good morning
Good morning to you too!
</pre>

As you see, the variables above were holding text. Variable names can also be longer than one letter—here, we had word1, word2, and word3\. As you can also see, strings can be added together to make longer words or sentences. However, spaces aren't added in between the words—hence me putting in the " " things (there is one space between those).


<a name="Loops,_Conditionals" />

# Loops, Conditionals

<pre>
Introduction
The while loop
Boolean Expressions (Boolean... what?!?)
Conditional Statements
'else' and 'elif' - When it Ain't True
Indentation
</pre>

### Introduction

(Our final lesson before we get into interacting with human input. Can't wait, can you?)

Just imagine you needed a program to do something 20 times. What would you do? You could copy and paste the code 20 times, and have a virtually unreadable program. Or, you could tell the computer to repeat a bit of code between point A and point B, until the time comes that you need it to stop. Such a thing is called a loop.

### while loop

The following are examples of a type of loop, called the <tt style="font-family: monospace, Courier;">while</tt> loop:

`Code Example 1 – The while loop`

<pre>
a = 0
while a < 10:
    a = a + 1
    print(a)
</pre>



How does this program work? Let's go through it in English (this is called [pseudocode](https://en.wikipedia.org/wiki/pseudocode "w:pseudocode")):

`Code Example 2 – Plain-language whileloop`


<pre >'a' now equals 0
As long as 'a' is less than 10, do the following:
    Make 'a' one larger than what it already is.
    print on-screen what 'a' is now worth.
</pre>

What does this do? Let's go through what the computer would be 'thinking' when it is in the while loop:



`Code Example 3 – while loop process`

<pre >#JUST GLANCE OVER THIS QUICKLY
#(It looks fancy, but is really simple.)
Is 'a' less than 10? YES (it's 0)
Make 'a' one larger (now 1)
print on-screen what 'a' is (1)

Is 'a' less than 10? YES (it's 1)
Make 'a' one larger (now 2)
print on-screen what 'a' is (2)

Is 'a' less than 10? YES (it's 2)
Make 'a' one larger (now 3)
print on-screen what 'a' is (3)

Is 'a' less than 10? YES (it's 3)
Make 'a' one larger (now 4)
print on-screen what 'a' is (4)

Is 'a' less than 10? YES (it's 4)
Make 'a' one larger (now 5)
print on-screen what 'a' is (5)

Is 'a' less than 10? YES (it's 5)
Make 'a' one larger (now 6)
print on-screen what 'a' is (6)

Is 'a' less than 10? YES (it's 6)
Make 'a' one larger (now 7)
print on-screen what 'a' is (7)

Is 'a' less than 10? YES (are you still here?)
Make 'a' one larger (now 8)
print on-screen what 'a' is (8)

Is 'a' less than 10? YES (it's 8)
Make 'a' one larger (now 9)
print on-screen what 'a' is (9)

Is 'a' less than 10? YES (it's 9)
Make 'a' one larger (now 10)
print on-screen what 'a' is (10)

Is 'a' less than 10? NO (it's 10, therefore isn't less than 10)
Don't do the loop
There's no code left to do, so the program ends.
</pre>

So in short, try to think of it that way when you write while loops. This is how you write them, by the way:



`Code Example 4 – while loop form`

<pre >while {condition that the loop continues}:
    {what to do in the loop}
    {have it indented, usually four spaces}
{the code here is not looped}
{because it isn't indented}
</pre>

An example:

`Code Example 5 – while loop example`



<pre >#EXAMPLE
#Type this in and see what it does.
x = 10
while x != 0:
    print(x)
    x = x - 1
    print("Wow, we've counted x down, and now it equals", x)
print "And now the loop has ended."
</pre>

</div>



### Boolean Expressions (Boolean... what?!?)

What do you type in the area marked {conditions that the loop continues}? The answer is a boolean expression.

What? A forgotten concept for the non-math people here. Never mind, boolean expression just means a question that can be answered with a TRUE or FALSE response. For example, if you wanted to say your age is the same as the person next to you, you would type:

My age == the age of the person next to me

And the statement would be TRUE. If you were younger than the person opposite, you'd say:

My age < the age of the person opposite me

And the statement would be TRUE. If, however, you were to say the following, and the person opposite of you was younger than you:

My age < the age of the person opposite me

The statement would be FALSE - the truth is that it is the other way around. This is how a loop thinks - if the expression is true, keep looping. If it is false, don't loop. With this in mind, lets have a look at the operators (symbols that represent an action) that are involved in boolean expressions:

<table border="1" ><caption>Table 1 - Boolean operators</caption>

<tbody>

<tr>

<th>Expression</th>

<th>Function</th>

</tr>

<tr>

<td><</td>

<td>less than</td>

</tr>

<tr>

<td><=</td>

<td>less than or equal to</td>

</tr>

<tr>

<td>></td>

<td>greater than</td>

</tr>

<tr>

<td>>=</td>

<td>greater than or equal to</td>

</tr>

<tr>

<td>!=</td>

<td>not equal to</td>

</tr>

<tr>

<td><></td>

<td>not equal to (alternate, != preferred)</td>

</tr>

<tr>

<td>==</td>

<td>equal to</td>

</tr>

</tbody>

</table>

Dont get '=' and '==' mixed up - the '=' operator makes what is on the left equal to what is on the right. the '==' operator says whether the thing on the left is the same as what is on the right, and returns true or false.
### Conditional Statements

OK! We've (hopefully) covered 'while' loops. Now let's look at something a little different - conditionals.

Conditionals are where a section of code is only run if certain conditions are met. This is similar to the 'while' loop you just wrote, which only runs when x doesn't equal 0\. However, Conditionals are only run once. The most common conditional in any program language, is the 'if' statement. Here is how it works:



`Code Example 6 - if statement and example`



<pre >'''
if {conditions to be met}:
    {do this}
    {and this}
    {and this}
{but this happens regardless}
{because it isn't indented}
'''

#EXAMPLE 1
y = 1
if y == 1:
    print ("y still equals 1, I was just checking")

#EXAMPLE 2
print ("We will show the even numbers up to 20")
n = 1
while n <= 20:
    n = n + 1
    if n % 2 == 0:    
           print(n)
print("there, done.")
</pre>

</div>

Example 2 there looks tricky. But all we have done is run an 'if' statement every time the 'while' loop runs. Remember that the % just means the remainder from a division - just checking that there is nothing left over if the number is divided by two - showing it is even. If it is even, it prints what 'n' is.

### 'else' and 'elif' - When it Ain't True

There are many ways you can use the 'if' statement, to deal with situations where your boolean expression ends up FALSE. They are 'else' and 'elif'.

'else' simply tells the computer what to do if the conditions of 'if' aren't met. For example, read the following:



`Code Example 7 - the else statement`

<pre >
a = 1
if a > 5:
    print("This shouldn't happen.")
else:
    print("This should happen.")
</pre>



'a' is not greater than five, therefore what is under 'else' is done.

'elif' is just a shortened way of saying 'else if'. When the 'if' statement fails to be true, 'elif' will do what is under it IF the conditions are met. For example:



`Code Example 8 - The elif statement`



<pre>
z = 4
if z > 70:
    print("Something is very wrong")
elif z < 7:
    print("This is normal")
</pre>



The 'if' statement, along with 'else' and 'elif' follow this form:



`Code Example 9 - the complete if syntax`

<pre >if {conditions}:
    {run this code}
elif {conditions}:
    {run this code}
elif {conditions}:
    {run this code}
else:
    {run this code}

#You can have as many or as few elif statements as you need
#anywhere from zero to the sky.
#You can have at most one else statement
#and only after all other ifs and elifs.
</pre>

One of the most important points to remember is that you MUST have a colon (:) at the end of every line with an 'if', 'elif', 'else' or 'while' in it. I forgot that, and as a result a stack of people got stumped at this lesson (sorry ;)).

### Indentation

One other point is that the code to be executed if the conditions are met, MUST BE INDENTED. That means that if you want to loop the next five lines with a 'while' loop, you must put a set number of spaces at the beginning of each of the next five lines. This is good programming practice in any language, but python requires that you do it. Here is an example of both of the above points:



`Code Example 10 - Indentation`

<pre >
a = 10
while a > 0:
    print(a)
    if a > 5:
        print("Big number!")
    elif a % 2 != 0:
        print("This is an odd number")
        print("It isn't greater than five, either")
    else:
        print("this number isn't greater than 5")
        print("nor is it odd")
        print("feeling special?")
    a = a - 1
    print("we just made 'a' one less than what it was!")
    print("and unless a is not greater than 0, we'll do the loop again.")
print("well, it seems as if 'a' is now no bigger than 0!")
print("the loop is now over, and without furthur ado, so is this program!")
</pre>



Notice the three levels of indents there:

Each line in the first level starts with no spaces. It is the main program, and will always execute. Each line in the second level starts with four spaces. When there is an 'if' or loop on the first level, everything on the second level after that will be looped/'ifed', until a new line starts back on the first level again. Each line in the third level starts with eight spaces. When there is an 'if' or loop on the second level, everything on the third level after that will be looped/'ifed', until a new line starts back on the second level again. This goes on infinitely, until the person writing the program has an internal brain explosion, and cannot understand anything he/she has written. There is another loop, called the 'for' loop, but we will cover that in a later lesson, after we have learnt about lists.



<a name="Functions" />

# Functions

<pre>

Introduction
Using a function
Parameters and Returned Values - Communicating with Functions
A Calculator Program
Define Your Own Functions
Passing Parameters to Functions
A Final Program
Tricky Ways You Can Pass Parameters

</pre>

### Introduction

Last lesson I said that we would delve into purposefull programming. That involves user input, and user input requires a thing called functions.

What are functions? Well, in effect, functions are little self-contained programs that perform a specific task, which you can incorporate into your own, larger programs. After you have created a function, you can use it at any time, in any place. This saves you the time and effort of having to retell the computer what to do every time it does a common task, for example getting the user to type something in.

### Using a function

Python has lots of pre-made functions, that you can use right now, simply by 'calling' them. 'Calling' a function involves you giving a function input, and it will return a value (like a variable would) as output. Don't understand? Here is the general form that calling a function takes:


`Code Example 1 - How to call a function`

<pre >function_name(parameters)</pre>


See? Easy.

function_name identifies which function it is you want to use (you'd figure...). For example, the function raw_input, which will be the first function that we will use. Parameters are the values you pass to the function to tell it what it should do, and how to do it.. for example, if a function multiplied any given number by five, the stuff in parameters tells the function which number it should multiply by five. Put the number 70 into parameters, and the function will do 70×5.

### Parameters and Returned Values - Communicating with Functions

Well, that's all well and good that the program can multiply a number by five, but what does it have to show for it? A warm fuzzy feeling? Your program needs to see the results of what happened, to see what 70 x 5 is, or to see if there is a problem somewhere (like you gave it a letter instead of a number). So how does a function show what it does?

Well, in effect, when a computer runs a function, it doesn't actually see the function name, but the result of what the function did. Variables do the exact same thing - the computer doesn't see the variable name, it sees the value that the variable holds. Lets call this program that multiplied any number by five, multiply(). You put the number you want multiplied in the brackets. So if you typed this:


`Code Example 2 - Using a function`


<pre >
a = multiply(70)
</pre>

The computer would actually see this:


`Code Example 3 - What the computer sees`


<pre >a = 350
</pre>



Note: don't bother typing in this code - multiply() isn't a real function, unless you create it.

The function ran itself, then returned a number to the main program, based on what parameters it was given.

Now let's try this with a real function, and see what it does. The function is called input, and asks the user to type in something. It then turns it into a string of text. Try the code below:

`Code Example 4 - Using raw_input`


<pre ># this line makes 'a' equal to whatever you type in
a = raw_input("Type in something, and it will be repeated on screen:")
# this line prints what 'a' is now worth
print a
</pre>

Say in the above program, you typed in 'hello' when it asked you to type something in. To the computer, this program would look like this:

`Code Example 5 - What the computer sees`


<pre >a = "hello"
print "hello"
</pre>



Remember, a variable is just a stored value. To the computer, the variable 'a' doesn't look like 'a' - it looks like the value that is stored inside it. Functions are similar - to the main program (that is, the program that is running the function), they look like the value of what they give in return of running.


###  A Calculator Program

Let's write another program, one that will act as a calculator. This time it will do something more adventurous than what we have done before. There will be a menu that will ask you whether you want to multiply two numbers together, add two numbers together, divide one number by another, or subtract one number from another. The only problem is that theraw_input function returns what you type in as a _string_, whereas we want the _number_ 1, not the letter 1 (and yes, in Python, there is a difference).

Luckily, somebody wrote the function input, which returns what you typed in to the main program - but crucially, as a number, not a letter. If you type an _integer_ (a whole number), what comes out of input is an integer. And if you put that integer into a variable, the variable will be an integer-type variable, which means you can perform addition, subtraction and other mathematical operations on it.

Now, let's design this calculator properly. We want a menu that is returned to every time you finish adding, subtracting, etc. In other words, to loop (HINT!!!) while (BIG HINT!!!) you tell it the program should still run.

We want it to perform an option in the menu associated with the number you enter. That involves you typing in a number (a.k.a. input) and an if loop.

Let's write it out in understandable English first:



`Code Example 6 - human-language example`

<pre >START PROGRAM
print opening message

while we let the program run, do this:
    #Print what options you have
    print Option 1 - add
    print Option 2 - subtract
    print Option 3 - multiply
    print Option 4 - divide
    print Option 5 - quit program

    ask the person what option they want and look for an integer
    if it is option 1:
        ask for first number
        ask for second number
        add them together
        display the result on screen
    if it is option 2:
        ask for first number
        ask for second number
        subtract one from the other
        display the result on screen
    if it is option 3:
        ask for first number
        ask for second number
        multiply them
        display the result on screen
    if it is option 4:
        ask for first number
        ask for second number
        divide the first by the second
        display the result on screen
    if it is option 5:
        tell the loop to stop
Display a goodbye message on screen
END PROGRAM
</pre>

Let's put this in something that Python can understand:



`Code Example 7 - Python version of menu`



<pre >
#calculator program

#This variable tells the loop whether it should loop or not.
# 1 means loop. Anything else means don't loop.

loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #Display the available options
    print ("Welcome to calculator.py")

    print ("your options are:")
    print (" ")
    print ("1) Addition")
    print ("2) Subtraction")

    print ("3) Multiplication")

    print ("4) Division")
    print ("5) Quit calculator.py")
    print (" ")

    choice = int(input("Choose your option: "))
    if choice == 1:
        add1 = int(input("Add this: "))
        add2 = int(input("to this: "))
        print (add1, "+", add2, "=", add1 + add2)
    elif choice == 2:
        sub2 = int(input("Subtract this: "))
        sub1 = int(input("from this: "))
        print (sub1, "-", sub2, "=", sub1 - sub2)
    elif choice == 3:
        mul1 = int(input("Multiply this: "))
        mul2 = int(input("with this: "))
        print (mul1, "*", mul2, "=", mul1 * mul2)
    elif choice == 4:
        div1 = int(input("Divide this: "))
        div2 = int(input("by this: "))
        print (div1, "/", div2, "=", div1 / div2)
    elif choice == 5:
        loop = 0
	
print ("Thank you for using calculator.py!")
</pre>



Wow! That is an impressive program! Paste it into Python file, save it as 'calculator.py' and run it. Play around with it - try all options, entering in integers (numbers without decimal points), and numbers with stuff after the decimal point (known in programming as a floating point). Try typing in text, and see how the program chucks a minor fit, and stops running (That can be dealt with, using error handling, which we can address later.)

### Define Your Own Functions

Well, it is all well and good that you can use other people's functions, but what if you want to write your own functions, to save time, and maybe use them in other programs? This is where the 'def' operator comes in. (An operator is just something that tells python what to do, e.g. the '+' operator tells python to add things, the 'if' operator tells python to do something if conditions are met.)

This is how the 'def' operator works:



`Code Example 8 - The def operator`

<pre >def function_name(parameter_1, parameter_2):
    {this is the code in the function}
    {more code}
    {more code}
    return {value to return to the main program}
{this code isn't in the function}
{because it isn't indented}
#remember to put a colon ":" at the end
#of the line that starts with 'def'
</pre>

function_name is the name of the function. You write the code that is in the function below that line, and have it indented. (We will worry about parameter_1 and parameter_2 later, for now imagine there is nothing between the parentheses.

Functions run completely independent of the main program. Remember when I said that when the computer comes to a function, it doesn't see the function, but a value, that the function returns? Here's the quote:

"To the computer, the variable 'a' doesn't look like 'a' - it looks like the value that is stored inside it. Functions are similar - to the main program (that is, the program that is running the function), they look like the value of what they give in return of running."

A function is like a miniature program that some parameters are given to - it then runs itself, and then returns a value. Your main program sees only the returned value. If that function flew to the moon and back, and then at the end had:



`Code Example 9 - return`



<pre >return "Hello"
</pre>



then all your program would see is the string "hello", where the name of the function was. It would have no idea what else the program did.

Because it is a separate program, a function doesn't see any of the variables that are in your main program, and your main program doesn't see any of the variables that are in a function. For example, here is a function that prints the words "hello" onscreen, and then returns the number '1234' to the main program:



`Code Example 10 - using return`



<pre ># Below is the function
def hello():
    print ("hello")
    return 1234

# And here is the function being used
>>>hello()
</pre>

</div>

Think about the last line of code above. What did it do? Type in the program (you can skip the comments), and see what it does. The output looks like this:



`Code Example 11 - the output`

<pre >hello
1234
</pre>

So what happened?

when 'def hello()' was run, a function called 'hello' was created When the line 'hello()' was run, the function 'hello' was executed (The code inside it was run) The function 'hello' printed "hello" onscreen, then returned the number '1234' back to the main program The main program now sees the line as 'print 1234' and as a result, printed '1234' That accounts for everything that happened. remember, that the main program had NO IDEA that the words "hello" were printed onscreen. All it saw was '1234', and printed that onscreen.

### Passing Parameters to Functions

There is one more thing we will cover in this (monsterously huge) lesson - passing parameters to a function. Think back to how we defined functions:



`Code Example 12 - Defining functions with parameters`

<pre >def function_name(parameter_1,parameter_2):
    {this is the code in the function}
    {more code}
    {more code}
    return {value (e.g. text or number) to return to the main program}
</pre>

Where parameter_1 and parameter_2 are (between the parentheses), you put the names of variables that you want to put the parameters into. Put as many as you need, just have them seperated by commas. When you run a function, the first value you put inside the parentheses would go into the variable where parameter_1 is. The second one (after the first comma) would go to the variable where parameter_2 is. This goes on for however many parameters there are in the function (from zero, to the sky) For example:



`Code Example 13 - how parameters work`



<pre >
def funny_function(first_word, second_word, third_word):
    print "The word created is: " + first_word + second_word + third_word
    return first_word + second_word + third_word
</pre>

</div>

When you run the function above, you would type in something like this: `funny_function("meat", "eater", "man")`. The first value (that is, "meat") would be put into the variable called first_word. The second value inside the brackets (that is, "eater") would be put into the variable called second_word, and so on. This is how values are passed from the main program to functions - inside the parentheses, after the function name.

### A Final Program

Think back to that calculator program. Did it look a bit messy to you? I think it did, so lets re-write it, with functions.

To design - First we will define all the functions we are going to use with the 'def' operator (still remember what an operator is ;) ). Then we will have the main program, with all that messy code replaced with nice, neat functions. This will make it so much easier to look at again in the future.


de Example 14 - Calculator program`

<pre ># calculator program

# NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
# Here we will define our functions
# this prints the main menu, and prompts for a choice
def menu():
    #print what options you have
    print "Welcome to calculator.py"
    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit calculator.py"
    print " "
    return input ("Choose your option: ")
    
# this adds two numbers given
def add(a,b):
    print a, "+", b, "=", a + b
    
# this subtracts two numbers given
def sub(a,b):
    print b, "-", a, "=", b - a
    
# this multiplies two numbers given
def mul(a,b):
    print a, "*", b, "=", a * b
    
# this divides two numbers given
def div(a,b):
    print a, "/", b, "=", a / b
    
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "),input("to this: "))
    elif choice == 2:
        sub(input("Subtract this: "),input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "),input("by this: "))
    elif choice == 4:
        div(input("Divide this: "),input("by this: "))
    elif choice == 5:
        loop = 0

print "Thank you for using calculator.py!"

# NOW THE PROGRAM REALLY FINISHES
</pre>

</div>

The initial program had 34 lines of code. The new one actually had 35 lines of code! It is a little longer, but if you look at it the right way, it is actually simpler.

You defined all your functions at the top. This really isn't part of your main program - they are just lots of little programs, that you will call upon later. You could even re-use these in another program if you needed them, and didn't want to tell the computer how to add and subtract again.

If you look at the main part of the program (between the line 'loop = 1' and 'print "Thank you for..."'), it is only 15 lines of code. That means that if you wanted to write this program differently, you would only have to write 15 or so lines, as opposed to the 34 lines you would normally have to without functions.

### Tricky Ways You Can Pass Parameters

Finally, as a bit of an interlude, I will explain what the line `add(input("Add this: "), input("to this: "))` means.

I wanted to fit everything onto one line, with as few variables as possible. Remember what functions look like to the main program? Whatever value they return. If the numbers you passed to the add() function were 2 and 30, the main program would see this:



`Code Example 15 - The results of fancy parameter work`



<pre >        add(2, 30)
</pre>


The add program would then run, adding 2 and 30, then printing the result. The add program has no 'return' operator - it doesn't return anything to the main program. It simply adds two numbers and prints them onscreen, and the main program doesn't see anything of it.

Instead of `(input("Add this: "), input("to this: "))` as the parameters for the add program, you could have variables. For example,


`Code Example 16 - variables as parameters`

<pre >num1 = 45
num2 = 7
add(num1, num2)
</pre>

</div>

For the above, remember that the function you are passing the variables to cannot change the variables themselves - they are simply used as values. You could even put the values straight into the function:

`Code Example 17 - the end result`

<pre >add(45, 7)
</pre>



This is because the only thing the function sees are the values that are passed on as parameters. Those values are put into the variables that are mentioned when 'add' is defined (the line 'def add(a,b)' ). The function then uses those parameters to do its job.

In short:

*   the only thing functions see of the main program is the parameters that are passed to it
*   the only thing the main program sees of functions is the returned value that it passes back

<a name="Tuples,_Lists,_Dictionaries" />

## Tuples, Lists, Dictionaries

<pre>
Introduction
The Solution - Lists, Tuples, and Dictionaries
Tuples
Lists
Dictionaries

</pre>

### Introduction

Your brain still hurting from the last lesson? Never worry, this one will require a little less thought. We're going back to something simple - variables - but a little more in depth.

Think about it - variables store one bit of information. They may regurgitate (just not on the carpet...) that information at any point, and their bit of information can be changed at any time. Variables are great at what they do - storing a piece of information that may change over time.

But what if you need to store a long list of information, which doesn't change over time? Say, for example, the names of the months of the year. Or maybe a long list of information, that does change over time? Say, for example, the names of all your cats. You might get new cats, some may die, some may become your dinner (we should trade recipes!). What about a phone book? For that you need to do a bit of referencing - you would have a list of names, and attached to each of those names, a phone number. How would you do that?

### The Solution - Lists, Tuples, and Dictionaries

For these three problems, Python uses three different solutions - lists, tuples, and dictionaries:

-   `Lists` are what they seem - a list of values. Each one of them is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, etc. You can remove values from the list, and add new values to the end. Example: Your many cats' names.

-   `Tuples` are just like lists, but you can't change their values. The values that you give it first up, are the values that you are stuck with for the rest of the program. Again, each value is numbered starting from zero, for easy reference. Example: the names of the months of the year.

-   `Dictionaries` are similar to what their name suggests - a dictionary. In a dictionary, you have an 'index' of words, and for each of them a definition. In Python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. (Each key must be unique, though!) You can add, remove, and modify the values in dictionaries. Example: telephone book.


### Tuples

Tuples are pretty easy to make. You give your tuple a name, then after that the list of values it will carry. For example, the months of the year:


`Code Example 1 - creating a tuple`

<pre >months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')
</pre>



Note that the '\' thingy at the end of the first line carries over that line of code to the next line. It is useful way of making big lines more readable. Technically, you don't have to put those parentheses there (the '(' and ')' thingies), but it stops Python from getting things confused. You may have spaces after the commas if you feel it necessary - it doesn't really matter. Python then organises those values in a handy, numbered index - starting from zero, in the order that you entered them in. It would be organised like this:

<table border="1" style="line-height: 22.4px;" width="25%"><caption>Table 1 - tuple indicies</caption>

<tbody>

<tr>

<th>Index</th>

<th>Value</th>

</tr>

<tr>

<td>0</td>

<td>January</td>

</tr>

<tr>

<td>1</td>

<td>February</td>

</tr>

<tr>

<td>2</td>

<td>March</td>

</tr>

<tr>

<td>3</td>

<td>April</td>

</tr>

<tr>

<td>4</td>

<td>May</td>

</tr>

<tr>

<td>5</td>

<td>June</td>

</tr>

<tr>

<td>6</td>

<td>July</td>

</tr>

<tr>

<td>7</td>

<td>August</td>

</tr>

<tr>

<td>8</td>

<td>September</td>

</tr>

<tr>

<td>9</td>

<td>October</td>

</tr>

<tr>

<td>10</td>

<td>November</td>

</tr>

<tr>

<td>11</td>

<td>December</td>

</tr>

</tbody>

</table>

And that is tuples! Really easy...

### Lists

Lists are extremely similar to tuples. Lists are modifiable (or 'mutable', as a programmer may say), so their values can be changed. Most of the time we use lists, not tuples, because we want to easily change the values of things if we need to.

Lists are defined very similarly to tuples. Say you have FIVE cats, called Tom, Snappy, Kitty, Jessie and Chester. To put them in a list, you would do this:



`Code Example 2 - Creating a list`


<pre >cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
</pre>


As you see, the code is exactly the same as a tuple, EXCEPT that all the values are put between square brackets, not parentheses. Again, you don't have to have spaces after the comma.

You recall values from lists exactly the same as you do with tuples. For example, to print the name of your 3rd cat you would do this:



`Code Example 3 - Recalling items from a list`



<pre >print cats[2]
</pre>



You can also recall a range of examples, like above, for example - `cats[0:2]` would recall your 1st and 3rd cats.

Where lists come into their own is how they can be modified. To add a value to a list, you use the `append()` function. Let's say you got a new cat called Catherine. To add her to the list you'd do this:



`Code Example 4 - Adding items to a list`



<pre >cats.append('Catherine')
</pre>



That's a little weird, isn't it? I'll explain. That function is in a funny spot - after a period (the '.' kind of period, not otherwise), after the list name. You'll get to see those things more in a later lesson. For the meanwhile, this is the form of the function that adds a new value to a list:



`Code Example 5 - Using the append function`



<pre >#add a new value to the end of a list:
list_name.append(value_to_add)

#e.g. to add the number 5038 to the list 'numbers':
numbers.append(5038)
</pre>



Clears things up? Good!

Now to a sad situation - Snappy was shot by a neighbour, and eaten for their dinner (good on 'em!). You need to remove him (or her) from the list. Removing that sorry cat is an easy task, thankfully, so you have to wallow in sadness for as short a time as possible:



`Code Example 6 - Deleting an item`



<pre >#Remove your 2nd cat, Snappy. Woe is you.
del cats[1]
</pre>



You've just removed the 2nd cat in your list - poor old Snappy.

And with that morbid message, lets move on to...

### Dictionaries

Ok, so there is more to life than the names of your cats. You need to call your sister, mother, son, the fruit man, and anyone else who needs to know that their favourite cat is dead. For that you need a telephone book.

Now, the lists we've used above aren't really suitable for a telephone book. You need to know a number based on someone's name - not the other way around, like what we did with the cats. In the examples of months and cats, we gave the computer a number, and it gave us a name. This time we want to give the computer a name, and it give us a number. For this we need dictionaries.

So how do we make a dictionary? Put away your binding equipment, it isn't that advanced.

Remember, dictionaries have keys, and values. In a phone book, you have people's names, then their numbers. See a similarity?

When you initially create a dictionary, it is very much like making a tuple or list. Tuples have ( and ) things, lists have [ and ] things. Guess what! dictionaries have { and } things - curly braces. Here is an example below, showing a dictionary with four phone numbers in it:



`Code Example 7 - Creating a dictionary`



<pre >#Make the phone book:
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}
</pre>



The program would then print Lewis Lame's number onscreen. Notice how instead of identifying the value by a number, like in the cats and months examples, we identify the value, using another value - in this case the person's name.

Ok, you've created a new phone book. Now you want to add new numbers to the book. What do you do? A very simple line of code:



`Code Example 8 - Adding entries to a dictionary`



<pre >#Add the person 'Gingerbread Man' to the phonebook:

phonebook['Gingerbread Man'] = 1234567

# Didn't think I would give you
# my real number now, would I?
</pre>



All that line is saying is that there is a person called Gingerbread Man in the phone book, and his number is 1234567\. In other words - the key is 'Gingerbread Man', and the value is 1234567.

You delete entries in a dictionary just like in a list. Let's say Andrew Parson is your neighbour, and shot your cat. You never want to talk to him again, and therefore don't need his number. Just like in a list, you'd do this:



`Code Example 9 - Removing entries from a dictionary`



<pre >del phonebook['Andrew Parson']
</pre>



Again, very easy. the 'del' operator deletes any function, variable, or entry in a list or dictionary (An entry in a dictionary is just a variable with a number or text string as a name. This comes in handy later on.)

Remember that append function that we used with the list? Well, there are quite a few of those that can be used with dictionaries. Below, I will write you a program, and it will incorporate some of those functions in. It will have comments along the way explaining what it does.

Type this program into Python  (you can skip the comments). Experiment as much as you like with it. Type it where you see the lines beginning with >>>



`Code Example 10 - Functions of dictionaries`



<pre >#A few examples of a dictionary

#First we define the dictionary
#it will have nothing in it this time
ages = {}

#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use the function has_key() - 
#This function takes this form:
#function_name.has_key(key-name)
#It returns TRUE
#if the dictionary has key-name in it
#but returns FALSE if it doesn't.
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if ages.has_key('Sue'):
    print "Sue is in the dictionary. She is", \
ages['Sue'], "years old"

else:
    print "Sue is not in the dictionary"

#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print "The following people are in the dictionary:"
print ages.keys()

#You could use this function to
#put all the key names in a list:
keys = ages.keys()

#You can also get a list
#of all the values in a dictionary.
#You use the values() function:
print "People are aged the following:", \
ages.values()

#Put it in a list:
values = ages.values()

#You can sort lists, with the sort() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print keys
keys.sort()
print keys

print values
values.sort()
print values

#You can find the number of entries
#with the len() function:
print "The dictionary has", \
len(ages), "entries in it"</pre>

<a name="for_loop" />
## For Loop

<pre>
Introduction
The 'for' Loop
Making a Menu Function
Our First 'Game'
Making the Game Better
</pre>


### Introduction

Well, in the first lesson about loops, I said I would put off teaching you the for loop, until we had reached lists. Well, here it is!

### The 'for' Loop

Basically, the for loop does something for every value in a list. The way it is set out is a little confusing, but otherwise is very basic. Here is an example of it in code:


`Code Example 1 - The for Loop`


<pre ># Example 'for' loop
# First, create a list to loop through:
newList = [45, 'eat me', 90210, "The day has come, the walrus said, \
to speak of many things", -67]

# create the loop:
# Goes through newList, and seqentially puts each bit of information
# into the variable value, and runs the loop
for value <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in newList:
    print(value)
</pre>



As you see, when the loop executes, it runs through all of the values in the list mentioned after 'in'. It then puts them into value, and executes through the loop, each time with value being worth something different. Let's see it a again, in a classic cheerleading call that we all know:


`Code Example 2 - A for loop example`


<pre ># cheerleading program
word = raw_input("Who do you go for? ")

for letter <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in word:
    call = "Gimme a " + letter + "!"
    print(call)
    print(letter + "!")
print("What does that spell?")
print(word + "!")
</pre>


A couple of things you've just learnt:

As you see, strings (remember - strings are lines of text) are just lists with lots of characters. The program went through each of the letters (or values) in word, and it printed them onscreen. And that is all there is to the for loop.

### Making a Menu Function

Now to the business end of the lesson. Lets start writing programs. So far we have learnt variables, lists, loops, and functions. That is pretty much all we need for quite a bit of programming. So let's set ourselves a task.


`Code Example 3 - A menu function`


<pre ># THE MENU FUNCTION
# The program asks for a string with all the menu options in it,
# and a text string asking a question.
# make sure every menu entry is unique.

def menu(list, question):
    for entry <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in </span> list:
        print(1 + list.index(entry),)
        print (") " + entry)

    return input(question) - 1

# def menu(list, question): is telling the function to
# ask for two bits of information:
# A list of all the menu entries,
# and the question it will ask when all the options have been printed

# for entry in list: is pretty much saying;
#'for every entry in the list, do the following:'

# print list.index(entry) + 1 uses the .index() function to find
# where in the list the entry is in. print function then prints it
# it adds 1 to make the numbers more intelligable.

# print ") " + entry prints a bracket, and then the entry name

# after the for loop is finished, input(question) - 1 asks the question,
# and returns the value to the main program (minus 1, to turn it back to
# the number the computer will understand).
</pre>


That wasn't very difficult, was it? the actual program only took up five lines - this is the wonder of how much we have learnt so far! All my comments take up sixteen lines - more than three times the program length. It is a good idea to comment your programs extensively. Remember that if you are going to be publishin gyour code open-source, there are going to be a lot of people checking out the code that you have written. We'll see the function we just wrote in our first example program.

### Our First 'Game'

What will our first example program be? How about a (very) simple text adventure game? Sounds like fun! It will only encompass one room of a house, and will be extremely simple. There will be five things, and a door. In one of the five things, is a key to the door. You need to find the key, then open the door. I will give a plain-english version first, then do it in python:



`Code Example 4 - Plain-english version of code`

<pre >#Plain-english version of our 'game'

Tell the computer about our menu function

Print a welcoming message, showing a description of the room.
We will give the player six things to look at: plant, painting,\
 vase, lampshade, shoe, and the door

Tell the computer that the door is locked
Tell the computer where the key is

present a menu, telling you what things you can 'operate':
    It will give you the six options
    It will ask the question "what will you look at?"

if the user wanted to look at:
    plant:
        If the key is here, give the player the key
        otherwise, tell them it isn't here
    painting:
        same as above
    etc.
    door:
        If the player has the key, let them open the door
        Otherwise, tell them to look harder

Give the player a well done message, for completing the game.
</pre>

From this, we can write a real program. Ready? Here it is (skip typing the comments):


`Code Example 5 - Text Adventure Game`


<pre >#TEXT ADVENTURE GAME

#the menu function:
def menu(list, question):
    for entry <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in list:
        print(1 + list.index(entry),)
        print(") " + entry)

    return input(question) - 1

#Give the computer some basic information about the room:
items = ["plant","painting","vase","lampshade","shoe","door"]

#The key is in the vase (or entry number 2 in the list above):
keylocation = 2

#You haven't found the key:
keyfound = 0

loop = 1

#Give some introductary text:
print("Last night you went to sleep in the comfort of your own home.")

print("Now, you find yourself locked in a room. You don't know how")
print("you got there, or what time it is. In the room you can see")
print(len(items), "things:")
for x <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in items:
    print(x)
print("")
print("The door is locked. Could there be a key somewhere?")
#Get your menu working, and the program running until you find the key:
while loop == 1:
    choice = menu(items,"What do you want to inspect? ")
    if choice == 0:
        if choice == keylocation:
            print("You found a small key in the plant.")

            print("")
            keyfound = 1
        else:
            print("You found nothing in the plant.")
            print("")
    elif choice == 1:
        if choice == keylocation:
            print("You found a small key behind the painting.")
            print("")

            keyfound = 1
        else:
            print("You found nothing behind the painting.")
            print("")
    elif choice == 2:
        if choice == keylocation:
            print("You found a small key in the vase.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the vase.")

            print ""
    elif choice == 3:
        if choice == keylocation:
            print("You found a small key in the lampshade.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the lampshade.")
            print("")

    elif choice == 4:
        if choice == keylocation:
            print("You found a small key in the shoe.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the shoe.")
            print("")
    elif choice == 5:
        if keyfound == 1:
            loop = 0
            print("You put in the key, turn it, and hear a click")

            print("")
        else:
            print("The door is locked, you need to find a key.")
            print("")

# Remember that a backslash continues
# the code on the next line

print "Light floods into the room as \
you open the door to your freedom."
</pre>



Well, a very simple, but fun, game. Don't get daunted by the amount of code there, 53 of the lines are just the 'if' statements, which is the easiest thing to read there. (Once you comprehend all the indentation, you'll be able to make your own game, and you can make it as simple [or as complex] as you like.)

### Making the Game Better

The first question you should ask is "does this program work?". The answer here is yes. Then you should ask "does this program work well?" - not quite. The menu() function is great - it reduces a lot of typing. The 'while' loop that we have, however, is a little messy - four levels of indents, for a simple program. We can do better!

Now, this will become much MUCH more straightforward when we introduce classes. But that will have to wait. Until then, let's make a function that reduces our mess. It we will pass two things to it - the menu choice we made, and the location of the key. It will return one thing - whether or not the key has been found. Lets see it:



`Code Example 6 - Creating an inspect function`



<pre >def inspect(choice,location):
    if choice == location:
        print("")
        print("You found a key!")
        print("")
        return 1
    else:
        print("")
        print("Nothing of interest here.")
        print("")
        return 0
</pre>



Now the main program can be a little simpler. Let's take it from the while loop, and change things around:



`Code Example 7 - The new game`

<pre >while loop == 1:
    keyfound = inspect(menu(items,"What do you want to inspect? "), keylocation)
    if keyfound == 1:
        print("You put the key in the lock of the door, and turn it. It opens!")
        loop = 0

print("Light floods into the room, \
as you open the door to your freedom.")
</pre>


Now the program becomes massively shorter - from a cumbersome 83 lines, to a very shapely 50 lines! Of course, you lose quite a bit of versatility - all the items in the room do the same thing. You automatically open the door when you find the key. The game becomes a little less interesting. It also becomes a little harder to change.


<a name="Classes" />

## Classes

<pre>
 
Introduction
Creating a Class
Using a Class
Lingo
Inheritance
Pointers and Dictionaries of Classes
</pre>


### Introduction

One thing that you will get to know about programming, is that programmers like to be lazy. If something has been done before, why should you do it again? 

That is what functions cover in Python. You've already had your code do something special. Now you want to do it again. You put that special code into a function, and re-use it for all it is worth. You can refer to a function anywhere in your code, and the computer will always know what you are talking about. Handy, eh?

Of course, functions have their limitations. Functions don't store any information like variables do - every time a function is run, it starts afresh. However, certain functions and variables are related to each other very closely, and need to interact with each other a lot. For example, imagine you have a golf club. It has information about it (i.e. variables) like the length of the shaft, the material of the grip, and the material of the head. It also has functions associated with it, like the function of swinging your golf club, or the function of breaking it in pure frustration. For those functions, you need to know the variables of the shaft length, head material, etc.

That can easily be worked around with normal functions. Parameters affect the effect of a function. But what if a function needs to affect variables? What happens if each time you use your golf club, the shaft gets weaker, the grip on the handle wears away a little, you get that little more frustrated, and a new scratch is formed on the head of the club? A function cannot do that. A function only makes one output, not four or five, or five hundred. What is needed is a way to group functions and variables that are closely related into one place so that they can interact with each other.

Chances are that you also have more than one golf club. Without classes, you need to write a whole heap of code for each different golf club. This is a pain, seeing that all clubs share common features, it is just that some have changed properties - like what the shaft is made of, and its weight. The ideal situation would be to have a design of your basic golf club. Each time you create a new club, simply specify its attributes - the length of its shaft, its weight, etc.

Or what if you want a golf club, which has added extra features? Maybe you decide to attach a clock to your golf club (why, I don't know - it was your idea). Does this mean that we have to create this golf club from scratch? We would have to write code first for our basic golf club, plus all of that again, and the code for the clock, for our new design. Wouldn't it be better if we were to just take our existing golf club, and then tack the code for the clock to it?

These problems are what a thing called object-oriented-programming solves. It puts functions and variables together in a way that they can see each other and work together, be replicated, and altered as needed, and not when unneeded. And we use a thing called a 'class' to do this.


### Creating a Class

What is a class? Think of a class as a blueprint. It isn't something in itself, it simply describes how to make something. You can create lots of objects from that blueprint - known technically as instances.

So how do you make these so-called 'classes'? Very easily, with the class operator:



`Code Example 1 - defining a class`

<pre ># Defining a class
class class_name:
    [statement 1]
    [statement 2]
    [statement 3]
    [etc.]
</pre>

Makes little sense? That's okay, here is an example that creates the definition of a Shape:



`Code Example 2 - Example of a Class`



<pre >#An example of a class
class <span class="nc" style="color: rgb(0, 0, 255); font-weight: bold;">Shape:

    def __init__(<span class="bp" style="color: rgb(0, 128, 0);">self, x, y):
        <span class="bp" style="color: rgb(0, 128, 0);">self.x = x
        <span class="bp" style="color: rgb(0, 128, 0);">self.y = y
        <span class="bp" style="color: rgb(0, 128, 0);">self.description = "This shape has not been described yet"
        <span class="bp" style="color: rgb(0, 128, 0);">self.author = "Nobody has claimed to make this shape yet"

    def area(<span class="bp" style="color: rgb(0, 128, 0);">self):
        return <span class="bp" style="color: rgb(0, 128, 0);">self.x * <span class="bp" style="color: rgb(0, 128, 0);">self.y

    def perimeter(<span class="bp" style="color: rgb(0, 128, 0);">self):
        return 2 * <span class="bp" style="color: rgb(0, 128, 0);">self.x + 2 * <span class="bp" style="color: rgb(0, 128, 0);">self.y

    def describe(<span class="bp" style="color: rgb(0, 128, 0);">self, text):
        <span class="bp" style="color: rgb(0, 128, 0);">self.description = text

    def authorName(<span class="bp" style="color: rgb(0, 128, 0);">self, text):
        <span class="bp" style="color: rgb(0, 128, 0);">self.author = text

    def scaleSize(<span class="bp" style="color: rgb(0, 128, 0);">self, scale):
        <span class="bp" style="color: rgb(0, 128, 0);">self.x = <span class="bp" style="color: rgb(0, 128, 0);">self.x * scale
        <span class="bp" style="color: rgb(0, 128, 0);">self.y = <span class="bp" style="color: rgb(0, 128, 0);">self.y * scale
</pre>



What you have created is a description of a shape (That is, the variables) and what operations you can do with the shape (That is, the functions). This is very important - you have not made an actual shape, simply the description of what a shape is. The shape has a width (x), a height (y), and an area and perimeter (area(self) and perimeter(self)). No code is run when you define a class - you are simply making functions and variables.

The function called __init__ is run when we create an instance of Shape - that is, when we create an actual shape, as opposed to the 'blueprint' we have here, __init__ is run. You will understand how this works later.

self is how we refer to things in the class from within itself. self is the first parameter in any function defined inside a class. Any function or variable created on the first level of indentation (that is, lines of code that start one TAB to the right of where we put class Shape) is automatically put into self. To access these functions and variables elsewhere inside the class, their name must be preceeded with self and a full-stop (e.g. self.variable_name).

### Using a Class

Its all well and good that we can make a class, but how do we use one? Here is an example, of what we call creating an instance of a class. Assume that the code example 2 has already been run:



`Code Example 3 - Creating a class`



<pre >rectangle = Shape(100, 45)
</pre>



What has been done? It takes a little explaining...

The __init__ function really comes into play at this time. We create an instance of a class by first giving its name (in this case, Shape) and then, in brackets, the values to pass to the __init__ function. The init function runs (using the parameters you gave it in brackets) and then spits out an instance of that class, which in this case is assigned to the name rectangle.

Think of our class instance, rectangle, as a self-contained collection of variables and functions. In the same way that we used self to access functions and variables of the class instance from within itself, we use the name that we assigned to it now (rectangle) to access functions and variables of the class instance from outside of itself. Following on from the code we ran above, we would do this:



`Code Example 4 - accessing attributes from outside an instance`



<pre >#finding the area of your rectangle:
print rectangle.area()

#finding the perimeter of your rectangle:
print rectangle.perimeter()

#describing the rectangle
rectangle.describe("A wide rectangle, more than twice\
 as wide as it is tall")

#making the rectangle 50% smaller
rectangle.scaleSize(<span class="mf" style="color: rgb(102, 102, 102);">0.5)

#re-printing the new area of the rectangle
print rectangle.area()
</pre>



As you see, where self would be used from within the class instance, its assigned name is used when outside the class. We do this to view and change the variables inside the class, and to access the functions that are there.

We aren't limited to a single instance of a class - we could have as many instances as we like. I could do this:



`Code Example 5 - More than one instance`



<pre >long_rectangle = Shape(120,10)
fat_rectangle = Shape(130,120)
</pre>



Both long_rectangle and fat_rectangle have their own functions and variables contained inside them - they are totally independent of each other. There is no limit to the number of instances I could create.

### Lingo

Object-oriented programming has a set of lingo that is associated with it. Its about time that we have this all cleared up:

<pre>
*   when we first describe a class, we are defining it (like with functions)
*   the ability to group similar functions and variables together is called encapsulation
*   the word 'class' can be used when describing the code where the class is defined (like how a function is defined), and it can also refer to an instance of that class - this can get confusing, so make sure you know in which form we are talking about classes
*   a variable inside a class is known as an Attribute
*   a function inside a class is known as a method
*   a class is in the same category of things as variables, lists, dictionaries, etc. That is, they are objects
*   a class is known as a 'data structure' - it holds data, and the methods to process that data.
</pre>



### Inheritance

Let's have a look back at the introduction. We know how classes group together variables and functions, known as attributes and methods, so that both the data and the code to process it is in the same spot. We can create any number of instances of that class, so that we don't have to write new code for every new object we create. But what about adding extra features to our golf club design? This is where inheritance comes into play.

Python makes inheritance really easy. We define a new class, based on another, 'parent' class. Our new class brings everything over from the parent, and we can also add other things to it. If any new attributes or methods have the same name as an attribute or method in our parent class, it is used instead of the parent one. Remember the Shape class?



`Code Example 6 - the Shape class`



<pre >class <span class="nc" style="color: rgb(0, 0, 255); font-weight: bold;">Shape:
    def __init__(<span class="bp" style="color: rgb(0, 128, 0);">self,x,y):
        <span class="bp" style="color: rgb(0, 128, 0);">self.x = x
        <span class="bp" style="color: rgb(0, 128, 0);">self.y = y
        <span class="bp" style="color: rgb(0, 128, 0);">self.description = "This shape has not been described yet"
        <span class="bp" style="color: rgb(0, 128, 0);">self.author = "Nobody has claimed to make this shape yet"
    def area(<span class="bp" style="color: rgb(0, 128, 0);">self):
        return <span class="bp" style="color: rgb(0, 128, 0);">self.x * <span class="bp" style="color: rgb(0, 128, 0);">self.y
    def perimeter(<span class="bp" style="color: rgb(0, 128, 0);">self):
        return 2 * <span class="bp" style="color: rgb(0, 128, 0);">self.x + 2 * <span class="bp" style="color: rgb(0, 128, 0);">self.y
    def describe(<span class="bp" style="color: rgb(0, 128, 0);">self,text):
        <span class="bp" style="color: rgb(0, 128, 0);">self.description = text
    def authorName(<span class="bp" style="color: rgb(0, 128, 0);">self,text):
        <span class="bp" style="color: rgb(0, 128, 0);">self.author = text
    def scaleSize(<span class="bp" style="color: rgb(0, 128, 0);">self,scale):
        <span class="bp" style="color: rgb(0, 128, 0);">self.x = <span class="bp" style="color: rgb(0, 128, 0);">self.x * scale
        <span class="bp" style="color: rgb(0, 128, 0);">self.y = <span class="bp" style="color: rgb(0, 128, 0);">self.y * scale
</pre>



If we wanted to define a new class, let's say a square, based on our previous Shape class, we would do this:



`Code Example 7 - Using inheritance`



<pre >class <span class="nc" style="color: rgb(0, 0, 255); font-weight: bold;">Square(Shape):
    def __init__(<span class="bp" style="color: rgb(0, 128, 0);">self,x):
        <span class="bp" style="color: rgb(0, 128, 0);">self.x = x
        <span class="bp" style="color: rgb(0, 128, 0);">self.y = x
</pre>



It is just like normally defining a class, but this time we put in brackets after the name, the parent class that we inherited from. As you see, we described a square really quickly because of this. That's because we inherited everything from the shape class, and changed only what needed to be changed. In this case we redefined the __init__ function of Shape so that the X and Y values are the same.

Let's take from what we have learnt, and create another new class, this time inherited from Square. It will be two squares, one immediately left of the other:



`Code Example 8 - DoubleSquare class`



<pre ># The shape looks like this:
# _________
#|    |    |
#|    |    |
#|____|____|

class <span class="nc" style="color: rgb(0, 0, 255); font-weight: bold;">DoubleSquare(Square):
    def __init__(<span class="bp" style="color: rgb(0, 128, 0);">self,y):
        <span class="bp" style="color: rgb(0, 128, 0);">self.x = 2 * y
        <span class="bp" style="color: rgb(0, 128, 0);">self.y = y
    def perimeter(<span class="bp" style="color: rgb(0, 128, 0);">self):
        return 2 * <span class="bp" style="color: rgb(0, 128, 0);">self.x + 3 * <span class="bp" style="color: rgb(0, 128, 0);">self.y
</pre>



This time, we also had to redefine the perimeter function, as there is a line going down the middle of the shape. Try creating an instance of this class. 
### Pointers and Dictionaries of Classes

Thinking back, when you say that one variable equals another, e.g. variable2 = variable1, the variable on the left-hand side of the equal-sign takes on the value of the variable on the right. With class instances, this happens a little differently - the name on the left becomes the class instance on the right. So in instance2 = instance1, instance2 is 'pointing' to instance1 - there are two names given to the one class instance, and you can access the class instance via either name.

In other languages, you do things like this using pointers, however in python this all happens behind the scenes.

The final thing that we will cover is dictionaries of classes. Keeping in mind what we have just learnt about pointers, we can assign an instance of a class to an entry in a list or dictionary. This allows for virtually any amount of class instances to exist when our program is run. Lets have a look at the example below, and see how it describes what I am talking about:



`Code Example 9 - Dictionaries of Classes`



<pre ># Again, assume the definitions on Shape,
# Square and DoubleSquare have been run.
# First, create a dictionary:
dictionary = {}

# Then, create some instances of classes in the dictionary:
dictionary["DoubleSquare 1"] = DoubleSquare(5)
dictionary["long rectangle"] = Shape(600,45)

#You can now use them like a normal class:
print dictionary["long rectangle"].area()

dictionary["DoubleSquare 1"].authorName("The Gingerbread Man")
print dictionary["DoubleSquare 1"].author
</pre>



As you see, we simply replaced our boring old name on the left-hand side with an exciting, new, dynamic, dictionary entry. Pretty cool, eh?



<a name="Importing_Modules" />

## Importing Modules

### Introduction

Last lesson we covered the killer topic of Classes. As you can remember, classes are neat combinations of variables and functions in a nice, neat package. Programming lingo calls this feature encapsulation, but regardless of what it is called, it's a really cool feature for keeping things together so the code can be used in many instances in lots of places. Of course, you've got to ask, "how do I get my classes to many places, in many programs?". The answer is to put them into a module, to be imported into other programs.

### Module? What's a Module?

A module is a Python file that (generally) has only definitions of variables, functions, and classes. For example, a module might look like this:



`Code Example 1 - moduletest.py`



<pre >### EXAMPLE PYTHON MODULE
# Define some variables:
numberone = 1
ageofqueen = 78

# define some functions
def printhello():
    print "hello"

def timesfour(input):
    print input * 4

# define a class
class <span class="nc" style="color: rgb(0, 0, 255); font-weight: bold;">Piano:
    def __init__(<span class="bp" style="color: rgb(0, 128, 0);">self):
        <span class="bp" style="color: rgb(0, 128, 0);">self.type = raw_input("What type of piano? ")
        <span class="bp" style="color: rgb(0, 128, 0);">self.height = raw_input("What height (in feet)? ")
        <span class="bp" style="color: rgb(0, 128, 0);">self.price = raw_input("How much did it cost? ")
        <span class="bp" style="color: rgb(0, 128, 0);">self.age = raw_input("How old is it (in years)? ")

    def printdetails(<span class="bp" style="color: rgb(0, 128, 0);">self):
        print "This piano is a/an " + <span class="bp" style="color: rgb(0, 128, 0);">self.height + " foot",
        print <span class="bp" style="color: rgb(0, 128, 0);">self.type, "piano, " + <span class="bp" style="color: rgb(0, 128, 0);">self.age, "years old and costing\
 " + <span class="bp" style="color: rgb(0, 128, 0);">self.price + " dollars."
</pre>



As you see, a module looks pretty much like your normal Python program.

So what do we do with a module? We import bits of it (or all of it) into other programs.

To import all the variables, functions and classes from moduletest.py into another program you are writing, we use the import operator. For example, to import moduletest.py into your main program, you would have this:



`Code Example 2 - mainprogram.py`



<pre >### mainprogam.py
### IMPORTS ANOTHER MODULE
<span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">import <span class="nn" style="color: rgb(0, 0, 255); font-weight: bold;">moduletest
</pre>



This assumes that the module is in the same directory as mainprogram.py, or is a default module that comes with python. You leave out the '.py' at the end of the file - it is ignored. You normally put all import statements at the beginning of the python file, but technically they can be anywhere. In order to use the items in the module in your main program, you use the following:



`Code Example 3 - mainprogram.py continued`



<pre >### USING AN IMPORTED MODULE
# Use the form modulename.itemname
# Examples:
print moduletest.ageofqueen
cfcpiano = moduletest.Piano()
cfcpiano.printdetails()
</pre>



As you see, the modules that you import act very much like the classes we looked at last lesson - anything inside them must be preceeded with modulename. for it to work.

### More Module Thingamajigs (for lack of a better title)

Wish you could get rid of the modulename. part that you have to put before every item you use from a module? No? Never? Well, I'll teach it you anyway.

One way to avoid this hassle is to import only the wanted objects from the module. To do this, you use the from operator. You use it in the form of from modulename import itemname. Here is an example:



`Code Example 4 - importing individual objects`



<pre >### IMPORT ITEMS DIRECTLY INTO YOUR PROGRAM

# import them
<span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">from <span class="nn" style="color: rgb(0, 0, 255); font-weight: bold;">moduletest <span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">import ageofqueen
<span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">from <span class="nn" style="color: rgb(0, 0, 255); font-weight: bold;">moduletest <span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">import printhello

# now try using them
print ageofqueen
printhello()
</pre>



What is the point of this? Well, maybe you could use it to make your code a little more readable. If we get into heaps of modules inside modules, it could also remove that extra layer of crypticness.

If you wanted to, you could import everything from a module in this way by using from modulename import *. Of course, this can be troublesome if there are objects in your program with the same name as some items in the module. With large modules, this can easily happen, and can cause many a headache. A better way to do this would be to import a module in the normal way (without the from operator) and then assign items to a local name:



`Code Example 5 - mainprogram.py continued`



<pre >### ASSIGNING ITEMS TO A LOCAL NAME

# Assigning to a local name
timesfour = moduletest.timesfour

# Using the local name
print timesfour(565)
</pre>



This way, you can remove some crypticness, AND have all of the items from a certain module.




<a name="File_I/O"></a>

# File I/O

<pre>
Introduction
Opening a File
Seek and You Shall Find
Other I/O Functions
Mmm, Pickles
</pre>


### Introduction

Last lesson we learnt how to load external code into our program. Without any introduction (like what I usually have), let's delve into file input and output with normal text files, and later the saving and restoring of instances of classes. (Wow, our lingo power has improved greatly!)

### Opening a File

To open a text file you use, well, the open() function. Seems sensible. You pass certain parameters to open() to tell it in which way the file should be opened - 'r' for read only, 'w' for writing only (if there is an old file, it will be written over), 'a' for appending (adding things on to the end of the file) and 'r+' for both reading and writing. But less talk, lets open a file for reading (you can do this in your python idle mode). Open a normal text file. We will then print out what we read inside the file:


`Code Example 1 - Opening a file`

<pre >openfile = open('pathtofile', 'r')
openfile.read()
</pre>


That was interesting. You'll notice a lot of '\n' symbols. These represent newlines (where you pressed enter to start a new line). The text is completely unformatted, but if you were to pass the output of openfile.read() to print (by typing print openfile.read()) it would be nicely formatted.

### Seek and You Shall Find

Did you try typing in print openfile.read()? Did it fail? It likely did, and reason is because the 'cursor' has changed it's place. Cursor? What cursor? Well, a cursor that you really cannot see, but still a cursor. This invisible cursor tells the read function (and many other I/O functions) where to start from. To set where the cursor is, you use the seek() function. It is used in the form seek(offset, whence).

whence is optional, and determines where to seek from. If whence is 0, the bytes/letters are counted from the beginning. If it is 1, the bytes are counted from the current cursor position. If it is 2, then the bytes are counted from the end of the file. If nothing is put there, 0 is assumed.

offset decribes how far from whence that the cursor moves. for example:

openfile.seek(45,0) would move the cursor to 45 bytes/letters after the beginning of the file. openfile.seek(10,1) would move the cursor to 10 bytes/letters after the current cursor position. openfile.seek(-77,2) would move the cursor to 77 bytes/letters before the end of the file (notice the - before the 77) Try it out now. Use openfile.seek() to go to any spot in the file and then try typing print openfile.read(). It will print from the spot you seeked to. But realise that openfile.read() moves the cursor to the end of the file - you will have to seek again.

### Other I/O Functions

There are many other functions that help you with dealing with files. They have many uses that empower you to do more, and make the things you can do easier. Let's have a look at tell(), readline(), readlines(), write() and close().

tell() returns where the cursor is in the file. It has no parameters, just type it in (like what the example below will show). This is infinitely useful, for knowing what you are refering to, where it is, and simple control of the cursor. To use it, type fileobjectname.tell() - where fileobjectname is the name of the file object you created when you opened the file (in openfile = open('pathtofile', 'r') the file object name is openfile).

readline() reads from where the cursor is till the end of the line. Remember that the end of the line isn't the edge of your screen - the line ends when you press enter to create a new line. This is useful for things like reading a log of events, or going through something progressively to process it. There are no parameters you have to pass to readline(), though you can optionally tell it the maximum number of bytes/letters to read by putting a number in the brackets. Use it with fileobjectname.readline().

readlines() is much like readline(), however readlines() reads all the lines from the cursor onwards, and returns a list, with each list element holding a line of code. Use it with fileobjectname.readlines(). For example, if you had the text file:



`Code Example 2 - example text file`

<pre>Line 1

Line 3
Line 4

Line 6
</pre>

The returned list from readlines() would be:

<table border="1" width="25%"><caption>Table 1 - resulting list from readlines</caption>

<tbody>

<tr>

<th>Index</th>

<th>Value</th>

</tr>

<tr>

<td>0</td>

<td>'Line 1'</td>

</tr>

<tr>

<td>1</td>

</tr>

<tr>

<td>2</td>

<td>'Line 3'</td>

</tr>

<tr>

<td>3</td>

<td>'Line 4'</td>

</tr>

<tr>

<td>4</td>

</tr>

<tr>

<td>5</td>

<td>'Line 6'</td>

</tr>

</tbody>

</table>

The write() function, writes to the file. How did you guess? It writes from where the cursor is, and overwrites text in front of it - like in MS Word, where you press 'insert' and it writes over the top of old text. To utilise this most purposeful function, put a string between the brackets to write e.g. fileobjectname.write('this is a string').

close, you may figure, closes the file so that you can no longer read or write to it until you reopen in again. Simple enough. To use, you would write fileobjectname.close(). Simple!

In Python, open up a test file (or create a new one...) and play around with these functions. You can do some simple (and very inconvenient) text editing.

### Mmm, Pickles

Pickles, in Python, are to be eaten. Their flavour is just too good to let programmers leave them in the fridge.

Ok, just joking there. Pickles, in Python, are objects saved to a file. An object in this case could be a variables, instance of a class, or a list, dictionary, or tuple. Other things can also be pickled, but with limits. The object can then be restored, or unpickled, later on. In other words, you are 'saving' your objects.

So how do we pickle? With the dump() function, which is inside the pickle module - so at the beginning of your program you will have to write import pickle. Simple enough? Then open an empty file, and use pickle.dump() to drop the object into that file. Let's try that:



`Code Example 3 - pickletest.py`



<pre >### pickletest.py
### PICKLE AN OBJECT

# import the pickle module
<span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">import <span class="nn" style="color: rgb(0, 0, 255); font-weight: bold;">pickle

# lets create something to be pickled
# How about a list?
picklelist = ['one',2,'three','four',5,'can you count?']

# now create a file
# replace filename with the file you want to create
file = open('filename', 'w')

# now let's pickle picklelist
pickle.dump(picklelist,file)

# close the file, and your pickling is complete
file.close()
</pre>



The code to do this is laid out like pickle.load(object_to_pickle, file_object) where:

*   object_to_pickle is the object you want to pickle (i.e. save it to file)
*   file_object is the file object you want to write to (in this case, the file object is 'file')

After you close the file, open it in notepad and look at what you see. Along with some other gibblygook, you will see bits of the list we created.

Now to re-open, or unpickle, your file. to use this, we would use pickle.load():



`Code Example 4 - unpickletest.py`



<pre >### unpickletest.py
### unpickle file

# import the pickle module
<span class="kn" style="color: rgb(0, 128, 0); font-weight: bold;">import <span class="nn" style="color: rgb(0, 0, 255); font-weight: bold;">pickle

# now open a file for reading
# replace filename with the path to the file you created in pickletest.py
unpicklefile = open('filename', 'r')

# now load the list that we pickled into a new object
unpickledlist = pickle.load(unpicklefile)

# close the file, just for safety
unpicklefile.close()

# Try out using the list
for item <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in unpickledlist:
    print item
</pre>



Nifty, eh?

Of course, the limitation above is that we can only put in one object to a file. We could get around this by putting lots of picklable objects in a list or dictionary, and then pickling that list or dictionary. This is the quickest and easiest way, but you can do some pretty advanced stuff if you have advanced knowledge of pickle.

Which we won't cover.

<a name="Exception_Handling" />

## Exception Handling

<pre>
Introduction
Bugs - Human Errors
Exceptions - Limitations of the Code
Endless Errors
</pre>


### Introduction

If you haven't seen them before, you're not trying hard enough. What are they? Errors. Exceptions. Problems. Know what I'm talking about? I got it with this program:



`Code Example 1 - buggy program`



<pre >def menu(list, question):
    for entry <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in list:
        print 1 + list.index(entry),
        print ") " + entry

    return raw_input(question) - 1

# running the function
# remember what the backslash does
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')

print 'You picked answer ' + (answer + 1)
</pre>



This is just an example of the menu program we made earlier. Appears perfectly fine to me. At least until when I first tried it. Run the program, and what happens?

### Bugs - Human Errors

The most common problems with your code are of your own doing. Sad, but true. What do we see when we try to run our crippled program?



`Code Example 2 - error message`

<pre style="font-family: monospace, Courier; color: black; border: 1px solid rgb(221, 221, 221); padding: 1em; white-space: pre-wrap; line-height: 1.3em; background-color: rgb(249, 249, 249);">Traceback (most recent call last):
  File "/home/steven/errortest.py", line 8, in -toplevel-
    answer = menu(< I'll snip it here >)
  File "/home/steven/errortest.py", line 6, in menu
    return raw_input(question) - 1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
</pre>

Say what? What Python is trying to tell you (but struggling to find a good word for it) is that you can't join a string of letters and a number into one string of text. Let's go through the error message and have a look at how it tells us that:

*   `File "/home/steven/errortest.py", line 8, in -toplevel-` tells us a couple of things. File "/home/steven/errortest.py" tells us which file the error occured in. This is useful if you use lots of modules that refer to each other. line 8, in -toplevel- tells us that it is in line # 8 of the file, and in the top level (that is, no indentation).
*   `answer = menu(['A','B','C','D','E','F','H','I'],'Which letter is your favourite? ')` duplicates the code where the error is.
*   Since this line calls a function, the next two lines describe where in the function the error occured.
*   `TypeError: unsupported operand type(s) for -: 'str' and 'int'` tells you the error. In this case, it is a 'TypeError', where you tried to subtract incompatible variables.

There are multiple file and code listings for a single error, because the error occured with the interaction of two lines of code (e.g. when using a function, the error occured on the line where the function was called, AND the line in the function where things went wrong).

Now that we know what the problem is, how do we fix it. Well, the error message has isolated where the problem is, so we'll only concentrate on that bit of code.



`Code Example 3 - calling the menu function`

<pre >answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')
</pre>

This is a call to a function. The error occured in the function in the following line


`Code Example 4 - Where it went wrong`



<pre >return raw_input(question) - 1
</pre>


raw_input always returns a string, hence our problem. Let's change it to input(), which, when you type in a number, it returns a number:



`Code Example 5 - Fixing it`



<pre >return input(question) - 1
</pre>



Bug fixed!

### Exceptions - Limitations of the Code

Okay, the program works when you do something normal. But what if you try something weird? Type in a letter (lets say, 'm') instead of a number? Whoops!



`Code Example 6 - Another error message`

<pre style="font-family: monospace, Courier; color: black; border: 1px solid rgb(221, 221, 221); padding: 1em; white-space: pre-wrap; line-height: 1.3em; background-color: rgb(249, 249, 249);">Traceback (most recent call last):
  File "/home/steven/errortest.py", line 8, in -toplevel-
    answer = menu(< I'll snip it here >)
  File "/home/steven/errortest.py", line 6, in menu
    return input(question) - 1
  File "", line 0, in -toplevel-
NameError: name 'm' is not defined
</pre>

What is this telling us? There are two code listings - one in line 8, and the other in line 6\. What this is telling us is that when we called the menu function in line 8, an error occured in line 6 (where we take away 1). This makes sense if you know what the input() function does - I did a bit of reading and testing, and realised that if you type in a letter or word, it will assume that you are mentioning a variable! so in line 6, we are trying to take 1 away from the variable 'm', which doesn't exist.

Have no clue on how to fix this? One of the best and easiest ways is to use the try and except operators.

Here is an example of try being used in a program:



`Code Example 7 - The try operator`



<pre >try:
    function(world, parameters)
except:
    print world.errormsg
</pre>



This is an example of a really messy bit of code that I was trying to fix. First, the code under try: is run. If there is an error, the compiler jumps to the except section and prints world.errormsg. The program doesn't stop right there and crash, it runs the code under except: then continues on.

Let's try that where the error occured in our code (line 6). The menu function now is:



`Code Example 8 - testing our fix`



<pre >def menu(list, question):
    for entry <span class="ow" style="color: rgb(170, 34, 255); font-weight: bold;">in list:
        print 1 + list.index(entry),
        print ") " + entry
    try:
        return input(question) - 1
    except NameError:
        print "Enter a correct number"
</pre>



Try entering a letter when you're asked for a number and see what happens. Dang. We fixed one problem, but now it has caused another problem furthur down the track. This happens all the time. (Sometimes you end up going around in circles, because your code is an absolute mess). Let's have a look at the error:



`Code Example 9 - Yet another error message`

<pre style="font-family: monospace, Courier; color: black; border: 1px solid rgb(221, 221, 221); padding: 1em; white-space: pre-wrap; line-height: 1.3em; background-color: rgb(249, 249, 249);">Traceback (most recent call last):
  File "/home/steven/errortest.py", line 12, in -toplevel-
    print 'You picked answer', (answer + 1)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
</pre>

What has happened this time is that the menu function has returned no value - it only printed an error message. When, at the end of the program, we try to print the returned value plus 1, what is the returned value? There is no returned value? So what is 1 + ... well, we have no clue what we are adding 1 to!

We could just return any old number, but that would be lying. What we really should to is rewrite the program to cope with this exception. With what? try and except!



`Code Example 10 - yet another solution`



<pre ># from when we finish defining the function
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')
try:
    print 'You picked answer', (answer + 1)
    # you can put stuff after a comma in the 'print' statement,
    # and it will continue as if you had typed in 'print' again
except:
    print '\nincorrect answer.'
    # the '\n' is for formatting reasons. Try without it and see.
</pre>



Problem solved again.

### Endless Errors

The approach that we used above is not recomended. Why? Because apart from the error that we know can happen, except: catches every other error too. What if this means we never see an error that could cause problems down the track? If except: catches every error under the sun, we have no hope of controlling what errors we deal with, and the other ones that we want to see, because so far we haven't dealt with them. We also have little hope of dealing with more than one type of error in the same block of code. What should one do, when all is hopeless? Here is an example of code with such a situation:



`Code Example 11 - The Problem We Face`



<pre >print 'Subtraction program, v0.0.1 (beta)'
a = input('Enter a number to subtract from > ')
b = input('Enter the number to subtract > ')
print a - b
</pre>



Okay, you enter your two numbers and it works. Enter a letter, and it gives you a NameError. Lets rewrite the code to deal with a NameError only. We'll put the program in a loop, so it restarts if an error occurs (using continue, which starts the loop from the top again, and break, which leaves the loop):



`Code Example 12 - Dealing With NameError`



<pre >print 'Subtraction program, v0.0.2 (beta)'
loop = 1
while loop == 1:
    try:
        a = input('Enter a number to subtract from > ')
        b = input('Enter the number to subtract > ')
    except NameError:
        print "\nYou cannot subtract a letter"
        continue
    print a - b
    try:
        loop = input('Press 1 to try again > ')
    except NameError:
        loop = 0
</pre>



Here, we restarted the loop if you typed in something wrong. In line 12 we assumed you wanted to quit the program if you didn't press 1, so we quit the program.

But there are still problems. If we leave something blank, or type in an unusual character like ! or ;, the program gives us a SyntaxError. Lets deal with this. When we are asking for the numbers to subtract, we will give a different error message. When we ask to press 1, we will again assume the user wants to quit.



`Code Example 13 - Now, dealing with SyntaxError`



<pre >print 'Subtraction program, v0.0.3 (beta)'
loop = 1
while loop == 1:
    try:
        a = input('Enter a number to subtract from > ')
        b = input('Enter the number to subtract > ')
    except NameError:
        print "\nYou cannot subtract a letter"
	continue
    except SyntaxError:
        print "\nPlease enter a number only."
	continue
    print a - b
    try:
        loop = input('Press 1 to try again > ')
    except (NameError,SyntaxError):
        loop = 0
</pre>



As you can see, you can have multiple except uses, each dealing with a different problem. You can also have one except to deal with multiple exceptions, by putting them inside parentheses and seperating them with commas.

Now we have a program that is very difficult, to crash by an end user. As a final challenge, see if you can crash it. There is one way I have thought of - if you read the section on human error carefully, you might know what it is.
