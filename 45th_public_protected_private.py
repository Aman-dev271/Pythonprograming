class publicprotectedprivate:
    var= 23
    name = "Amandeep"
    # these two variables are public variables that var anyone can acces
    _protec = "komal"
    # this is protected variable only class child can access these variable
    __private = "Amandeep"
    # this is an private variable only and only main class can acess these no child or other
class childclass(publicprotectedprivate):
    pass
print(childclass.var)
print(childclass._protec)
# the private variable only access by this token
print(publicprotectedprivate._publicprotectedprivate__private)
class outerclass:
    pass
# the var variable is defined as publically so that's outerclass can access var from publicprotectedprivate
print(publicprotectedprivate.var)
# __protec is protected var so thats why outer class cant access it only can accessible by the child or main class
print(publicprotectedprivate.__protec)
