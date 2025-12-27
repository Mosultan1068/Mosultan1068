'''
personal budget calculator
input - the following
'''
from pickletools import read_int4

#asking the user for the income

income = int(input('what is your monthly income ?'))
rent = int(input('what is your rent ?'))
grocery = int(input('what is your grocery ?'))
transportation = int(input('what is your transportation ?'))
utility = int(input('what is your utility ?'))
others = int(input('what is your others ?'))

print('Your Income is £',income ,'Per Month')
total_expense = rent + grocery + transportation + utility + others

left_over = int(income) - int(total_expense)
print('Your left over is:',left_over ,'£')
print('total expensis is',total_expense ,'£')


