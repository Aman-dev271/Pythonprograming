list1 = []
list2 = []
dictionary = {}
set = set({})
print(type(set))

def make_comprihentions():
    # print("amandeep")

    want_input_for_comprihentions = int(input("Enter the number how much you want to make coprihentions"))
    what_we_want_to_do = input("what you want to make comprihentions for list press'1' for dictionary press '2' for set press '3' ")
    if what_we_want_to_do  == '1':
        for i in range(1, want_input_for_comprihentions+1):
            in_list = input(f"enter the value of {i} to the list")
            a = list1.append(in_list)
        print(list1)
        print("comprihension for list is :-[ i for i in range(list1)]")
    elif what_we_want_to_do  == '2':
        for i in range(1, want_input_for_comprihentions+1):
            in_dict = input(f"enter the value of {i} to the dictionary")
            a = list1.append(in_dict)
            b = list2.append(i)
        dictionary = dict(zip(list2, list1))
        print(dictionary)
        print(type(dictionary))
        print("comprihension for dictionary is :-{i:f'Item{i}'' for i in range(30) if i%2==0 }")
    elif what_we_want_to_do == '3':
        for i in range(1, want_input_for_comprihentions+1):
            in_list = input(f"enter the value of {i} to the set")
            set.add(in_list)
        print(set)
        print(type(set))
        print('comprihension for set is :-{dress for dress in ["dress1", "dress1","dress2","dress2"]}')
input_for_funcion = int(input(f"press {1} for cotinue process other wise {3}"))

while input_for_funcion < 4:
    make_comprihentions()
    input_for_funcion +=1
