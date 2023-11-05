# Playing with a monthly expenditure Data

month_wise_expense = {'January':2200, 'February':2350, 'March':2600, 'April':2130, 'May':2190}

print('Expenditure in Feb is ', month_wise_expense['February'])

counter = 0
quarter_exp = 0

for key,value in month_wise_expense.items():
    if counter == 3:
        break
    counter = counter + 1
    quarter_exp = quarter_exp + value
print(f'total expenditure in the first quarter is, {quarter_exp}')

isSpend = False
for month, amount in month_wise_expense.items():
    if amount == 2000:
        isSpend = True
        print(f'Yes! 2000 was spent in the month of {month}')
if isSpend == False:
    print('No month is having a spent of 2000')

month_wise_expense['June'] = 1980

month_to_update = 'April'
amount_to_update = 200

month_wise_expense['April'] = month_wise_expense['April'] + amount_to_update
print(f'Updated List would be, {month_wise_expense}')
