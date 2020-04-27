class Employee():
    no_of_leaves = 4
    def printdetails(self):
        return f"the name is {self.name} kaam is {self.work}"


aman = Employee()
mani = Employee()
aman.name = "amandeep"
aman.work = "worker"
mani.name = "mandeep"
mani.work = "CEO OF Rs.12000000000000 millions compeny"
print(mani.printdetails())