# input_binary = ['01','10']
# input_binary = ["00","01"]
input_binary = ["111","011","001"]

input_decimal = []

for i in input_binary:
    input_decimal.append(int(i,2))

for i in range(0,2**16+1):
    binary_value = bin(i).replace('0b','')
    print('binary',binary_value)
    if len(binary_value) == len(input_binary) and binary_value not in input_binary:
        print(i)
        break