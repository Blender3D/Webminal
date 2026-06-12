
[Source](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux_OpenStack_Platform/2/html/Getting_Started_Guide/ch02s03.html "Permalink to 2.3.&nbsp;Configuring sudo Access")


##  &nbsp;Configuring `sudo` Access

The `sudo` command offers a mechanism for providing trusted users with administrative access to a system without sharing the password of the `root` user. When users given access via this mechanism precede an administrative command with `sudo` they are prompted to enter their own password. Once authenticated, and assuming the command is permitted, the administrative command is executed as if run by the `root` user. 

Follow this procedure to create a normal user account and give it `sudo` access. You will then be able to use the `sudo` command from this user account to execute administrative commands without logging in to the account of the `root` user. 

⁠

**Procedure to configure `sudo` Access**

1. Log in to the system as the `root` user. 

2. Create a normal user account using the `useradd` command. Replace _USERNAME_ with the user name that you wish to create. 
    
        # useradd _USERNAME_

3. Set a password for the new user using the `passwd` command. 
    
        # passwd _USERNAME_
          Changing password for user _USERNAME_.
          New password: 
          Retype new password: 
         passwd: all authentication tokens updated successfully.

4. Run the `visudo` to edit the `/etc/sudoers` file. This file defines the policies applied by the `sudo` command. 
    
        # visudo

5. Find the lines in the file that grant `sudo` access to users in the group `wheel` when enabled. 
    
        ## Allows people in group wheel to run all commands
       # %wheel        ALL=(ALL)       ALL

6. Remove the comment character (**#**) at the start of the second line. This enables the configuration option. 

7. Save your changes and exit the editor. 

8. Add the user you created to the `wheel` group using the `usermod` command. 
    
        # usermod _-aG_ _wheel_ _USERNAME_

9. Test that the updated configuration allows the user you created to run commands using `sudo`. 

    1. Use the `su` to switch to the new user account that you created. 
        
                # su _USERNAME_ _-_

    2. Use the `groups` to verify that the user is in the `wheel` group. 
        
                $ groups
                  _USERNAME_ wheel

    3. Use the `sudo` command to run the `whoami` command. As this is the first time you have run a command using `sudo` from this user account the banner message will be displayed. You will be also be prompted to enter the password for the user account. 
        
                $ sudo whoami
        We trust you have received the usual lecture from the local System
        Administrator. It usually boils down to these three things:
        
            #1) Respect the privacy of others.
            #2) Think before you type.
            #3) With great power comes great responsibility.
        
            [sudo] password for _USERNAME_:
             root

The last line of the output is the user name returned by the `whoami` command. If `sudo` is configured correctly this value will be `root`. 

You have successfully configured a user with `sudo` access. You can now log in to this user account and use `sudo` to run commands as if you were logged in to the account of the `root` user. 

  