# Writing While Loops Practice
# Danielle Arnett

# 1a.

x = 1
while x < 6:
    print(x)
    x += 1
print()

#1b.

x = 2
while x < 12:
    print(x)
    x += 3
print()

# 1c.

x = -10
while x < 1:
    print(x, ' ', end='')
    x += 2
print()
print()


# 1d.

x = '****'
count = 1
while count < 5:
    print(x)
    count += 1
print()


# 2.
string = "CSCI 150"
index = 0
while index < len(string):
    print(string[index])
    index += 1
print()

# 3.

prompt = "Please enter a number.  Enter 0 to finish "
num_list = []
index = 0
number = eval(input(prompt))
while number != 0:
    num_list.append(number)
    number = eval(input(prompt))
print("Here are the numbers you entered, sorted in ascending order: ", sorted(num_list))
print("Here is the sum of the numbers you entered: ", sum(num_list))
print("Here is the average of the numbers you entered: ", sum(num_list)/len(num_list))
