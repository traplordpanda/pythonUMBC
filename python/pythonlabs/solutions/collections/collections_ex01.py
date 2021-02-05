#!/usr/bin/env python3
""" A Solution For collections_ex01

    Write a program that creates a loop asking the user to input a number.
    • Repeat this process until the user enters the value "end."
    • The following can be used to loop through the user input.
            prompt = "Enter a number (or the word 'end' to quit) "
            while True:
                data = input(prompt )
                if value == "end":
                    break
                # Remainder of while loop goes here
    • Enter each number into a set.
    • However, before you enter the number, check to see if the number is
      already in the set.
    • If it is already there, update a counter that tracks how many entries
      were not added to the set.
    • Just before the program ends, print the following:
    • The contents of the set on one line and
    • The number of elements that were NOT added to the set on the
      second line.
"""
count = 0
numbers = set()
prompt = "Enter a number (or the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    # Remainder of while loop goes here
    if data not in numbers:
        numbers.add(data)
    else:
        count += 1

print("The set is:", numbers)
print(count, "values were not unique.")
