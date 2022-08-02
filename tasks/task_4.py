# 3.
# Given a list called community_members with names
# of our members (strings) in it. All members which have
# at least the letter "a" 1x in should be filtered and
# stored in a new list variable. Please return the total
# number of entries of that list.

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]

criteria = 'a'


def start_task4():
    members_names_containing_criteria = []
    for member in community_members:
        if criteria in member:
            members_names_containing_criteria.append(member)

    remove_members_with_criteria(community_members)

    print(f'filtered_members: {members_names_containing_criteria}')
    print(f'total entries: {len(members_names_containing_criteria)}')
    print('----------')
    print(f'remaining_members: {community_members}')



def remove_members_with_criteria(remaining_members: [str]):
    for member in remaining_members:
        if criteria in member:
            community_members.remove(member)
            remove_members_with_criteria(community_members)


if __name__ == '__main__':
    start_task4()
    print('✨ 🏁 ️task 4 completed')