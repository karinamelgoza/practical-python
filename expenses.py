# expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum = 0

# for i in expenses:
#     sum = sum + i

# total = 0
expenses = []
num_expenses = int(input('# of expenses:\n'))

for i in range(num_expenses):
    expenses.append(float(input('enter your expense: \n')))

total = sum(expenses)

print('You spent $', total, ' on lunch this week', sep='')
