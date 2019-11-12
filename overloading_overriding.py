#===================overloading

# First product method. 
# Takes two argument and print their 
# product 
def product(a, b): 
    p = a * b 
    print(p) 
      
# Second product method 
# Takes thre argument and print their 
# product 
def product(a, b, c): 
    p = a * b*c 
    print(p) 
  
# Uncommenting the below line shows an error     
#product(4, 5)
  
# This line will call the second product method 
product(4, 5, 5)
#==============overloading workaround
# Function to take multiple arguments 
def add(datatype, *args): 
  
    # if datatype is int 
    # initialize answer as 0 
    if datatype =='int': 
        answer = 0
          
    # if datatype is str 
    # initialize answer as '' 
    if datatype =='str': 
        answer ='' 
  
    # Traverse through the arguments 
    for x in args: 
  
        # This will do addition if the  
        # arguments are int. Or concatenation  
        # if the arguments are str 
        answer = answer + x 
  
    print(answer) 
  
# Integer 
add('int', 5, 6) 
  
# String 
add('str', 'Hi ', 'Geeks') 
#================overriding

class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1


c=Child()
print(c.get_value())
