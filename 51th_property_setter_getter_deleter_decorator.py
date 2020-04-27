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
