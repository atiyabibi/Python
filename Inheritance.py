#Inheritance

#1st program
#single inheritance
class Box:
    def __init__(self,name,roll):
        self.name=name
        self.rollnumber=roll
    def printall(self):
        print("Name:",self.name)
        print("RollNumber:",self.rollnumber)
        print("Marks:",self.marks)

class student(Box):
    def __init__(self,name,roll,marks):
        self.marks=marks
        Box.__init__(self,name,roll)
        Box.printall(self)

ob1=student("Raj",9,88)

Output
Name: Raj
RollNumber: 9
Marks: 88

#2nd program
class Box:
    def __init__(self,name,roll):
        self.name=name
        self.rollnumber=roll
    def printall(self):
        print("Name:",self.name)
        print("RollNumber:",self.rollnumber)
        print("Marks:",self.marks)
        print("Fees:",self.fees)

class student:
    def __init__(self,marks):
        self.marks=marks

class Box2(Box,student):
    def __init__(self,name,roll,marks,fees):
        self.fees=fees
        student.__init__(self,marks)
        Box.__init__(self,name,roll)
        Box.printall(self)

ob1=Box2("Raj",8,98,20000)

Output
Name: Raj
RollNumber: 8
Marks: 98
Fees: 20000

#3rd program
#Multilevel 
class Box:
    def __init__(self,name,roll):
        self.name=name
        self.rollnumber=roll
    def printall(self):
        print("Name:",self.name)
        print("RollNumber:",self.rollnumber)
        print("Marks:",self.marks)
        print("Fees:",self.fees)
       
class student:
    def __init__(self,marks):
        self.marks=marks

class Box2(Box,student):
    def __init__(self,name,roll,marks,fees):
        self.fees=fees
        student.__init__(self,marks)
        Box.__init__(self,name,roll)
        Box.printall(self)

class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"R",6,55,10000)

obj=Box3("2-1")
print(obj.sem)

obj2=Box2("S",12,23,200000)

obj3=Box2("R",45,88,50000)

Output
Name: R
RollNumber: 6
Marks: 55
Fees: 10000
2-1
Name: S
RollNumber: 12
Marks: 23
Fees: 200000
Name: R
RollNumber: 45
Marks: 88
Fees: 50000



#4th program
#Multiple
class Box:
    def __init__(self,name,roll):
        self.name=name
        self.rollnumber=roll
    def printall(self):
        print("Name:",self.name)
        print("RollNumber:",self.rollnumber)
        print("Marks:",self.marks)
        print("Fees:",self.fees)
       
class student:
    def __init__(self,marks):
        self.marks=marks

class Box2(Box,student):
    def __init__(self,name,roll,marks,fees):
        self.fees=fees
        student.__init__(self,marks)
        Box.__init__(self,name,roll)
        Box.printall(self)

class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"R",6,55,10000)

class Box4(Box2):
    def __init__(self,usn):
        self.usn=usn
        Box2.__init__(self,"A",4,99,20000)

ob1=Box4("3br2162")
print("USN:",ob1.usn)
obj=Box3("2-1")
print("SEM:",obj.sem)
obj2=Box2("S",12,23,200000)
obj3=Box2("R",45,88,50000)

Output
Name: A
RollNumber: 4
Marks: 99
Fees: 20000
USN: 3br2162
Name: R
RollNumber: 6
Marks: 55
Fees: 10000
SEM: 2-1
Name: S
RollNumber: 12
Marks: 23
Fees: 200000
Name: R
RollNumber: 45
Marks: 88
Fees: 50000

