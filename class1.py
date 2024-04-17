class Box:
    def __init__(self,name,rn,osmarks,javamarks,dsmarks):
        self.Name=name
        self.RollNumber=rn
        self.OSMarks=osmarks
        self.JavaMarks=javamarks
        self.DSMarks=dsmarks

s1=Box("HI",56,88,99,50)
print(s1.Name)
print(s1.RollNumber)
print(s1.OSMarks)

Output
HI
56
88
