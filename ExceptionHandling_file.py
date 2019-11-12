class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post

        Person.__init__(self,name,idnumber)
    def display(self):
        print(self.name,self.post)

p=Person('Rahul',57613316)
p.display()
e=employee('Ganni',5363,300000,'hhdsgdj')
e.display()
