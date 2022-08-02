# 3.
# Given a list called community_members with names
# of our members (strings) in it. All members which have
# at least the letter "a" 1x in should be filtered and
# stored in a new list variable. Please return the total
# number of entries of that list.

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]


def start_task4():
    criteria = 'a'
    members_names_containing_a = []
    for member in community_members:
        if criteria in member:
            members_names_containing_a.append(member)

    print(f'total entries: {len(members_names_containing_a)}')
    print('✨ 🏁 ️task 4 completed')


if __name__ == '__main__':
    start_task4()
