# diamond shape problem is nothing but a multiple inheritence confusion structure lets see how we can deal with that problem
class A:
    def details(self):
        print("you are in the class A")
class B(A):
    def details(self):
        print("you are in the class B")
class C(A):
    def details(self):
        print("you are in the class C")
class D(B, C):
    def details(self):
        print("you are in the class D")
a = A()
b = B()
c = C()
d = D()
d.details()
# that is the diamond problem it does not a problem in python but it matterr in java C++ thats why the dont allow to use this
