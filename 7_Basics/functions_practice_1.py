# Functions Practice 1
# Danielle Arnett

def main():
    print("Iterative Test Cases:")
    iterative_pyramid(char, longest_row)
    print()
    iterative_pyramid(char1, longest_row1)
    print()
    iterative_pyramid(char2, longest_row2)
    print()
    iterative_pyramid(char3, longest_row3)
    print()
    print('-' * 15)
    print("Recursive Test Cases")
    recursive_pyramid(char, start, longest_row)
    print()
    recursive_pyramid(char1, start, longest_row1)
    print()
    recursive_pyramid(char2, start, longest_row2)
    print()
    recursive_pyramid(char3, start, longest_row3)
    print()
    print('-' * 15)
    print("absolute_difference() test Cases")
    absolute_difference(first_num, second_num)
    print("^ Should be 20")
    print()
    absolute_difference(first_num1, second_num1)  #
    print("^ Should be 5")
    print()
    absolute_difference(first_num2, second_num2)
    print("^ Should be 5")
    print()
    absolute_difference(first_num3, second_num3)
    print("^ Should be 400")

# Problem 1.

# Iterative Solution
def iterative_pyramid(char, num):
    for i in range(num+1):
        print(char * i)

char = '^'
start = 1
longest_row = 6
char1 = '*'
longest_row1 = 5
char2 = 'x'
longest_row2 = 9
char3 = '+'
longest_row3 = 6

# print("Iterative Tests:")
# iterative_pyramid(char, longest_row)
# print()
# iterative_pyramid(char1, longest_row1)
# print()
# iterative_pyramid(char2, longest_row2)
# print()
# iterative_pyramid(char3, longest_row3)
# print()
# print('-' * 15)

# Recursive Solution
def recursive_pyramid(char, start, longest_row):
    if start == longest_row:
        return char * longest_row
    else:
        print(char * start)
        start += 1
        return recursive_pyramid(char, start, longest_row)

# print("Recursive Tests")
# recursive_pyramid(char, start, longest_row)
# print()
# recursive_pyramid(char1, start, longest_row1)
# print()
# recursive_pyramid(char2, start, longest_row2)
# print()
# recursive_pyramid(char3, start, longest_row3)
# print()


# Problem 2:

def absolute_difference(first_num, second_num):
    if first_num > second_num:
        return print(first_num - second_num)
    else:
        return print(second_num - first_num)

print("absolute_difference() test cases")
first_num = -10
second_num = 10

first_num1 = 5
second_num1 = 10

first_num2 = 10
second_num2 = 5

first_num3 = 200
second_num3 = -200

# absolute_difference(first_num, second_num)
# print("^ Should be 20")
# print()
#
# absolute_difference(first_num1, second_num1)  #
# print("^ Should be 5")
# print()
#
# absolute_difference(first_num2, second_num2)
# print("^ Should be 5")
# print()

# absolute_difference(first_num3, second_num3)
# print("^ Should be 400")

main()