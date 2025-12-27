'''
this snipit is to check the password streanth
'''

password=input("Enter your password: ")

#to track the password streangth
streangth = 0

#checking the length of the password
if len(password) >= 8:
    print("Your password ok")
    streangth +=1
else:
    streangth +=0
    print("password is too short")

# second check, if there are special characters or not
# if there is we update the password streagth otherwise failed
# special characters are ! , # , @

if "!" in password:
    streangth +=1
else:
    streangth +=0
if "#" in password:
    streangth +=1
else:
    streangth +=0
if "@" in password:
    streangth +=1
else:
    streangth +=0

#checking the password stranth counter
if streangth >= 2:
    print("Your password is ok")
else:
    print("Your password is not weak")

print("password streangth is at : ", streangth)

