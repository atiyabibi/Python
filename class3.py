#Online shpng

class onlineshpng:
    def __init__(self,img,price,rating,comments):
        self.Image=img
        self.Price=price
        self.Rating=rating
        self.Comments=comments
Laptop=onlineshpng("Pic 1", 46000 , 4.5, list(input().split()))
print("When laptop is searched")
print(Laptop.Image)
print(Laptop.Price)
print(Laptop.Rating)
for c in Laptop.Comments:
    print(c)
print()
Mobile=onlineshpng("Pic 2",15000,3.9,list(input().split()))
print("When mobile is searches")
print(Mobile.Image)
print(Mobile.Price)
print(Mobile.Rating)
for c in Mobile.Comments:
    print(c)
print()
SmartWatch=onlineshpng("Pic 3",5000,4.9,list(input().split()))
print("When smart watch is searched ")
print(SmartWatch.Image)
print(SmartWatch.Price)
print(SmartWatch.Rating)
for c in SmartWatch.Comments:
    print(c)

Input:
Good Nyc Verygood
Poor Notgood Okay
VeryGood  Excellent

Output
When laptop is searched
Pic 1
46000
4.5
Good
Nyc
Verygood

When mobile is searches
Pic 2
15000
3.9
Poor
Notgood
Okay

When smart watch is searched 
Pic 3
5000
4.9
VeryGood
Excellent

