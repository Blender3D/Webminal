
[Source](https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-users-tools.html "Permalink to 2.&nbsp;User and Group Management Tools")

### 2.&nbsp;User and Group Management Tools

Managing users and groups can be a tedious task; The following command line tools can also be used to manage users and groups: 

* `useradd`, `usermod`, and `userdel` — Industry-standard methods of adding, deleting and modifying user accounts 
* `groupadd`, `groupmod`, and `groupdel` — Industry-standard methods of adding, deleting, and modifying user groups 
* `gpasswd` — Industry-standard method of administering the `/etc/group` file 
* `pwck`, `grpck` — Tools used for the verification of the password, group, and associated shadow files 
* `pwconv`, `pwunconv` — Tools used for the conversion of passwords to shadow passwords and back to standard passwords 

### 2.1.&nbsp;Command Line Configuration


#### 2.2. Adding a User

To add a user to the system: 

1. Issue the `useradd` command to create a locked user account: 
    
        useradd _<username>_
    

2. Unlock the account by issuing the `passwd` command to assign a password and set password aging guidelines: 
    
        passwd _<username>_
    

Command line options for `useradd` are detailed below. 

| Option                  | Description                                                                                                                                                                                                                                            |  
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  
| `-c` '_`<comment>`_'    | _`<comment>`_ can be replaced with any string. This option is generally used to specify the full name of a user.                                                                                                                                       |  
| `-d` _ `<home-dir>` _   | Home directory to be used instead of default `/home/_`<username>`_/`                                                                                                                                                                                   |  
| `-e` _ `<date>` _       | Date for the account to be disabled in the format YYYY-MM-DD                                                                                                                                                                                           |  
| `-f` _ `<days>` _       | Number of days after the password expires until the account is disabled. If **`0`** is specified, the account is disabled immediately after the password expires. If **`-1`** is specified, the account is not be disabled after the password expires. |  
| `-g` _ `<group-name>` _ | Group name or group number for the user's default group. The group must exist prior to being specified here.                                                                                                                                           |  
| `-G` _ `<group-list>` _ | List of additional (other than default) group names or group numbers, separated by commas, of which the user is a member. The groups must exist prior to being specified here.                                                                         |  
| `-m`                    | Create the home directory if it does not exist.                                                                                                                                                                                                        |  
| `-M`                    | Do not create the home directory.                                                                                                                                                                                                                      |  
| `-n`                    | Do not create a user private group for the user.                                                                                                                                                                                                       |  
| `-r`                    | Create a system account with a UID less than 500 and without a home directory                                                                                                                                                                          |  
| `-p` _ `<password>` _   | The password encrypted with `crypt`                                                                                                                                                                                                                    |  
| `-s`                    | User's login shell, which defaults to `/bin/bash`                                                                                                                                                                                                      |  
| `-u` _ `<uid>` _        | User ID for the user, which must be unique and greater than 499                                                                                                                                                                                        |  



#### 2.3. Adding a Group

To add a group to the system, use the command `groupadd`: 
    
    
    groupadd _<group-name>_
    

Command line options for `groupadd` are detailed below. 

| Option           | Description                                                                                                               |  
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |  
| `-g` _ `<gid>` _ | Group ID for the group, which must be unique and greater than 499                                                         |  
| `-r`             | Create a system group with a GID less than 500                                                                            |  
| `-f`             | When used with `-g`_`<gid>`_ and _`<gid>`_ already exists, `groupadd` will choose another unique _`<gid>`_ for the group. |  

#### 2.4. Password Aging


For security reasons, it is advisable to require users to change their passwords periodically. 

To configure password expiration for a user from a shell prompt, use the `chage` command, followed by an option , followed by the username of the user. 


