users = ['blazer, 23', 'long, 28', '10act, 27', 'albina, 18', 'matilda, 28']


def generate_user() -> []:
    new_users = []
    for raw_user in users:
        user = raw_user.split(',')
        user_name = user[0]
        user_age = user[1]

        new_user = {
            'name': user_name,
            'age': user_age,
        }
        new_users.append(new_user)
    return new_users


sub_users = [
    generate_user()
]


def get_user():
    return users


def delete_user(index: int):
    user_to_delete = users[index]
    users.remove(user_to_delete)
    print(f'removed {user_to_delete}')


def add_user(username: str):
    users.append(username)
    users.sort()
    print(f'added {username}')


def edit_user(user_id: int, new_name: str, new_age: int = None):
    max_user_count = len(users) - 1
    if user_id > max_user_count:
        print(f'could not find a user with the given id: {user_id}, limit is: {max_user_count}')
        return IndexError

    if new_age is not None:
        users[user_id] = f'{new_name}, {new_age}'
        print(f'''
        updated user: {user_id}
        new: {users[user_id]}
        ''')
        return

    if new_age is None:
        existing_user_age = users[user_id].split()[1]
        users[user_id] = f'{new_name}, {existing_user_age}'
        print(f'''
        updated user: {user_id}
        new: {users[user_id]}
        ''')
