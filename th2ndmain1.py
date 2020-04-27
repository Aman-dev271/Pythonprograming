def printhar(string):
    return f"ye string haary ko de dobi{string}"
def add(num1,num2):
    return num1+num2 +5
print("and the name is ",__name__)
if __name__ == '__main__':
    print(printhar("l=kaludeep"))
    print(add(30,40))
# if we use:-print("and the name is ",__name__)
            # if __name__ == '__main__':

# then output is:-and the name is  th2ndmain1
                    # ye string haary ko de dobiamandeepsingh
                    # 10
# if we dont use these decorator or keywrd:-print("and the name is ",__name__)
                                            # if __name__ == '__main__':
    # then the out put is:-ye string haary ko de dobil=kaludeep
                            # 75
                            # ye string haary ko de dobiamandeepsingh
                            # 10