| Option            | Description                                                                                                                                                                                                                                                          |  
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
| `-m` _ `<days>` _ | Specifies the minimum number of days between which the user must change passwords. If the value is 0, the password does not expire.                                                                                                                                  |  
| `-M` _ `<days>` _ | Specifies the maximum number of days for which the password is valid. When the number of days specified by this option plus the number of days specified with the `-d` option is less than the current day, the user must change passwords before using the account. |  
| `-d` _ `<days>` _ | Specifies the number of days since January 1, 1970 the password was changed                                                                                                                                                                                          |  
| `-I` _ `<days>` _ | Specifies the number of inactive days after the password expiration before locking the account. If the value is 0, the account is not locked after the password expires.                                                                                             |  
| `-E` _ `<date>` _ | Specifies the date on which the account is locked, in the format YYYY-MM-DD. Instead of the date, the number of days since January 1, 1970 can also be used.                                                                                                         |  
| `-W` _ `<days>` _ | Specifies the number of days before the password expiration date to warn the user.                                                                                                                                                                                   |  


If the `chage` command is followed directly by a username (with no options), it displays the current password aging values and allows them to be changed. 

You can configure a password to expire the first time a user logs in. This forces users to change passwords the first time they log in. 


1. _Lock the user password_ — If the user does not exist, use the `useradd` command to create the user account, but do not give it a password so that it remains locked. 

If the password is already enabled, lock it with the command: 
    
        usermod -L _username_
    

2. _Force immediate password expiration_ — Type the following command: 
    
        chage -d 0 _username_
    

This command sets the value for the date the password was last changed to the epoch (January 1, 1970). This value forces immediate password expiration no matter what password aging policy, if any, is in place. 

3. _Unlock the account_ — There are two common approaches to this step. The administrator can assign an initial password or assign a null password. 


You can assign a null password instead of an initial password. To do this, use the following command: 
    
        usermod -p "" _username_
    

#### Caution

Using a null password, while convenient, is a highly unsecure practice, as any third party can log in first an access the system using the unsecure username. Always make sure that the user is ready to log in before unlocking an account with a null password. 

In either case, upon initial log in, the user is prompted for a new password. 

### 2.5.&nbsp;Explaining the Process

The following steps illustrate what happens if the command `useradd juan` is issued on a system that has shadow passwords enabled: 

1. A new line for `juan` is created in `/etc/passwd`. The line has the following characteristics: 

    * It begins with the username `juan`. 

    * There is an `x` for the password field indicating that the system is using shadow passwords. 

    * A UID greater than 499 is created. (Under Red Hat Enterprise Linux, UIDs and GIDs below 500 are reserved for system use.) 

    * A GID greater than 499 is created. 

    * The optional GECOS information is left blank. 

    * The home directory for `juan` is set to `/home/juan/`. 

    * The default shell is set to `/bin/bash`. 

2. A new line for `juan` is created in `/etc/shadow`. The line has the following characteristics: 

    * It begins with the username `juan`. 

    * Two exclamation points (`!!`) appear in the password field of the `/etc/shadow` file, which locks the account. 

    * The password is set to never expire. 

3. A new line for a group named `juan` is created in `/etc/group`. A group with the same name as a user is called a _user private group_.

The line created in `/etc/group` has the following characteristics: 

    * It begins with the group name `juan`. 

    * An `x` appears in the password field indicating that the system is using shadow group passwords. 

    * The GID matches the one listed for user `juan` in `/etc/passwd`. 

4. A new line for a group named `juan` is created in `/etc/gshadow`. The line has the following characteristics: 

    * It begins with the group name `juan`. 

    * An exclamation point (`!`) appears in the password field of the `/etc/gshadow` file, which locks the group. 

    * All other fields are blank. 

5. A directory for user `juan` is created in the `/home/` directory. This directory is owned by user `juan` and group `juan`. However, it has read, write, and execute privileges _only_ for the user `juan`. All other permissions are denied. 

6. The files within the `/etc/skel/` directory (which contain default user settings) are copied into the new `/home/juan/` directory. 

At this point, a locked account called `juan` exists on the system. To activate it, the administrator must next assign a password to the account using the `passwd` command and, optionally, set password aging guidelines. 


