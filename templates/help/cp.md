title: cp

now file is copied to new location.Now compute the usage again using,
`wm_du` now you should see usage has been increased by file size.

>`Tips and tricks:`

	 cp -v hello.txt dir2/file2.txt

This will copy hello.txt into dir2 at the same time, rename it as "file2.txt".


	cp  -vr dir2/*.txt dir2/dir3 

This will copy all files ending with ".txt" from dir2 into dir2/dir3.

	cp -vr dir2/dir3  .

This will copy the directory named "dir3" to current directory.

Use `wm_ls`,it should show you dir3.

now we have copied few files,how do we verify its file integrity?simple 
`cat` should be enough.But If its large file or binary file,we can't use
cat.We have to use,

	md5sum hello.txt 
