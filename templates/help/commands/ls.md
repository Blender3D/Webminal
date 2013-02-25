title: ls

# `ls`

`ls` is a command to list files in a folder.

To see what files are in your current folder, just run `ls`:

    $ ls
    file1.txt
    file2.txt
    file3.png
    folder4/

For more verbose information (permissons, owner, group, filesize and name, in that order), append the `-l` flag:

    $ ls -l
    drwxr--r--   1 fred  editors   4096  drafts
    -rw-r--r--   1 fred  editors  30405  edition-32
    -r-xr-xr-x   1 fred  fred      8460  edit
