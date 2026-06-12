title: whereis

you should see an output

	ls: /bin/ls /usr/share/man/man1p/ls.1p.gz /usr/share/man/man1/ls.1.gz 

`whereis` command will locate source files and binaries,lets
see another example,finding source file 

	whereis stdio.h

will give you

	stdio: /usr/include/stdio.h /usr/share/man/man3/stdio.3.gz

Assume,you have installed two version a php (php4 and php5),when you simply type 

	php
which version will get executed?we don't know. In order to find it out,we use

	which php

