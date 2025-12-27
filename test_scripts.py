'''
bottle factory quiz
'''

for ids in range(1001, 1010):
    if ids % 2 == 0:
        print(f"{ids} is Even")
        if ids == 1005:
            continue
    else:
        print(f"{ids} is Odd")
        if ids == 1009:
            exit(100)





