#1 example

a=0    #int
b=3.5  #float
c=5j   #complex

#2 example

a = 10
b = 1234567890
c = -9876543211234567890
print(type(a)) #<class 'int'>
print(type(b)) #<class 'int'>
print(type(c)) #<class 'int'>

#3 example

a=0.5
b=3.14134567892345678
c= -96.7
print(type(a)) #<class 'float'>
print(type(b)) #<class 'float'>
print(type(c)) #<class 'float'>

#4 example
a=3+5j
y= -2j
z=4+0j

print(type(a)) #<class 'complex'>
print(type(b)) #<class 'complex'>
print(type(c)) #<class 'complex'>

#5 example
x=1    #int
y=5.6  #float

a=float(x)   #int -> float
b=int(y)     #float -> int
c=complex(x) #int -> complex

print(type(a)) #<class 'float'>
print(type(b)) #<class 'int'>
print(type(c)) #<class 'complex'>