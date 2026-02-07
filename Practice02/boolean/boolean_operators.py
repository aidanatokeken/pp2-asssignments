#1 example
a=0
b=1
c=True
d=False
print(a and b)   #False
#2 example
print(a or b)    #True
#3 example
print(not a)     #True
#4 example
if c is True:
    print("Good!")
else:
    print("Bad!")

#5 example
if not((a and b) or (c or d)):
    print("bool operators")
else:
    print("False")