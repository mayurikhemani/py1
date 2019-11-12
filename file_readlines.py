#reading lines---

fileptr=open("file1.txt","r")
content=fileptr.readline();
print(content)

#to read multiple lines in file

for i in fileptr:
      print(i)

fileptr.close()
