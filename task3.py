"""List of unique elements"""

my_list = list(map(int, input("Enter random numbers separated by spaces: ").split()))
print(f"Original list: {my_list}")
new_list = []
for el in my_list:
    if el not in new_list:
        new_list.append(el)
print(f"List of unique elements: {new_list}")
