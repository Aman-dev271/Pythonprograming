class Employee():
    no_of_leaves = 4
    def __init__(self, aname, awork):
        self.name = aname
        self.work = awork

    def printdetails(self):
        return f"the name is {self.name} kaam is {self.work}"


aman = Employee("amandeep", "CEO OF Rs.120000000000000 millions compeny")
mani = Employee("mandeep" , "CEO OF Rs.12000000000000 millions compeny")
# aman.name = "amandeep"
# aman.work = "worker"
# mani.name = "mandeep"
# mani.work = "CEO OF Rs.12000000000000 millions compeny"
print(aman.work)