#Exceptions

#1st program
print("starting line")
try:
    a=10/0
except:
    print("Some exception rised")


#2nd program
print("starting line")
try:
    a=10/5
except:
    print("Some exception rised")
else:
    print("no exception")
print("Outside try block")

#3rd program
print("starting line")
try:
    a=10/5
except:
    print("Some exception rised")
else:
    print("no exception")
finally:
    print("This will be executed")
print("Outside try block")


#4th program
print("starting line")
a=[22,33,44,55]
try:
    a=10/5
    a[5]
    print(y)
    print("This is in try block")
except:
    print("Some exception rised")
else:
    print("no exception")
finally:
    print("This will be executed")
print("Outside try block")

Output
starting line
Some exception rised
This will be executed
Outside try block


#5th program
print("starting line")
a=[22,33,44,55]
try:
    b=10/5
    a[3]
    print(a)
    print("This is in try block")
except:
    print("Some exception rised")
else:
    print("no exception")
finally:
    print("This will be executed")
print("Outside try block")

Output
starting line
[22, 33, 44, 55]
This is in try block
no exception
This will be executed
Outside try block

#Multiple except statements
#6th program
print("Starting")
c=[26,24,23]
try:
    a=10/5
    b=c[1]
    print(y)
    print("This is in try block")
except ZeroDivisionError:
    print("Exception due to division by zero")
except IndexError:
    print("Exception due to list index out of range")
except NameError:
    print("Exception due to undefined variable")
except:
    print("Some exception raised")
else:
    print("No exceeption")
finally:
    print("This is a final block")
print("Outside try block")

Output
Starting
Exception due to undefined variable
This is a final block
Outside try block

#7th program
#Nested try block

print("Starting")
c=[26,24,23]
try:
    try:
        b=20/0
    except:
        print("Nested try")
    a=10/5
    b=c[5]
    print(z)
    print("This is in try block")
except ZeroDivisionError:
    print("Exception due to division by zero")
except IndexError:
    print("Exception due to list index out of range")
except NameError:
    print("Exception due to undefined variable")
except:
    print("Some exception raised")
else:
    print("No exceeption")
finally:
    print("This is a final block")
print("Outside try block")

Output
Starting
Nested try
Exception due to list index out of range
This is a final block
Outside try block

#8th program
print("Starting")
c=[26,24,23]
try:
    try:
        b=20/5
        try:
            d=c[6]
        except:
            print("Try block inside another try block")
    except:
        print("Nested try")
    a=10/0
    b=c[1]
    print(b)
    print("This is in try block")
except ZeroDivisionError:
    print("Exception due to division by zero")
except IndexError:
    print("Exception due to list index out of range")
except NameError:
    print("Exception due to undefined variable")
except:
    print("Some exception raised")
else:
    print("No exceeption")
finally:
    print("This is a final block")
print("Outside try block")

Output
Starting
Try block inside another try block
Exception due to division by zero
This is a final block
Outside try block


#9th program
#raising exception explicitly

print("Starting")
c=[26,24,23]
try:
    a=10/5
    b=c[1]
    print(b)
    raise IndexError
    print("This is in try block")
except ZeroDivisionError:
    print("Exception due to division by zero")
except IndexError:
    print("Exception due to list index out of range")
except NameError:
    print("Exception due to undefined variable")
except:
    print("Some exception raised")
else:
    print("No exceeption")
finally:
    print("This is a final block")
print("Outside try block")

Output
Starting
24
Exception due to list index out of range
This is a final block
Outside try block
