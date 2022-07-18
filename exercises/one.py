# 1.
# Given is a list between numbers from 0 to 100, and it should be
# output every number in the terminal, which is divisible by 2.
#
numbers_list1 = range(0, 100)

for number in numbers_list1:
    if number % 2 == 0:
        print(number)

# 2.
# Given is a list between numbers from 0 to 100. All numbers which
# have a 5 as a digit like: 5, 15, 95 should be counted and stored
# in a new list variable. Please return the total number of entries
# in that list and the list itself.

numbers_list2 = range(0, 100)
numbers_containing_five = []

for number in numbers_list2:
    if number.__str__().__contains__('5'):
        numbers_containing_five.append(number)
print(numbers_containing_five)
