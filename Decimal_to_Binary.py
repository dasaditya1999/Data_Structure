# Function to convert decimal number
# to binary using recursion
# res = ""
# def DecimalToBinary(num):
# 	global res
# 	# if num == 0:
# 	# 	return str(num)*length
# 	if num >= 1:
# 		DecimalToBinary(num // 2)
# 	res = res + str(num % 2)
# 	return res
	

# # Driver Code
# if __name__ == '__main__':
	
# 	# decimal value
# 	dec_val = 1
# 	length = 2
	
# 	# Calling function
# 	print(DecimalToBinary(dec_val))


# Python program to convert decimal to binary

# Function to convert Decimal number 
# to Binary number 
def decimalToBinary(n): 
	return bin(n).replace("0b", "")

# Driver code 
if __name__ == '__main__': 
	print(type(decimalToBinary(8)))
	print(decimalToBinary(18)) 
	print(decimalToBinary(7))
