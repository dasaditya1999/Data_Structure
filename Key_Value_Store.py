#Method 1 -- Using 1-D array
with open('stock_prices.csv','r') as f:
    for line in f:
        every_row = line.split(',')
        if every_row[0] == 'march 7':
            print(f'Yes, we have the expenditure for the same & i.e. {every_row[1]}')

#Method 2 -- Using 2-D Array
main_array = []

with open('stock_prices.csv', 'r') as f:
    for line in f:
        subarray = list()
        every_row = line.split(',')
        main_array.append([every_row[0], every_row[1]])

for i in main_array:
    if i[0] == 'march 7':
        print(f'Yeahhh!!! we have it here having value {i[1]}')


#Method 3 -- Using Dictionary & Dictionary is an implementation of the Hashtable.
d = dict()

with open('stock_prices.csv', 'r') as f:
    for line in f:
        arr = line.split(',')
        d[arr[0]] = arr[1]

# print(f'The Dictionary is {d}')
user_input = 'march 7'
print(d[user_input])

