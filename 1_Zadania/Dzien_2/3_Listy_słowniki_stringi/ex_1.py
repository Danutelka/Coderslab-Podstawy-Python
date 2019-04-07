def create_list(a, b):
    new_list = []
    for i in range(4):
          new_list += [a, b]
    return new_list


my_list = create_list(True, 1)
print(my_list)