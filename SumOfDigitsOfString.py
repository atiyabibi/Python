str=input()
def SumOfDigitsOnString(str):
    sum=0
    for i in range(0,len(str)):
        if str[i].isdigit():
            sum+=int(str[i])
    return sum
print(SumOfDigitsOnString(str))

******************************************************************************************************************

str1=input()
def findSum(str1):
    temp = "0"
    Sum = 0
    for ch in str1:
        if (ch.isdigit()):
            temp += ch
        else:
            Sum += int(temp)
            temp = "0"
    return Sum + int(temp) 

print(findSum(str1))
