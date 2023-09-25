# Reading ifs
# Danielle Arnett

# Question 1:
    # 1. Monday - "Wake up at 7 am"
    # 2. Saturday - "Wake up at 9 am"
    # 3. Sunday - "Wake up at 10 am"
    # 4. Raining -  "Wake up at 7 am"

# Question 2:

# a & b

DoW = input("What day is it? ")
# DoW = "Monday"

if DoW.lower() == "saturday":
    print("Wake up at 9 am")
elif DoW.lower() == "sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")