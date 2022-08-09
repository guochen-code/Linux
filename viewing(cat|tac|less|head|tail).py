# cat: stick files together to a long file or read content of file
# tac reverses file vertically and rev reverses file horizontallly !!!!!!!!!!!!!!!!!!!

cat file[1-5].txt > beautiful.txt

# write to file (append)
echo "abc" >>alpha.txt
echo "def" >>alpha.txt

cat alpha.tx
'''
abc
def
'''

tac alpha.txt # reverse order
'''
def
abc
'''

cat file[1-5] | tac > reversed.txt

# tac application mp3 or movies
tac myfile.mps > myreversedfile.mp3

cat file[1-5] | rev # reverse along the lines (line by line)

******************************************************************************************************************************************************************
# elegant solution to deal with large files (many lines) or directories

less largefile.txt

cat largefile.txt | less # same as above

cat largefile.txt | head # by default, showing first 10 lines of the file

cat largefile.txt | head -n 2 # show first 2 lines

cat largefile.txt | wc -l # word count command

head -n 20 /etc/largefile.txt

############################################################## head and tail
