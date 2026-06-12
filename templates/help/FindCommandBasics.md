
###find command Intro
The GNU find command searches files within a directory and its subdirectories according to several criteria such as name, size and time of last read/write. By default find prints the name of the located files but it can also perform commands on these files. 

The GNU find command is part of the GNU *findutils* and is installed on every Linux system. *findutils* is actually made up of 4 utilities:

 - find - search for files in a directory hierarchy
   
 - locate - list files in databases that match a pattern
      
 - updatedb - update a file name database
       
 - xargs - build and execute command lines from standard input


###The Basics
The syntax for using find is:

      find [-H] [-L] [-P] [path...] [expression]

The 3 options [-H] [-L] [-P] are not commonly seen but should at least be noted if only to realise that the -P option will be the default unless another option is specified:

 1. -H : Do not follow symbolic links, except while processing the command line arguments. 
 2. -L : Follow symbolic links.
 3. -P : Never follow symbolic links: the default option.

The option [path...] refers to the particular location that you wish to search, whether it be your $HOME directory, a particular directory such as /usr, your present working directory which can simply be expressed as '.' or your entire computer which can be expressed as '/'. 

The option [expression] refers to one or a series of options which effect the overall option of the find command. These options can involve a search by name, by size, by access time or can also involve actions taken upon these files. 

###Locating Files by Name
The most common use of find is in the search for a specific file by use of its name. The following command searches the home directory and all of its subdirectories looking for the file mysong.ogg:

    find $HOME -name 'mysong.ogg' 

It is important to get into the habit of quoting patterns in your search as seen above or your search results can be a little unpredictable. Such a search can be much more sophisticated though. For example if you wished to search for all of the ogg files in your home directory, some of which you think might be named 'OGG' rather than 'ogg', you would run:


    find $HOME -iname '*.ogg' 

Here the option '-iname' performs a case-insensitive search while the wildcard character '*' matches any character, or number of characters, or zero characters. To perform the same search on your entire drive you would run:


    `find / -iname '*.ogg'` 
This could be a slow search depending on the number of directories, sub-directories and files on your system. This highlights an important difference in the way that find operates in that it examines the system directly each time unlike programs like locate or slocate which actually examine a regularly updated database of filnames and locations.

###Locating Files by Size
Another possible search is to search for files by size. To demonstrate this we can again search the home directory for Ogg Vorbis files but this time looking for those that are 100 megabytes or larger:


    find $HOME -iname '*.ogg' -size +100M 

There are several options with -size, I have used 'M' for 'megabytes' here but 'k' for 'kilobytes' can be used or 'G' for 'Gigabytes'. This search can then be altered to look for files only that are less than 100 megabytes:


    find $HOME -iname '*.ogg' -type f -size -100M 

Are you starting to see the power of find, and the thought involved in constructing a focused search? If you are interested there is more discussion of these combined searches in the Advanced Usage section below.

###Locating Files by Access Time
It is also possible to locate files based on their access time or the time that they were last used, or viewed by the system. For example to show all files that have not been accessed in the $HOME directory for 30 days or more:


    find $HOME -atime +30

This type of search is normally more useful when combined with other find searches. For example one could search for all ogg files in the $HOME directory that have an access time of greater than 30 days:


    find $HOME -iname '*.ogg' -atime +30

The syntax works from left to right and by default find joins the 2 expressions with an implied "and". This is dealt with in more depth in the section below entitled "Combining Searches".

###Advanced Usage
The sections above detail the most common usage of find and this would be enough for most searches. However there are many more possibilities in the usage of find for quite advanced searches and this sections discusses a few of these possibilities.

####Combining Searches
It is possible to combine searches when using find with the use of what is known in the find man pages as operators. The classic example is the use of a logical AND syntax:


    find $HOME -iname '*.ogg' -size +20M 

This find search performs initially a case insensitive search for all the ogg files in your $HOME directory and for every true results it then searches for those with a size of 20 megabytes and over. This contains and implied operator which could be written joined with an -a. This search can be altered slightly by use of an exclamation point to signify negation of the result:


    find $HOME -iname '*.ogg' ! -size +20M 

This performs the same search as before but will look for ogg files that are not greater than 20 megabytes. It is possible also to use a logical OR in your find search:


    find $HOME -iname '*.ogg' -o -iname '*.mp3'

This will perform a case insensitive search in the $HOME directories and find all files that are either ogg OR mp3 files. There is great scope here for creating very complex and finely honed searches and I would encourage a through reading of the find man pages searching for the topic OPERATORS. 

###Acting On The files
One advanced but highly useful aspect of find usage is the ability to perform a user-specified action on the result of a find search. For example the following search looks for all ogg vorbis files in the $HOME directory and then uses -exec to pass the result to the du program to give the size of each file:


    find $HOME -name '*.ogg' -type f -exec du -h '{}' \;

This syntax is often used to delete files by using -exec rm -rf but this must be used with great caution, if at all, as recovery of any deleted files can be quite difficult.

###Using xargs
When using a really complex search it is often a good idea to use another member of the findutils package: xargs. Without its use the message Argument list too long could be seen signalling that the kernel limit on the combined length of a commandline and its environment variables has been exceeded. xargs works by feeding the results of the search to the subsequent command in batches calculated on the system capabilities (based on ARG_MAX). An example:


    find /tmp -iname '*.mp3' -print0 | xargs -0 rm

This example searches the /tmp folder for all mp3 files and then deletes them. You will note the use of both -print0 and xargs -0 which is a deliberate strategy to avoid problems with spaces and/or newlines in the filenames. Modern kernels do not have the ARG_MAX limitation but to keep your searches portable it is an excellent idea to use xargs in complex searches with subsequent commands.

Source : https://help.ubuntu.com/community/find
