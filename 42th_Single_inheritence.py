class Employee:
    no_of_employee = 23
    def __init__(self,name , work , sallary):
        self.name = name
        self.work = work
        self.sallary = sallary
    def Detail_function(self):
        print(f"The name of Employee{self.name} and work is {self.work} and sallary is {self.sallary}")
# Single inheritence is that method which one class is inherits from the others
class programmer(Employee):
    def __init__(self,name , work , sallary, contact_number):
        self.name = name
        self.work = work
        self.sallary = sallary
        self.contact_number = contact_number
    def programmers_Details(self):
        print(f"The name of programmer is {self.name} and work is {self.work} and sallary  is {self.sallary} the contact number is {self.contact_number}")

mandeep = Employee("Mandeep", "manager" , 200000000000)
Amandeep = programmer("AmandeepSingh", "Programmer", 200000000000 , 9872026957)
# th programmer class is child and Employee class is our parant class so we can access all the functuions of parant classesby the uses of child class but childs function cannot access by teh parent class
Amandeep.Detail_function()
# mandeep.programmers_Details()
Amandeep.programmers_Details()
print(programmer.no_of_employee)
