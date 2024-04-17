password=2387
n=3
ac=3
while n>=1:
    key=int(input())
    if key==password:
        print("Successfully logged in")
        break
    else:
        if ac==1:
            print("Your account got blocked try after 24 hours")
        else:
            print("Incorrect password you are left with",n-1,"attempts")
        ac=ac-1
    n=n-1

Input
1
2
3
Output
Incorrect password you are left with 2 attempts
Incorrect password you are left with 1 attempts
Your account got blocked try after 24 hours

Input
1
2
2387
Output
Incorrect password you are left with 2 attempts
Incorrect password you are left with 1 attempts
Successfully logged in
