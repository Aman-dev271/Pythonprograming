# pickle module is a module that allow us to store the objects in the program and store where we want
import pickle
# to make the file as pickle
# car = {'kali', 'peeli', 'nilee', 'chitti'}
# file = "carfile.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(car, fileobj)
# fileobj.close()



# to read the pickle file
file = "carfile.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(type(mycar))
print(mycar)
