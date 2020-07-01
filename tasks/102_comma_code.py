list1 = ['apples', 'banana', 'tofu', 'cats']
list2 = [0, 1, 2, 3, 4, 5]
list3 = [*range(1, 101, 2)]
def ListCreator(list):
    print("List contains: ", end='')
    for i in list:
        x = len(list)
        y = list.index(i)
        if x-1 == y:
            print(i, end='. \n')
        elif x-2 == y:
            print(i, end=" and ")
        else:
            print(i, end=", ")

ListCreator(list1)
ListCreator(list2)
ListCreator(list3)
