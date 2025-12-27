'''
showing how the zip function works
'''


pairs = [('Alice', 25), ('Bob', 30)]
names, ages = zip(*pairs)

print(names)  # ('Alice', 'Bob')
print(ages)   # (25, 30)

string1="ABCDEF"
string2="123456"

combined=zip(string1,string2)

for i in combined:
    print(i)
