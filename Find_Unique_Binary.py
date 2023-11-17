# res = ""
# def DecimalToBinary(num):
#     global res
#     if num>1:
#         DecimalToBinary(num//2)
#     res = res + str(num%2)
#     return res

def DecimalToBinary(n):
	return bin(n).replace("0b", "")

## Generating all possible binary numbers as per the length of the list
n = int(input('Enter the length of the string'))
enumerateTill = 2**n - 1
possibleBinaryNumbers = []
for i in range(0,enumerateTill+1):
    res = ""
    resulted_binary = DecimalToBinary(i)
    print(i,resulted_binary)
    possibleBinaryNumbers.append(resulted_binary)

## Balancing the Binary Numbers as per the length of each binary present in the List
for i in range(0,len(possibleBinaryNumbers)):
    if len(possibleBinaryNumbers[i]) != n:
        zeros_to_be_added = n - len(possibleBinaryNumbers[i])
        possibleBinaryNumbers[i] = (zeros_to_be_added*'0')+possibleBinaryNumbers[i]

print(possibleBinaryNumbers)

input_array = ['00','01']
input_array = ['001','111']

for i in possibleBinaryNumbers:
    if i not in input_array:
        print(i)
