from P0 import Seq0
FOLDER = './sequences/' #only a dot means that that folder is inside the folder we are coding on, two dots mean a previoys folder and so on
ID = 'U5.txt'
U5_Seq = Seq0.seq_read_fasta(FOLDER + ID) #erases the first line of code

print('The first 20 bases are: ', U5_Seq[0:20])

#inside the wiki (P0) there is the explanation for ../folder or ./folder