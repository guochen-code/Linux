********************************************************************* set up your editor *******************************************************************************
# start a cron tab
crontab -e
# if this is your first time run the command, it will print out
'''
choose [1-3].
'''
# choose 1 for nano editor

#check your preference of your editor
cd home/
ls -a
.selected_editor
# this file stored your preference for editor

# change your preference
(1) nan .selected_editor # then edit the content in the file
or
(2) run command: select-editor # it will ask you to choose your editor again.

*********************************************************************** cron tab *****************************************************************************
# crontab has 6 columns: 1-5 columns are related to schedule settings and the 6th column is the command

1st column is minutes: 15 or * for any minute
2nd column is hour number: 11 means 11am and 14 means 2pm or * for any hour
3rd column is day of the month: 10 means 10th day of the month or * for any day of the month
4th column is the month: 1-12 or JAN/FEB/DEC or *
5th column is day of the week: 0 is sunday and 6 is saturday or SUN/SAT/MON
6th columns is the command to run: echo "hello world!" >> ~/Desktop/hello.txt

# add more lines for more commands
1st column is minutes: can be */15 = run every 15 minutes or 0,15,30,45
3rd column is day of the month: */3

example:
59 23 * JAN,DEC SUN echo "Because we can"

*********************************************************************** application ***********************************************************************
The great use of cron to schedule automatd backups of the file system
(1) create a backup directory under home
mkdir Backup
(2) created a backup.sh stored in the bin folder as follows:
#!/bin/bash
tar -czf ~Backup/backup.tar.gz ~/{Documents,Downloads,Desttop,Pictures,Videos} 2>/dev/null
date >> ~/backup/backup.log # log the time when back up
(3) run directly in the terminal:
# because it is in the bin folder and we already added the path to the .bashrc file, we can run script from anywhere by typing:
backup
(4) run as scheduled in cron tab. go to cron tab:
59 23 * * FRI bash ~/bin/backup # backup files every friday at 23:59



  
