fileptr=open("file1.txt","a")

fileptr.write("keep updating in file")

fileptr.close()

fileptr=open("file1.txt","r")
for i in fileptr:
    print(i)

fileptr.close()

