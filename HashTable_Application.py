######### Prepare the Data Structure ########
d = dict()
with open('nyc_weather.csv') as f:
    for line in f:
        line.rstrip('\n')
        arr = line.split(',')
        if arr[0] == 'date':
            continue
        val = arr[1]
        d[arr[0]] = val[0:-1]
# print(d)

##### Calculate the First Seven days Avg Temp in NYC ##########
days = 1
avg_temp = 0
for k,v in d.items():
    # print(k,'->',v)
    avg_temp = avg_temp + int(v)
    
    if days == 7:
        break
    
    days = days + 1

# print(avg_temp/7)


##### Calculate the Max Temp in the first 10 days of Jan ######
list1 = []
with open('nyc_weather.csv') as f:
    for line in f:
        arr = line.split(',')
        val = arr[1]
        val = val[0:-1]
        list1.append(val)
    list1 = list1[1:]

# print(max(list1))


#### Find Temp on Specific Date ####
# print(d['Jan 9'])
# print(d['Jan 4'])


###### Read Poem File & Find the Occurrence of each token/word in the poem #######
arr2 = []
resultant_dict = dict()
with open('poem.txt', 'r') as file:
    string = file.read()
    arr = string.split(' ')

for i in arr:
    resultant_dict[i] = arr.count(i)

print(resultant_dict)



