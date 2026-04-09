def flatter(nested_list):
    for i in nested_list:
        for j in i:
            print(j, end=" ")
    return j
nested_list = [[1, 2], [3, 4], [5, 6]]
flatter(nested_list)
print()

def flat(list):
    return [j for i in list for j in i]
list = [[1,2], [3,4], [5,6]]
flat_list = flat(list)
print(flat_list)