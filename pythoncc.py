test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print(test_list)

unique_list = []

for item in test_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
