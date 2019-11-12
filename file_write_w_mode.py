#file writing in write mode

fileptr=open("file2.txt","w")
#initial code
fileptr.write("new file in w mode which will overwrite the previous data")
#again rewrite the file
fileptr.write(" file in w mode which will overwrite the previous data1")
fileptr.close()

#right now file doesn't exisit" for fileptr=open("file3.txt","w")
