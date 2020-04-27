class maincls:
    classvar1 = "I am a class variable dear"
    def __init__(self):
        self.var = "i am A instance variable of class maincls"
        self.classvar1 = "I am B instance variable od class maincls"
        self.super = "i am special charactor"
class basecls(maincls):
    # here it overrite the classvar1 of maincls
    classvar1 = "i am inside the class basecls"
    def __init__(self):
        # if i want to inherit constructor also and dont overrite it the we use the super()
        # super().__init__()
        # if i wrote it here then first priority is basecls
        self.var = "i am b instance variable of class basecls"
        self.classvar1 = "I am b instance variable od basecls"
        super().__init__()
        # if i wrote it here then it change its working



a = maincls()
b = basecls()
print(b.classvar1)
# this first search the instance variable name:classvar1 first in base class if not the second
print(b.super)
# it does not work becasuse be oversite the the contructor of class maincls thats why now the contructor of maincls is useless
# if we want to run both the contructor as we need the we have super()that makes this functionality
print(b.classvar1,'\n',b.var,'\n',b.super)
