# - Write a Python function with the name "en_filter" which
# takes one parameter and checks whether a string has no "e"
# and "n".
#
# - Use a list comprehension which loops through the previous
# list from task 3 (community_members) and call (use) that
# function in the list comprehension.
#
# If the requirements are met, extend the function "en_filter"
# by implementing the code to append the string variable to the
# new list, created by the list comprehension. Print the final
# list the way it is.


def start_task6():
    community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
    numbers = [member for member in community_members if should_append_member(member)]
    print(numbers)


def should_append_member(member_name: str) -> bool:
    no_criteria_e = 'e' not in member_name
    no_criteria_n = 'n' not in member_name

    return no_criteria_e and no_criteria_n


if __name__ == '__main__':
    start_task6()
    print('✨ 🏁 ️task 6 completed')
