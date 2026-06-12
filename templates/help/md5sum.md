title: md5sum

`b8d5079c5d6a9dbb3294b31d318d74c0` is the calculated checksum
for a file.This helps with detecting accidental or deliberate 
file corruption.

When transfering a file from machine to another or downloading 
files from internet,to verify the file integrity compare md5sum 
on source and destination machines,

	md5sum dir2/hello.txt
should be same as 

	md5sum hello.txt

now lets move to another command,

	mv hello.txt dir2/dir3/dir4/hi.txt

