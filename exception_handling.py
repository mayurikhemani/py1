# with error when we divide it by zero

'''
a,b=[int(a) for a in input("enter 2 number").split()]
c=a/b

print(c)
'''
#will make it to handle exception

try:
    a,b=[int(a) for a in input("enter 2 numbers").split()]
    c=a/b
    print("a/b= %d",c)
#except Exception:
 #   print("divide by 0 is invalid")
#or

except:
    print("this is divide by 0")

else:
    print("this is else block")


#3rd example

try:
    fileptr=open("fileExc.txt","r")
except IOError:
    print("file not found")
else:
    print("the file opened successfully")
    fileptr.close()


#4th
try:
    a=10/0
except ArithmeticError:    
    print ("Arithmetic Exception"   )
else:
    print("successfully done")



#5th

try:
    fileptr=open("file1.txt","w")
    try:
        fileptr.write("hey i am good")
    finally:
        fileptr.close()
        print("file is closed")
except:
    print("error")


#6th
try:
    age=int(input("enter age"))
    if age<18:
        raise ValueError;
    else:
        print("age is valid")
except ValueError:
    print("age is not valid")
        
#7th

try:  
    a = int(input("Enter a?"))  
    b = int(input("Enter b?"))  
    if b is 0:  
        raise ArithmeticError;  
    else:  
        print("a/b = ",a/b)  
except ArithmeticError:  
    print("The value of b can't be 0") 
