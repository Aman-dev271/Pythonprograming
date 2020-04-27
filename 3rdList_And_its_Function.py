# list is a list of anything number char lists etc
grocery = ["harpic" , "vim bar" , "deodrant" ,"bhindi",
"lollypop" ,56,{"aman":"singh","katnoria":"singh"}]
print(grocery)

# to access the list items
print(grocery[2])
numbers = [20,13,40,15,46,70,18,19]
print(numbers[3])
# sorting changes the original list
print(numbers.sort())
print(numbers)
# reverse changes the original list
numbers.reverse()
print(numbers)
# slicing
print(numbers[0:2])
print(numbers[:5])
print(numbers[1:]) 

# extended slice
print(numbers [::1])
print(numbers[::3])
# to reverse the list
print(numbers[::-1])
# some functions
# it returns the maximum number from the list
print(max(numbers))
# it returns the least number from the list
print(min(numbers))
# to check the length of the list
print(len(numbers))
# append the list 
# it add the 10000 in the end of the list 
numbers.append(10000)
print(numbers)  
# insert function
# to insert any position in the list 
numbers.insert(3,567)
print(numbers)
# remove functions
# to remove th numbers
numbers.remove(10000)
print(numbers)
# pop function
numbers.pop(4)
print(numbers)
numbers[1] = 98
print(numbers)










# # to swap two numbes 
# a = 2
# b =4
# temp  = a
# a = b
# b = temp
# print(a,b)
# a  = 4
# b = 5
# a , b = b,a
# print(a,b)
# b = [1,2]
# numbers.copy()
# print(numbers)




