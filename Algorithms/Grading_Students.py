#!/bin/python3
import sys

# Get Student Count
n = int(input().strip())

# Read In Grades
for grades_i in range(n):
    grade = int(input().strip())

    if grade  >= 38:
        next_multiple = grade + 1

        while next_multiple % 5 != 0:
                next_multiple += 1

        if next_multiple - grade < 3:
            print (next_multiple)
        else:
            print(grade)
            
    else:
        print(grade)
            