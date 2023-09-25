# Writing Loops 2, part 1
# Danielle Arnett

# 1
for i in range(10, 26, 5):
    print(i, end=" ")
print()

# 2
for i in range(-3, 21, 3):
    print(i, end=", ")
print(21)
print()

# 3 - avg.py
total = 0
prompt = "Enter a real decimal number. "
for i in range(10):
    num = float(input(prompt))
    total += num
    print(total)
print("Average: ", total/10)




