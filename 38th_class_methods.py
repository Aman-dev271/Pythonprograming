class Employee():
    no_of_leaves = 4
    def __init__(self, aname, awork):
        self.name = aname
        self.work = awork

    def printdetails(self):
        return f"the name is {self.name} kaam is {self.work}"
    # this is a class method that is called class decorator and by this we  can acsses the main class variables change also 
    # it changes the main class variables 
    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves



aman = Employee("amandeep", "CEO OF Rs.120000000000000 millions compeny")
mani = Employee("mandeep" , "CEO OF Rs.12000000000000 millions compeny")
# aman.name = "amandeep"
# aman.work = "worker"
# mani.name = "mandeep"
# mani.work = "CEO OF Rs.12000000000000 millions compeny"
aman.change_leaves(34)
print(aman.no_of_leaves)
print(mani.no_of_leaves)
print(Employee.no_of_leaves)