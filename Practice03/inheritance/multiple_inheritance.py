#1
class A:
    def a_method(self):
        print("Method A")

class B:
    def b_method(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.a_method()
c.b_method()

#2
class A:
    def say(self):
        print("Hello from A")

class B:
    def say(self):
        print("Hello from B")

class C(A, B):
    def say(self):
        print("Hello from C")

c = C()
c.say()

#3
class A:
    def greet(self):
        print("Hi from A")

class B:
    def greet(self):
        print("Hi from B")

class C(A, B):
    def greet(self):
        A.greet(self)
        B.greet(self)
        print("Hi from C")

c = C()
c.greet()

#4
class A:
    def __init__(self):
        print("Init A")

class B:
    def __init__(self):
        print("Init B")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Init C")

c = C()

#5
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        super().method()
        print("B method")

class C(A):
    def method(self):
        super().method()
        print("C method")

class D(B, C):
    def method(self):
        super().method()
        print("D method")

d = D()
d.method()
