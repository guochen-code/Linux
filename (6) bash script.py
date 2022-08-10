(1) create a file called backup.sh and write below in the file: 
    #!/bin/bash            # use bash to interpret, always 1st line
    tar -cvzf backup.tar.gz ~/{Documents,Downloads,Desktop,Pictures,Videos} #
(2) run the script use command:
    bash backup.sh
    
# because of v: verbose, a lot of lines will be printed out on the terminal screen
# if remove v in the command, not so much output anymore. 
# will have one print out: "tar: Removing learding "/" from member names"
# to get rid of right above print out:

tar -cvzf backup.tar.gz ~/{Documents,Downloads,Desktop,Pictures,Videos} 2>/dev/null # redirect error use 2. It is a bitbucket will delete whatever sent to it.

************************************************************* run bash script from anywhere *****************************************************
(1) create a bin folder in the home directory
(2) create or move a bash script hello.sh to the bin folder
(3) add the path of the bin folder to the .bashrc file:
    PATH="$PATH$HOME/bin"
(4) in the bin folder, change the bash script to executable mode:
    chmod+x hello # if you list the file, it will turn to a green color which means executable
(5) go anywhere and run the bash script by typing:
    hello
    
************************************************************* compare with aliases *****************************************************
    
what is the difference vs aliases
all aliases are in ".bash_aliases" file

1) script is designed to contain more than one script line while aliases is just to give more convenient name to just one command line
2) script have more complicated programming constructs such as loops, if statement and functions.
3) script can be sheduled to run at any time using Cron
    
