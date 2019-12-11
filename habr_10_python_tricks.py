#1 concat strings
def concatenate_strings():
    characters = ['p', 'y', 't', 'h', 'o', 'n']
    word = ''.join(characters)
    print(word)

#list comprehensions
def list_comprehensions():
    r = range(5)
    m = [x ** 2 for x in r]
    print(type(m))
    print(m)

def list_comprehensions_1():
    #find numbers in both lists
    a = [1,2,3,4]
    b = [2,3,4,5]
    common_num = [x for x in a for y in b if x == y]
    print(common_num)


#1
#concatenate_strings()

#2
#list_comprehensions()
list_comprehensions_1()

#3
