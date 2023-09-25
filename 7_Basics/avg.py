# Writing Loops 2, part 2
# Danielle Arnett

total = 0
prompt = "Enter a real decimal number. "
for i in range(10):
    num = float(input(prompt))
    total += num
    print(total)
print("Average: ", total/10)
