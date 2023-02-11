"""Prime factors of n"""
num = int(input("Enter random integer: "))
my_list = []
i = 2
old = num
while i <= num:
    if num % i == 0:
        my_list.append(i)
        i += 1
    else:
        i += 1
print(f"Prime factors of {old} are in list: {my_list}")
