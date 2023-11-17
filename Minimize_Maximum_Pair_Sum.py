inputList = [3,5,4,2,4,6]
inputList.sort()
print(inputList)

array = list()

for i in range(0,len(inputList)//2):
    array.append(inputList[i] + inputList[len(inputList)-1-i])

print(max(array))