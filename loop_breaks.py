'''
testing how to exit the loop using
= break
== continue
== pass
'''


for i in range(1,11):
    if i == 5:
        print("stopping here. Number: ", i ,"has been spotted")
        break
    if i%2==0:
        print("even numbers", i)
        continue
    else:
        print("odd numbers", i)
        pass
