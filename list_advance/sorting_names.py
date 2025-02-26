def sorted_names(names_list):
    return sorted(names_list, key=lambda name: (-len(name), name))


names = input().split(', ')
result = sorted_names(names)
print(result)