class Employee():
    no_of_leaves = 4
    def __init__(self, aname, awork):
        self.name = aname
        self.work = awork

    def printdetails(self):
        return f"the name is {self.name} kaam is {self.work}"
    # this is a class method that is called class decorator and by this we  can acsses the main class variables change also
    # it changes the main class variables
    # The cls mean to Employee (class)
    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves
    @classmethod
    def form_string(cls, string):
        # params = string.split(",")
        # return cls(params[0], params[1])
        return cls(*string.split(","))
    @staticmethod
    def print_good_name(string):
        print("This is our html page"+' '+string)





aman = Employee("amandeep", "CEO OF Rs.120000000000000 millions compeny")
mani = Employee("mandeep" , "CEO OF Rs.12000000000000 millions compeny")
hardeep =Employee.form_string("Hardeepsingh,12000000")

print(hardeep.no_of_leaves)
print(mani.no_of_leaves)
Employee.print_good_name("anandeep")
print(hardeep.printdetails())
