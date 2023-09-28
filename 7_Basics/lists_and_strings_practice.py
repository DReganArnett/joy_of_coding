# Writing Lists & Strings Practice
# Danielle Arnett


def main():
    # 1. mean_of_20_nums()
    print("mean_of_20_nums() test cases: this function must be tested in real time")
    #mean_of_20_nums()

    print('-' * 30)

    # 2. mangle(string)
    print("mangle() test cases:")
    mangle(string)
    print("Test case 1 (danielle) should output 'DAIELE'")
    mangle(string)
    print()
    mangle(string1)
    print("Test case 2 (isaac) should output 'ISAC'")
    print()
    print("Test case 3 (timothy) should output 'TIOHY'")
    mangle(string2)
    print()
    print("Test case 4 (sean) should output 'SN'")
    mangle(string3)
    print()
    print("Test case 5 (ben) should output 'E'")
    mangle(string4)
    print()
    print("Test case 6 (al) should output 'AL'")
    mangle(string5)
    print()
    print("Test case 7 (alexandra) should output 'ALXANRA'")
    mangle(string6)
    print("Test case 8 (hellothere) should output 'HELOTHRE'")
    mangle(string7)
    print()
    print("Test case 9 (42 degrees Celsius) should output '42DEGREES CELSUS'")
    mangle(string8)
    print()
    print("Test case 10 (eeeeeee) should output 'eeeee'")
    mangle(string9)

    print('-' * 30)

    # 3. count_e(list)
    print("count_e(list) test cases:")
    print("Test case 1, ['hi', 'hello', 'EEK!'], should output 3")
    count_e(list)
    print()
    print("Test case 2, ['Danielle', 'and', 'SEAN', 'Arnett'], should output 4")
    count_e(list1)
    print()
    print("Test case 3, ['I love Python and Javascript'], should output 0")
    count_e(list2)
    print()
    print("Test case 4, ['Elephants', 'and', 'antelope', 'are', 'EXQUISITE!'], should output 7")
    count_e(list3)

    print('-' * 30)

    # 4. count_vowels(list)
    print("count_vowels(list) test cases:")
    print("Test case 1, ['hi', 'hello', 'OOF!'], should output 5")
    count_vowels(list4)
    print()
    print("Test case 2, ['hi', 'hello', 'EEK!'], should output 5")
    count_vowels(list)
    print()
    print("Test case 3, ['Danielle', 'and', 'SEAN', 'Arnett'], should output 9")
    count_vowels(list1)
    print()
    print("Test case 4, ['I love Python and Javascript'], should output 8")
    count_vowels(list2)
    print()
    print("Test case 4, ['Elephants', 'and', 'antelope', 'are', 'EXQUISITE!'], should output 15")
    count_vowels(list3)



# 1.
def mean_of_20_nums():
    prompt = "Enter a number. "
    numbers = []
    for i in range(20):
        num = eval(input(prompt))
        numbers.append(num)
    print("You entered: ", numbers)
    return print("Average = ", sum(numbers)/len(numbers))


# mean_of_20_nums()


#2.
# The solution below does not work with strings shorter than 5 characters in length

# def mangle(string):
#   string = string.upper()
#   string = string[0:2] + string[3:-3] + string[-2:]
#   return print(string)

def mangle(string):
    string = string.upper()
    string_list = []

    if len(string) < 3:
        return print(string)
    elif len(string) == 3:
        return print(string[1])
    elif len(string) == 4:
        return print(string[0] + string[3])
    else:
        for char in string:
            string_list.append(char)
    string_list_1 = string_list[:2]
    string_list_2 = string_list[3:-3]
    string_list_3 = string_list[-2:]
    string_list = string_list_1 + string_list_2 + string_list_3
    string = ''.join(string_list)
    return print(string)

string = 'danielle'
#mangle(string)
#print()
string1 = 'isaac'
#mangle(string1)
#print()
string2 = 'timothy'
#mangle(string2)
#print()
string3 = 'sean'
#mangle(string3)
#print()
string4 = 'ben'
#mangle(string4)
#print()
string5 = 'al'
#mangle(string5)
#print()
string6 = 'alexandra'
#mangle(string6)
#print()
string7 = 'hellothere'
#mangle(string7)
#print()
string8 = '42 degrees Celsius'
#mangle(string8)
#print()
string9 = 'eeeeeee'
#mangle(string9)


# 3.
def count_e(list):
    count = 0
    list_string = ''.join(list)
    for char in list_string:
        if char == 'e' or char == 'E':
            count +=1
    return print(count)

list = ["hi", "hello", "EEK!"]
#count_e(list)
#print()
list1 = ['Danielle', 'and', 'SEAN', 'Arnett']
#count_e(list1)
#print()
list2 = ['I love Python and Javascript']
#count_e(list2)
#print()
list3 = ['Elephants', 'and', 'antelope', 'are', 'EXQUISITE!']
#count_3(list3)


# 4.

def count_vowels(list):
    VOWELS = ['A','E','I','O','U']
    count = 0
    list_string = ' '.join(list).upper()
    print('list_string: ', list_string)
    for char in list_string:
        if char in VOWELS:
            count += 1
    return print(count)

list4 = ['hi', 'hello', 'OOF!']
#count_vowels(list4)
#print()


main()