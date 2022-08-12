z for gzip, j for bzip2, J for xz
************************************************************************************************************
tarballs are contains to store files in for compression. It does not do compression.

************************************************* achiving *************************************************
# create a tar
tar -cvf filename.tar # c: create # v: verbose # f: Tells tar that the next argument is the name of the tarball.

# file extension does not mean anything in linux
file filename.tar # we can see the nature of the file

# rename file
mv filename.tar filenewname.pdf
file ilenewname.pdf # it will still be a tar file in nature. The linux system is not tricked by the name. But some software can like pdf reader

# check what is inside
tar -tf filename.tar

# extract from tar
tar -xvf filename.tar

************************************************* compression *************************************************
# compression is 2 step process: (1) to tarball (2) compress with gzip (faster but less compression) or bzip2 
# (slower but more compression, not always unless file is very big like movies)
# gunzip / bunzip2

# zip is 1 step process
zip zipfilename.zip file1.txt fie2.txt file3.txt # create zip file # unzip

# gzip and bzip2 in 1 step
tar -cvzf filename.tar.gz # z: for gzip
tar -cvjf filename.tar.bz2 # j: for bzip2

tar -xvzf filename.tar.gz # z: for gzip
tar -xvjf filename.tar.bz2 # j: for bzip2

