# Learning Exercise: Conditions - Reading ifs, part 2
# Danielle Arnett

# Exercise
x = 3
y = 7

print(not x == 5)
    # true
print( x > 0 and y > 0 )
    # true
print(x < 0 or y < 0 )
    # false
print( x*y > 20 or x*y <-20 )
    # true

print()

# Challenge
print( not (x == 0 or y == 5) )
    # true
print(not x == 0 or y == 5 )
    # true
print( x == 3 and not y == 5 )
    # true
print( not (x == 3 and y == 5) )
    # true