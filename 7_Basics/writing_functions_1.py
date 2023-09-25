# Writing Functions 1
# Danielle Arnett

def main():
    print("If we add your two numbers, we get ", add(x, y), ". ", "If we multiply your two numbers, we get ",
          multiply(x, y), ".")

# 1.

def add(x,y):
    return x+y


# 2.

def multiply(x,y):
    return x*y


# 3.
prompt_1 = "Enter a number. "
prompt_2 = "Enter another number. "
x = eval(input(prompt_1))
y = eval(input(prompt_2))

add(x,y)
multiply(x,y)

main()