'''
menu.py
'''

''' 
lampda function takes any number of urgments and 1 expression.
first example below
arguments are: a,b,c which is 1,2,3
expression is: a+b+c+10 , which is 1+2+3+10

in a nutshell, many urgments and 1 expression ( Simple ) 
'''
x = lambda a, b, c : a + b + c + 10
a=1
b=2
c=3
print(x(a,b,c))

'''
this example below where the lampda function takes
the n as an argument, 
the expression looks at every number in the list known as n
if n div 2 and the reminder is not 0 then , the number is a odd number
then it is displayed 
Y is holding the list of items to be displayed

the argument is : n
the expression is : n%2!=0
the input parameter is numbers which is a list
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 99]
y=list(filter(lambda n: n%2!=0, numbers))
z=list(filter(lambda n: n%2==0, numbers))
print(y," These are the odd numbers")
print(z,"these are the even numbers")

'''
this is an example to retuen the largest number in a list of numbers using 
lampda function
more complicated but is very useful
it is using the list to go through
numbers_2 = [9, 2, 3, 22, 5, 6, 245, 8, 99]
'''
numbers_2 = [9, 2, 3, 22, 5, 6, 245, 8, 99]
max_index, max_value = max(enumerate(numbers_2), key=lambda x: x[1])
print("Max:", max_value, "Index:", max_index)



