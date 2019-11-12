try:
    fileptr=open("fileExc.txt","r")
except IOError:
    print("file not found")
else:
    print("the file opened successfully")
    fileptr.close()
