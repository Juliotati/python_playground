# 1.
# Given a .txt file with a string "1,2,3,4,5,6,7,8,10" inside.
# Read the string of this file and use a list comprehension to
# iterate through the string and multiple each integer by itself
# and return a new list.
# Use a function for the multiplication with 1 parameter.
#
# At the end, save new list into a new file called "Task3.txt"


def file_path() -> str:
    default_file_path = '/Users/juliotati/Library/Application Support/JetBrains/PyCharmCE2022.1/scratches'
    return default_file_path


def start_task2():
    print('🎬 starting task')
    file_items = get_strings_file()
    new_items = []
    for item in file_items:
        new_items.append(multiple(item))
    save_new_items(new_items)
    print('✨ 🏁 ️task completed')


def get_strings_file():
    file = open(f'{file_path()}/scratch.txt', 'r')
    file_strings = file.read()
    file.close()
    print('📂 🔒 opened and closed file')
    return file_strings.split(',')


def multiple(input_value: str) -> str:
    result = int(input_value) * int(input_value)
    return str(result)


def save_new_items(items: [str]):
    new_file = open(f'{file_path()}/Task3.txt', 'w')
    new_file.write(str(items))
    new_file.close()
    print('📂 🔒️ saved new items and closed file')


if __name__ == '__main__':
    start_task2()
