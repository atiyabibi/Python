n=int(input())
arr=list(map(int,input().split()))
def equilibrium(arr):
    n=len(arr)
    for i in range(n):
        lsum=0
        rsum=0
        for j in range(i):
            lsum+=arr[j]
        for j in range(i+1,n):
            rsum+=arr[j]
        if lsum==rsum:
            return i 
    return -1

print(equilibrium(arr))

Input 1:
5
-5 2 6 -1 -2 

Output 1:
2

Input 2:
5
-5 2 6 1 -2 

Output 2:
-1


