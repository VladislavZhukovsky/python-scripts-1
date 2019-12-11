#1 concat strings
def concatenate_strings():
    characters = ['p', 'y', 't', 'h', 'o', 'n']
    word = ''.join(characters)
    print(word)

#2 list comprehensions
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

#3 enumerations
def enumerate_list():
    numbers = [30, 42, 28, 50, 15]


    numbers1 = ['fuzzbuzz'
        if x % 5 == 0 and x % 3 == 0 
        else 'buzz' if x % 5 == 0
        else 'fuzz' if x % 3 == 0
        else x
        for x in numbers]

    for i, x in enumerate(numbers):
        if x % 5 == 0 and x % 3 == 0:
            numbers[i] = 'fuzzbuzz'
        elif x % 5 == 0:
            numbers[i] = 'buzz'
        elif x % 3 == 0:
            numbers[i] = 'fuzz'

    print(numbers)
    print(numbers1)

#1
#concatenate_strings()

#2
#list_comprehensions()
#list_comprehensions_1()

#3
enumerate_list()
