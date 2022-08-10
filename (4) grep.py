grep -ic a book.txt # case insensitive # search for letter a # c: count
'''
951
'''
# 951 lines contain letter a/A

grep -ic "our boys" book.txt # search for a sentence

wc -l book.txt
'''
1914 book.txt
'''
# this book has 1914 lines

grep -icv e book.txt # how many lines not contain letter e # v: not contain !!!!!!!!!!!
'''
1914
'''

grep -i "e" book1.txt book2.txt


ls hello/ | grep hello.txt # look for hello.txt in hello folder

************************************************************************************************************************************************
ls -F etc/ | grep -v / | sort -r > files.txt # -F: display slash("/") for directories. # -v: not contain 
# get all the file names in one directory in reverse order

man -k print | grep files # search for commands to (1) print (2) print files

man -k "list directory content"
