class Gran_Father:
    def __init__(self, dance, hocky, basktball):
        self.dance = dance
        self.hocky = hocky
        self.backtball = basktball
    def Grand_Ability(self):
        print(f"The Gran_Father  can {self.dance} and he can play {self.hocky} he als can play {self.backtball}")
class Father(Gran_Father):
    # here i oberright the Gran_Father class
    def Grand_Ability(self):

        print(f"The Father  can {self.dance} and he can play {self.hocky} he als can play {self.backtball}")
    # def __init__(self,Face_color, property):
    #     self.Face_color = Face_color
    #     self.property = property
    # def Father_Dtails(self):
    #     print(f"the face color of {self.name} is {self.Face_color} and he has property {self.property}$")

class Son(Father):
    # def Father_Dtails(self):
    #     print(f"the face of son  is {self.Face_color} and he has property {self.property}$")
    print(end="")

mandeep = Son("nhamgra","hocky","basktball")
mandeep.Grand_Ability()
