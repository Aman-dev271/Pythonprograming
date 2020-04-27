class Employee():
    no_of_leaves = 1000
    pass


aman = Employee()
mani = Employee()
aman.name = "amandeep"
aman.role ="project manager"
mani.name = "Mandeep"
mani.role ="Ceo"
print(mani.no_of_leaves)
print(mani.__dict__)
mani.no_of_leaves = 12
print(mani.__dict__)
# the class instance (mani,aman)can't change the value no_of_leaves from the original class
Employee.no_of_leaves = 20
print(Employee.__dict__)
# only that can change the employee class value