# Creating a list which would be having only Odd Numbers.

max_val = int(input('Please enter the value upto which you want the odd numbers '))

result_list = []

for i in range(1,max_val):
    if i %2 != 0:
        result_list.append(i)

print(result_list)


