mkdir haystack/folder{1..500} # create 100 folders in the folder of haystack

touch haystack/folder{1..500}/file{1..100} # create 100 files in each of previously created 100 folders

touch haystack/folder${shuf -i 1-500 -n 1)/needle.txt # create random

find haystack/ -type f -name "needle.txt" # find the needle in the haystack

find haystack/ -type f -name "needle.txt" -exec mv {} ~/Desktop \; # move the file to the Desktop # \; end the command when completely finished

find haystack/ -type f -name "needle.txt" -ok mv {} ~/Desktop \; # interactive - ok y/n

find /etc -maxdepth 4 # limite search depth
find /etc -type d -maxdepth 4 # wrong command |||||||||||||||||| find /etc -maxdepth 4 -type d # correct command
find /etc -maxdepth 4 -type f -size +100k
find /etc -maxdepth 4 -type f -size -100k -o +100M # or
sudo find ~ -type f -size +5M -exec rm {} \; # remove every file that is over 5MB below home directory

# locate command use database which may be not updated timely
