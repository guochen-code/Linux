# How to generated 100 random numbers 
shuf -r -i 0-10000000000 -n 100 > numbers.txt

# How to generate 100 random numbers with values between 0 and 9, inclusive.
shuf -r -i 1-10 -n 100 > numbers0-9.txt

# How to generate 100 random words
This process involves using a bash script, which is a relatively advanced concept. Here are the steps I followed:
1.	First, a script online that does this kind of thing at https://linuxconfig.org/random-word-generator
2.	Then, copied and pasted that script into a file called word_generator.sh, saved in my home directory. 
3.	After making sure that in my home directory, then made that script executable by running chmod +x word_generator.sh. 
4.	Then ran the script using ./word_generator.sh 100 > ~/words.txt.   T

# This will save 100 random words into a file called `words.txt` in home directory.
