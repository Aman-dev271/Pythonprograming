class Employee:
    def __init__(self, name, sallary):
        self.name = name
        self.sallary = sallary
    def print_about_Employee(self):
        return f"The name of the Employee is {self.name} and the sallary of the employee is {self.sallary}"
# that is called Operator overloading
    def __add__(self , other):
        addition = self.sallary+other.sallary
        return f"{self.sallary}+{other.sallary} is {addition}"
    def __truediv__(self, other):
        return f"{self.sallary / other.sallary}"
    # to represent the object
    def __repr__(self):
        return f"Employee (name:-'{self.name}',sallary:-'{self.sallary}')"
    def __str__(self):
        return self.print_about_Employee()
aman = Employee("AMANDEEP", 100)
mandeep = Employee("MANDEEP", 3)
print(mandeep.sallary)
print(aman.sallary + mandeep.sallary)
print(aman  + mandeep)
print(aman / mandeep)
print(aman)
print(mandeep)
