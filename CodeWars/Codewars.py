def move_zeros(lst: list) -> list:
    counter_of_zeros = 0
    temporary_list = list()
    for i in range(len(lst)):
        if lst[i] == 0:
            counter_of_zeros += 1
        else:
            temporary_list.append(lst[i])
    temporary_list += [0] * counter_of_zeros
    return temporary_list

# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))  # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(move_zeros([0, 0]))  # [0, 0]
print(move_zeros([]))  # []

