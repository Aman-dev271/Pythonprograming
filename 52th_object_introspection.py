class Employee:
    def __init__(self,F_name, L_name):
        self.F_name = F_name
        self.L_name = L_name

    def print_details(self):
        return f"The first_name is {self.F_name} and last name is {self.L_name}"
    @classmethod
    def form_string(cls,string):
        return cls(*string.split(","))
    @property
    def email(self):
        if self.F_name == None or self.L_name == None:
            print("plese set the email by setter")
        else:
            print(f"email is{self.F_name}.{self.L_name}@gmail.com ")
    # setter to set the attribute
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.F_name = names.split(".")[0]
        self.L_name = names.split(".")[1]
    # deleter to delete the eamil
    @email.deleter
    def email(self):
        self.F_name = None
        self.L_name = None



aman = Employee.form_string("Amandeep,singh")
# print(aman.email)
aman.F_name = "Mandeep"
# print(aman.email)
print(aman.F_name)
print(aman.email)
# if wan to change the email like f_name we chnaged
# a = aman.email =" amandeep.singh@gmail.com"
# print(a)
# it that way we cannot change we have to apply the setter property or decorator to set the attribute
#    a = aman.email =" amandeep.singh@gmail.com"
# AttributeError: can't set attribute
# we get this is type of error
# to solve it we have to create the setter classmethod

a = aman.email =" amandeep.singh@gmail.com"
print(a)
del aman.email
print(aman.email)
import inspect
print(inspect.getmembers(aman))
# outut is

# [('F_name', None), ('L_name', None), ('__class__', <class '__main__.Employee'>), ('__delattr__', <method-wrapper '__delattr__' of Employee object at 0x01945850>), ('__dict__', {'F_name': None, 'L_name': None}), ('__dir__', <built-in method __dir__ of Employee object at 0x01945850>), ('__doc__', None), ('__eq__', <method-wrapper '__eq__' of Employee object at 0x01945850>), ('__format__', <built-in method __format__ of Employee object at 0x01945850>), ('__ge__', <method-wrapper '__ge__' of Employee object at 0x01945850>), ('__getattribute__', <method-wrapper '__getattribute__' of Employee object at 0x01945850>), ('__gt__', <method-wrapper '__gt__' of Employee object at 0x01945850>), ('__hash__', <method-wrapper '__hash__' of Employee object at 0x01945850>), ('__init__', <bound method Employee.__init__ of <__main__.Employee object at 0x01945850>>), ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x0194B030>), ('__le__', <method-wrapper '__le__' of Employee object at 0x01945850>), ('__lt__', <method-wrapper '__lt__' of Employee object at 0x01945850>), ('__module__', '__main__'), ('__ne__', <method-wrapper '__ne__' of Employee object at 0x01945850>), ('__new__', <built-in method __new__ of type object at 0x6CE18140>), ('__reduce__', <built-in method __reduce__ of Employee object at 0x01945850>), ('__reduce_ex__', <built-in method __reduce_ex__ of Employee object at 0x01945850>), ('__repr__', <method-wrapper '__repr__' of Employee object at 0x01945850>), ('__setattr__', <method-wrapper '__setattr__' of Employee object at 0x01945850>), ('__sizeof__', <built-in method __sizeof__ of Employee object at 0x01945850>), ('__str__', <method-wrapper '__str__' of Employee object at 0x01945850>), ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x0194B030>), ('__weakref__', None), ('email', None), ('form_string', <bound method Employee.form_string of <class '__main__.Employee'>>), ('print_details', <bound method Employee.print_details of <__main__.Employee object at 0x01945850>>)


# the mean of intrspection of object is know the type and know where it comes and about that AttributeErro
# print(type(aman))

# output is <class '__main__.Employee'>
print(dir(aman))
print(id("i am amandeep"))
