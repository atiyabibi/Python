class onlineshpng:
    def __init__(self,img,b,price,rating,comments):
        self.Name=img
        self.Price=price
        self.Brand=b
        self.Rating=rating
        self.Comments=comments
    def printall(self):
        print("Product name is :",self.Name)
        print("Product brand is :",self.Brand)
        print("Product price is :",self.Price)
        print("Product Rating is :",self.Rating)
        print("Product comments are :",self.Comments)
    
c=["Very good","Excellent battery life"]
Laptop=onlineshpng("Laptop","Lenovo",46000 , 4.5,c)
print("When laptop is searched")
Laptop.printall()

c=["This is Good","Nyc","Working properly"]
Mobile=onlineshpng("Mobile","Samsumg",15000,3.9,c)
print("When mobile is searched")
Mobile.printall()

c=["not Good","Poor quality"]
SmartWatch=onlineshpng("Smart Watch","Boat",5000,4.9,c)
print("When smart watch is searched ")
SmartWatch.printall()

Output
When laptop is searched
Product name is : Laptop
Product brand is : Lenovo
Product price is : 46000
Product Rating is : 4.5
Product comments are : ['Very good', 'Excellent battery life']
When mobile is searched
Product name is : Mobile
Product brand is : Samsumg
Product price is : 15000
Product Rating is : 3.9
Product comments are : ['This is Good', 'Nyc', 'Working properly']
When smart watch is searched 
Product name is : Smart Watch
Product brand is : Boat
Product price is : 5000
Product Rating is : 4.9
Product comments are : ['not Good', 'Poor quality']
