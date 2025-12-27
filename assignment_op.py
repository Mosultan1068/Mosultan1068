'''
to learn more regarding the assignment operators
'''

files=int(input("Enter the number of files:"))
value1=float(100)
value2=int(100)
if files==10:
    print("file 10")
    for i in range(1,files+1):
        print("file", i)
else:
    print("file 5")

if value1 != value2:
    print("Not")
else:
    print("Yes")