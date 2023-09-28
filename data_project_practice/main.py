# Data Project Practice
# Danielle Arnett

import math
from tabulate import tabulate

def main():
    create_table(data, head)


grades_file = open('sample_grades.csv', 'r')
fall_grades = []
spring_grades = []
for line in grades_file:
    line = line.rstrip()
    line = line.split(',')
    if line[1] == 'Fall 2016':
        fall_grades.append(int(line[2]))
    else:
        spring_grades.append(int(line[2]))


def mean_grade(list):
    average = round(sum(list)/len(list), 2)
    return average


mean_fall = mean_grade(fall_grades)
mean_spring = mean_grade(spring_grades)


def median_grade(list):
    sorted_list = sorted(list)
    median_idx = math.floor(len(list)/2)
    if len(list) % 2 == 0:
        median = (sorted_list[median_idx] + sorted_list[median_idx-1])/2
    else:
        median = sorted_list[median_idx]
    return median


median_fall = median_grade(fall_grades)
median_spring = median_grade(spring_grades)


def standard_deviation(list):
    mean = sum(list)/len(list)
    differences = []
    squared_differences = []
    for grade in list:
        difference = grade-mean
        differences.append(difference)
    for difference in differences:
        square = difference * difference
        squared_differences.append(square)
    total = sum(squared_differences)
    variance = total/(len(list))
    standard_deviation = round(math.sqrt(variance), 2)
    return standard_deviation


std_fall = standard_deviation(fall_grades)
std_spring = standard_deviation(spring_grades)

head = ["Statistic Type:", "Fall 2016:", "Spring 2016:"]
data = [
            ['mean', mean_fall, mean_spring],
            ['median', median_fall, median_spring],
            ['STD', std_fall, std_spring]
       ]


def create_table(data, head):
    print(tabulate(data, headers=head, tablefmt='grid'))


# create_table(data, head)

main()