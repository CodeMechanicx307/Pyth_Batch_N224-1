set = {1,2,3,4,5}
odd_list = (filter(lambda value: value + 2,set))
even_list =map(lambda even_sum: even_sum + 10 if even_sum % 2 == 0 else even_sum + 2,set)
print((odd_list))
print(list(even_list))

"""
def sum_all_value(values):
    total = 0

    for item in values:
        total += item

    return total


values = [10, 20, 30, 40, 50]
total_sum = sum_all_value(values)
print(total_sum)
"""