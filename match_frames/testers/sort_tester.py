

'''
def custom_key_function(item):
    return abs(item)

numbers = [-3,1,-5,2,-4]

sorted_numbers = sorted(numbers, key=custom_key_function)
print(sorted_numbers)
'''

file_list = ['3.txt', '1.txt', '10.txt', '5.txt']
sorted_files = sorted(file_list, key=lambda x: int(x.split('.')[0]))

#print(sorted_files)
print(int("3.txt".split(".")[0]))