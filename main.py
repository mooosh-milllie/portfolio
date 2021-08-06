# unsorted_list = [('first_element', 6), ('second_element', 1), ('third_element', 2)]
# sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
# my_list = []
# while len(unsorted_list) > 0:
#     current_value = unsorted_list[0][1]
#     min_value = unsorted_list[0][1]
#     index = 0
#     for tuple_ in unsorted_list:
#         if tuple_[1] <= min_value:
#             min_value = tuple_[1]
#             min_index = index
#         index +=1
#     my_list.append(unsorted_list.pop(min_index))
#     print(str(unsorted_list))

# print(my_list)

unsorted_list = [('first_element', 4), ('second_element', 6), ('third_element', 2 )]
sorted_list = []

list_value = []
for tuple_ in unsorted_list:
    list_value.append(tuple_[1])

print(list_value)
list_value.sort()

for value in list_value:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            print(tuple_[1])
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)
print(unsorted_list)
