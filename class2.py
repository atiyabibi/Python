#Online shpng giving input directly as list

class onlineshpng:
    def __init__(self,img,price,rating,comments):
        self.Image=img
        self.Price=price
        self.Rating=rating
        self.Comments=comments

c=["Very good","Excellent battery life"]
Laptop=onlineshpng("Pic 1", 46000 , 4.5,c)
print("When laptop is searched")
print(Laptop.Image)
print(Laptop.Price)
print(Laptop.Rating)
for c in Laptop.Comments:
    print(c)
print()

c=["This is Good","Nyc","WOrking properly"]
Mobile=onlineshpng("Pic 2",15000,3.9,c)
print("When mobile is searches")
print(Mobile.Image)
print(Mobile.Price)
print(Mobile.Rating)
for c in Mobile.Comments:
    print(c)
print()

c=["not Good","Poor quality","Low battery"]
SmartWatch=onlineshpng("Pic 3",5000,4.9,c)
print("When smart watch is searched ")
print(SmartWatch.Image)
print(SmartWatch.Price)
print(SmartWatch.Rating)
for c in SmartWatch.Comments:
    print(c)

Output

When laptop is searched
Pic 1
46000
4.5
Very good
Excellent battery life

When mobile is searches
Pic 2
15000
3.9
This is Good
Nyc
WOrking properly

When smart watch is searched 
Pic 3
5000
4.9
not Good
Poor quality
Low battery
