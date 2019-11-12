"""fileptr=open("file1.txt","r")
if fileptr:
    print("file is opened successfully in read mode")

fileptr=open("file1.txt","w")
if fileptr:
    print("file is opened successfully in write mode")

fileptr=open("file1.txt","a")
if fileptr:
    print("file is opened successfully in append mode")
 """   



#read number of content


fileptr=open("file1.txt","r")
content= fileptr.read(100);
#readline or readlines
print(type(content))
print(content)

fileptr.close()
