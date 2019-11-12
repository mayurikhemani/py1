a=10
b=0
try:
    print(a/b)
except Exception:
    print("invalid division")


#### 2nd

try:
    global i
    i=int(input("Enter number between 0-12"))
    print(i)
except ValueError:
    print("you haven't entered number")

#######3rd
a=[1,2,4]
try:
    print("second value= %d" %(a[1]))
    print("second value= %d" %a[3])
except IndexError:
    print("an index error occurred")


######4h
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b =",b)
except(ZeroDivisionError,NameError):
    print("\n error occured and handled")
else:
    print(b)

##########6th
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

##############5th
'''
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise
finally:
    print("the finally will always work")
'''
#raise an exception if variable type is nnot int

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

###### 6th

try:  
    a = int(input("Enter a?"))  
    b = int(input("Enter b?"))  
    if b is 0:  
        raise ArithmeticError;  
    else:  
        print("a/b = ",a/b)  
except ArithmeticError:  
    print("The value of b can't be 0") 
    
 
 #7th 
 try:
    age=int(input("enter age"))
    if age<18:
        raise ValueError;
    else:
        print("age is valid")
except ValueError:
    print("age is not valid")
