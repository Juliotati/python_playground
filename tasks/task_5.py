# 4. Given a list called "list_99" between numbers from
# 0 to 100. Create a new list variable and code the
# following case:
#
# a) All numbers which have a 9 as a digit like: 9, 19
# 99 should be counted, multiplied by 2 and stored in
# a new list variable.
#
# b) Return (print) the very last element of that list only.
#
# c) All numbers which have a 7 as a digit like 7, 17, 97 should
# be removed from the previous list "list_99". Your goal is to
# get a new list without the 7's.


def list_99():
    new_list_from_range = []
    for number in range(100):
        new_list_from_range.append(number)
    return new_list_from_range


def start_task5():
    new_list_99 = []
    for number in list_99():
        new_list_99.append(number * 2)

    print(f'new_list_99: {new_list_99}')
    print(f'last_element: {new_list_99[-1]}')
    remove_numbers_containing_7(list_99())


def remove_numbers_containing_7(numbers: [int]):
    criteria = '7'
    for number in numbers:
        if criteria in str(number):
            numbers.remove(number)
            return remove_numbers_containing_7(numbers)

    print(f'numbers_without_7: {numbers}')


if __name__ == '__main__':
    start_task5()
    print('✨ 🏁 ️task 5 completed')
