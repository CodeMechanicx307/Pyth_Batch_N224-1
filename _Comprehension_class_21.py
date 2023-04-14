
list_comp=list(value for value in range (1,101))
print(list_comp)

dict_comp={ value:value+2 for value in range(1,6)}
print(dict_comp)

tpl_comp=tuple(value for value in range(1,11))
print(tpl_comp)

tpl_comp_2=*(n for n in range(1,11,2)),
print(tpl_comp_2)

set_comp={value for value in range (1,10) }
print(set_comp)

set_comp={value for value in range (1,10) if value %2 == 0 }
print(set_comp)

set_comp=set(value for value in range (1,10) )
print(set_comp)

# open_book_exam_2(recursion)
"""
def get_unique_list(original_list):
    unique_list = []

    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


original_list = [1, 2, 3, 4, 1, 2, 5]

unique_list = get_unique_list(original_list)

print(unique_list)
"""