# Functions Practice 2
# Danielle Arnett

def main():
    print("is_even() test cases")
    print("2 is even: ")
    is_even(2)
    print("3 is even: ")
    is_even(3)
    print("104 is even: ")
    is_even(104)
    print("3333 is even: ")
    is_even(3333)
    print('-' * 15)
    print("calculate_total() test cases")
    calculate_total(meal, tax_rate, tip_rate)
    print()
    calculate_total(meal1, tax_rate1, tip_rate1)
    print()
    calculate_total(meal2, tax_rate2, tip_rate2)
    print('-' * 15)
    print("hey() test cases")
    hey(num)
    print()
    hey(num1)
    print()
    hey(num2)
    print()
    hey(num3)
    print('-' * 15)
    print("there() test cases")
    there(n)
    print()
    there(n1)
    print()
    there(n2)
    print()
    there(n3)
    print()
    there(n4)
    print()
    print('-' * 15)
    print("are_we() test cases")
    are_we(num_repeats, phrase)
    print()
    are_we(num_repeats1, phrase1)
    print()
    are_we(num_repeats2, phrase2)
    print()
    are_we(num_repeats3, phrase3)
    print()

# Problem 4
def is_even(num):
    if num % 2 == 0:
        return print(True)
    else:
        return print(False)

# print("is_even() test cases")
# print("2 is even: ")
# is_even(2)
# print("3 is even: ")
# is_even(3)
# print("104 is even: ")
# is_even(104)
# print("3333 is even: ")
# is_even(3333)


# Problem 5

def calculate_total(meal, tax_rate, tip_rate):
    print('meal: $', meal)
    tax = meal * tax_rate
    print('tax: $', tax)
    tip = meal * tip_rate
    print('tip: $', tip)
    total = meal + tax + tip
    return print("total: $", total)

meal = 53.48
tax_rate = 0.07
tip_rate = 0.18
# calculate_total(meal, tax_rate, tip_rate)

meal1 = 100.00
tax_rate1 = 0.07
tip_rate1 = 0.20
# calculate_total(meal1, tax_rate1, tip_rate1)

meal2 = 50.00
tax_rate2 = 0.07
tip_rate2 = 0.25
# calculate_total(meal2, tax_rate2, tip_rate2)


# Problem 6

def hey(num):
    output = num * num
    return print(num, 'squared equals', output)

num = 5
num1 = 0
num2 = -3
num3 = 10
# print("hey() Test Cases")
# hey(num)
# print()
# hey(num1)
# print()
# hey(num2)
# print()
# hey(num3)


# Problem 7

def there(n):
    if n >= 0:
        output = 2 ** n
        return print("2 to the ", n, "th power equals", output)
    else:
        output = 0
        return print("Since ", n, "is a negative number, ", "the output is ", output)

n = 5
n1 = 0
n2 = 3
n3 = -2
n4 = -6
# print("there() test cases")
# there(n)
# print()
# there(n1)
# print()
# there(n2)
# print()
# there(n3)
# print()
# there(n4)
# print()


# Problem 8

def are_we(num_repeats, phrase):
    part1 = "Are we "
    part2 = phrase
    part3 = " yet? "
    whole_phrase = part1 + part2 + part3
    return print(whole_phrase * num_repeats)

print("are_we() test cases")
num_repeats = 2
phrase = "there"
#are_we(num_repeats, phrase)

num_repeats1 = 3
phrase1 = "50"
#are_we(num_repeats1, phrase1)

num_repeats2 = 1
phrase2 = ""
#are_we(num_repeats2, phrase2)

num_repeats3 = 0
phrase3 = "hey"
#are_we(num_repeats3, phrase3)


main()
