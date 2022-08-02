# 1.
# Given is a list between numbers from 0 to 100, and it should be
# output every number in the terminal, which is divisible by 2.

# 2.
# Given is a list between numbers from 0 to 100. All numbers which
# have a 5 as a digit like: 5, 15, 95 should be counted and stored
# in a new list variable. Please return the total number of entries
# in that list and the list itself.

numbers_list = range(0, 100)
numbers_containing_five = []
criteria = '5'
for number in numbers_list:
    if number % 2 == 0:
        print(number)
    if str(number).__contains__(criteria):
        numbers_containing_five.append(number)

print(numbers_containing_five)
print(f'Total numbers containing {criteria}: {len(numbers_containing_five)}')
print('✨ 🏁 ️Completed tasks')
