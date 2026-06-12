title: chmod


You should have seen a output like `mode of file1.txt changed to 0666 (rw-rw-rw-)`

That will set the file "file1.txt" to be "world writeable".This means 
the owner, group and others can read and write into file. The same 
effect can be achived (remember you can verify it by using `wm_stat file1.txt`) 
by

	chmod a+rw file1.txt

where as below makes it so that no one can read or write into this file, not even it's owner!

	chmod a-rw file1.txt

with next command only owner can read or write into this file. `chmod u+rw file1.txt`.
`Tips and tricks:` To change permission for more than one file  use the -R switch

	chmod -R 644 ~/chmod_dir
now to change file owner , `chown root file1.txt`
