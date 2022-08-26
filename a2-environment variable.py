#You can also set environment variables in a single line:

export MY_NEW_VAR="My New Var"

#Environment Variables created in this way are available only in the current session. If you open a new shell or if you log out all variables will be lost.

#to check:
echo $MY_NEW_VAR

#Persistent Environment Variables
#To make Environment variables persistent you need to define those variables in the bash configuration files. 
#In most Linux distributions when you start a new session, environment variables are read from the following files:

(1)
#/etc/environment - Use this file to set up system-wide environment variables. Variables in this file are set in the following format:

$FOO=bar
$VAR_TEST="Test Var"

(2)
#/etc/profile - Variables set in this file are loaded whenever a bash login shell is entered. 
#When declaring environment variables in this file you need to use the export command:

$export JAVA_HOME="/path/to/java/home"
$export PATH=$PATH:$JAVA_HOME/bin

(3)
#Per-user shell specific configuration files. For example, if you are using Bash, you can declare the variables in the ~/.bashrc:

$export PATH="$HOME/bin:$PATH"

#To load the new environment variables into the current shell session use the source command:

$source ~/.bashrc

*****************************************************************************************************************************************************************
#Setting Permanent Global Environment Variables for All Users
#A permanent environment variable that persists after a reboot can be created by adding it to the default profile. 
#This profile is loaded by all users on the system, including service accounts.

#All global profile settings are stored under /etc/profile. And while this file can be edited directory, 
#it is actually recommended to store global environment variables in a directory named /etc/profile.d, 
#where you will find a list of files that are used to set environment variables for the entire system.

(1)
# Create a new file under /etc/profile.d to store the global environment variable(s). 
# The name of the should be contextual so others may understand its purpose. 
# For demonstrations, we will create a permanent environment variable for HTTP_PROXY.
sudo touch /etc/profile.d/http_proxy.sh

(2)
# Open the default profile into a text editor.
sudo vi /etc/profile.d/http_proxy.sh

(3)
# Add new lines to export the environment variables
export HTTP_PROXY=http://my.proxy:8080

export HTTPS_PROXY=https://my.proxy:8080

export NO_PROXY=localhost,::1,.example.com

(4)
Save your changes and exit the text editor
