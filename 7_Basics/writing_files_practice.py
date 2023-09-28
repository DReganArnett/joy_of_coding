# Writing Files Practice
# Danielle Arnett

def main():
    # 1.
    test_file = open('read_file.py', 'r')
    for line in test_file:
        print("-", line)
    test_file.close()
    print()


    # 2.

    # Line 32: Variable to prompt user to enter the name of the file they are creating
    # Line 33: Variable to prompt user to enter a number and enter 0 when finished
    # Line 34: Variable to create and refer to the file named through user input and to enter "write" mode
    # Line 35: Boolean variable to control when the while-loop stops executing
    # Line 37: While keepGoing == true...
    # Line 38: The variable, userInput, stores the input from the user
    # Line 39: If userInput equals 0...
    # Line 40: Set keepGoing to false to end the storing of user input when user enters 0,
    # Line 41: Print "All done!" to the user console to alert the user that the write-phase of the program has finished
    # Line 42: Break out of the while loop before 0 is printed to the file
    # Line 43: Print the userInput to the file indicated
    # Line 44: Close the newly-created file
    # Line 47: Re-open file for testing
    # Line 48: Read file contents line by line
    # Line 49: Print each line to make sure the userInput made its way into the file
    # Line 51: Close the file

    file_name = (input("What do you want to name your file? "))
    prompt = "Enter a number.  Enter 0 when finished. "
    output_file = open(file_name, "w")
    keep_going = True

    while keep_going:
        user_input = eval(input(prompt))
        if user_input == 0:
            keep_going = False
            print("All done!")
            break
        print(user_input, file=output_file)
    output_file.close()

    # Read file created above to  make sure the user input got saved to the file
    output_file = open(file_name, "r")
    for line in output_file:
        print(line.rstrip())

    output_file.close()
    print()


    # 3.

    def read_and_count_lines(file):
        output_file = open(file, 'r')
        lines = []
        for line in output_file:
            lines.append(line)
        count = len(lines)
        output_file.close()
        return count

    count_file = open("count.txt", "w")
    print(read_and_count_lines('text1.txt'), file=count_file)
    print(read_and_count_lines('text2.txt'), file=count_file)
    print(read_and_count_lines('text3.txt'), file=count_file)
    count_file.close()

    count_file = open("count.txt", "r")
    for line in count_file:
        print(line.rstrip())
    count_file.close()
    print()


    # 4.

    def read_and_count_words(file):
        output_file = open(file, 'r')
        word_count = 0
        for line in output_file:
            words = len(line.split(' '))
            word_count += words
        output_file.close()
        return word_count

    line_count_1 = read_and_count_lines('text1.txt')
    line_count_2 = read_and_count_lines('text2.txt')
    line_count_3 = read_and_count_lines('text3.txt')
    total_lines = line_count_1 + line_count_2 + line_count_3

    word_count_1 = read_and_count_words('text1.txt')
    word_count_2 = read_and_count_words('text2.txt')
    word_count_3 = read_and_count_words('text3.txt')
    total_words = word_count_1 + word_count_2 + word_count_3

    count_file = open("count.txt", "w")
    print('text1.txt :', line_count_1, 'lines', word_count_1, 'words', file=count_file)
    print('text2.txt :', line_count_2, 'lines', word_count_2, 'words', file=count_file)
    print('text3.txt :', line_count_3, 'lines', word_count_3, 'words', file=count_file)
    print('TOTAL:', total_lines, 'lines,', total_words, 'words', file=count_file)
    count_file.close()

    count_file = open("count.txt", "r")
    for line in count_file:
        print(line.rstrip())
    count_file.close()


main()