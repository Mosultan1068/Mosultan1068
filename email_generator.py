'''
Exercise to generate an email
'''

opening_greeting= "Good day to you"
email_name= input("Enter your username: ")
#print(email_name)
fixed_email= (email_name.replace( " ",".")
              .replace("_","."))

first_name = fixed_email[:fixed_email.find (".")]
last_name = fixed_email[fixed_email.find (".")+1:]

formatted_first_name = first_name[0].upper() + first_name[1:]
formatted_last_name = last_name[0].upper() + last_name[1:]
print(formatted_first_name)
print(formatted_last_name)
full_email_address = formatted_first_name + "." + formatted_last_name + "@" + "yahoo.com"
print(full_email_address)

'''
formating the actual email to send
'''
recipient = 'Harry'
sender = 'full_email_address'
print("Dear " + recipient + " Good Day to You")
print()
print()
print()
print(''' This is an official email to express ...  

Best Regards
''')


