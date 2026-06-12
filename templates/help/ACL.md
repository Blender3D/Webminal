
[Source](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/ch-Access_Control_Lists.html "Permalink to Chapter&nbsp;4.&nbsp;Access Control Lists")


##  Access Control Lists

Files and directories have permission sets for the owner of the file, the group associated with the file, and all other users for the system. However, these permission sets have limitations. For example, different permissions cannot be configured for different users. Thus, _Access Control Lists_ (ACLs) were implemented. 

The Red Hat Enterprise Linux kernel provides ACL support for the ext3 file system and NFS-exported file systems. ACLs are also recognized on ext3 file systems accessed via Samba. 

Along with support in the kernel, the `acl` package is required to implement ACLs. It contains the utilities used to add, modify, remove, and retrieve ACL information. 

The `cp` and `mv` commands copy or move any ACLs associated with files and directories. 

##  1.&nbsp;Mounting File Systems

Before using ACLs for a file or directory, the partition for the file or directory must be mounted with ACL support. If it is a local ext3 file system, it can mounted with the following command: 

`mount -t ext3 -o acl _device-name_ _partition_`

For example: 

`mount -t ext3 -o acl /dev/VolGroup00/LogVol02 /work`

Alternatively, if the partition is listed in the `/etc/fstab` file, the entry for the partition can include the `acl` option: 
    
    
    LABEL=/work      /work       ext3    acl        1 2
    


##  2.&nbsp;Setting Access ACLs

There are two types of ACLs: _access ACLs_ and _default ACLs_. An access ACL is the access control list for a specific file or directory. A default ACL can only be associated with a directory; if a file within the directory does not have an access ACL, it uses the rules of the default ACL for the directory. Default ACLs are optional. 

ACLs can be configured: 

1. Per user 

2. Per group 

3. Via the effective rights mask 

4. For users not in the user group for the file 

The `setfacl` utility sets ACLs for files and directories. Use the `-m` option to add or modify the ACL of a file or directory: 
    
    
    # setfacl -m _rules_ _files_

Rules (_rules_) must be specified in the following formats. Multiple rules can be specified in the same command if they are separated by commas. 

`u:_uid_:_perms_`

Sets the access ACL for a user. The user name or UID may be specified. The user may be any valid user on the system. 

`g:_gid_:_perms_`


Sets the access ACL for a group. The group name or GID may be specified. The group may be any valid group on the system. 

`m:_perms_`

Sets the effective rights mask. The mask is the union of all permissions of the owning group and all of the user and group entries. 

`o:_perms_`

Sets the access ACL for users other than the ones in the group for the file. 

Permissions (_perms_) must be a combination of the characters `r`, `w`, and `x` for read, write, and execute. 

If a file or directory already has an ACL, and the `setfacl` command is used, the additional rules are added to the existing ACL or the existing rule is modified. 

⁠

**Example 1:&nbsp;Give read and write permissions**

For example, to give read and write permissions to user andrius: 
    
    
    # setfacl -m u:andrius:rw /project/somefile
    

To remove all the permissions for a user, group, or others, use the `-x` option and do not specify any permissions: 
    
    
    # setfacl -x _rules_ _files_

⁠

**Example2:&nbsp;Remove all permissions**

For example, to remove all permissions from the user with UID 500: 
    
    
    # setfacl -x u:500 /project/somefile
    
##  3.&nbsp;Setting Default ACLs

To set a default ACL, add `d:` before the rule and specify a directory instead of a file name. 


**Example 3:&nbsp;Setting default ACLs**

For example, to set the default ACL for the `/share/` directory to read and execute for users not in the user group (an access ACL for an individual file can override it): 
    
    
    # setfacl -m d:o:rx /share
    

# 4.&nbsp;Retrieving ACLs


    # getfacl home/john/picture.png
    

The above command returns the following output: 
    
    
    # file: home/john/picture.png 
    # owner: john 
    # group: john 
    user::rw- 
    group::r-- 
    other::r--

If a directory with a default ACL is specified, the default ACL is also displayed as illustrated below. For example, `getfacl home/sales/` will display similar output: 
    
    
    # file: home/sales/ 
    # owner: john 
    # group: john 
    user::rw- 
    user:barryg:r-- 
    group::r-- 
    mask::r-- 
    other::r-- 
    default:user::rwx 
    default:user:john:rwx 
    default:group::r-x 
    default:mask::rwx 
    default:other::r-x
    

  