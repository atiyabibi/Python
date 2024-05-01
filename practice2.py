n=int(input())
arr=list(map(int,input().split()))
d=int(input())
temp=[]
n=len(arr)
for i in range(d,n):
    temp.append(arr[i])
for i in range(d):
    temp.append(arr[i])
for i in range(n):
    arr[i]=temp[i]
print(arr)

Input:
7
1 2 3 4 5 6 7
2 
Output
[3, 4, 5, 6, 7, 1, 2]


