class Employee:
    no_of_leaves = 23
    def __init__(self, name, contact_number, Age, Work_Experience):
        self.name = name
        self.contact_number = contact_number
        self.Age = Age
        self.Work_Experience = Work_Experience
    def Employee_details(self):
        print(f"Name of employee is {self.name} contact_number  of employee is  {self.contact_number} he/she is {self.Age} years old he/she  has {self.Work_Experience} years Work_Experience")
    @classmethod
    def no_of_leaves_per_Employee(cls, change_leaves):
        cls.no_of_leaves = change_leaves
        return f"The  total no of leaves for is {change_leaves}"
class programmer:
    def __init__(self, name, contact_number, Age, Work_Experience,  programming_Languages, About_Projects, Family_Background):
        self.name = name
        self.contact_number = contact_number
        self.Age = Age
        self.Work_Experience = Work_Experience
        self.programming_Languages = programming_Languages
        self.About_Projects = About_Projects
        self.Family_Background = Family_Background
    def print_prohrammer_details(self):
        print(f"The name of programmer is{self.name} contact_number  of employee is  {self.contact_number} he/she is {self.Age} years old he/she  has {self.Work_Experience},{self.name} has good unserstanding of {self.programming_Languages}  he made the Projects like {self.About_Projects} and about familiy backgroung of {self.name } is {self.Family_Background}")
class student:
    def __init__ (self, name, contact_number, Age,  programming_Languages, Student_Qualification, Year_Of_Passing):
        self.name = name
        self.contact_number = contact_number
        self.Age = Age
        self.programming_Languages = programming_Languages
        self.Student_Qualification = Student_Qualification
        self.Year_Of_Passing = Year_Of_Passing
    def students_get_hired(self):
        print(f"The sudent Name is{self.name} contact_number is {self.contact_number} age of candidate is {self.Age} he has good knowladge of {self.programming_Languages} Qualifinction of student is{self.Student_Qualification} and he is passed in the {self.Year_Of_Passing}")
# MUltiple inheritence programmer_Employee class get inherited from the three class
class programmer_Employee(Employee, programmer, student):
    print(end=" ")

# amandeep=Employee("amandeep",34567890, 12, "peogrammer")
# print(amandeep.Employee_details())
# print(amandeep.no_of_leaves_per_Employee(13))
# print(amandeep.no_of_leaves)
# print(Employee.no_of_leaves)
kalu = programmer_Employee("AmandeepSingh", 9872026957, 20, 2 ,["python","django","flask","HTML","CSS","JAVASCRIPT","Jquery","jquery Ui","django rest-framework"], ['e-commerce site','toor&travels','boombox'], {'father':'farmer','mother':'house-wife','brother':'photographer'})
print(kalu.Employee_details())
print(kalu.print_prohrammer_details())
# Amandeep = programmer_Employee("AmandeepSingh", 9872026957, 20,["python","django","flask","HTML","CSS","JAVASCRIPT","Jquery","jquery Ui","django rest-framework"],'B.Tech in computer science', 2020)
# Amandeep.students_get_hired()
