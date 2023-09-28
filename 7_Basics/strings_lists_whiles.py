# Strings, Lists & Whiles
# Danielle Arnett

def main():
    average_neg_evens(list)
    print()
    count_letter(list2, letter)

# 1.
def average_neg_evens(list):
    index = 0
    total = 0
    count = 0
    while index < len(list):
        if list[index] < 0 and list[index] % 2 == 0:
            total += list[index]
            count += 1
            index += 1
        else:
            index += 1
    return print("Average: ", total/count)

list = [0, 1, 2, -2, -3, -4, 3, 4]
#average_neg_evens(list)


# 2.
def count_letter(list, letter):
    count = 0
    index = 0
    list = ''.join(list)
    while index < len(list):
        if list[index].lower() == letter:
            count += 1
            index += 1
        else:
            index += 1
    return print("The letter ", letter, " appears ", count, "times in the list.")
list2 = ["HELLO", "goodbye", "1234 Oooh!"]
letter = 'o'
#count_letter(list2, letter)

main()