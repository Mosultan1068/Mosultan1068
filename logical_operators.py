'''
this snipit shows the use of the logical operators
'''

question1=int(input("What is your favorite number?"))
question2=input("What is your favorite colour?")
question3=input("What is your favorite place?")

print(question1, question2, question3);

if question1 >=5 and question2=="Blue" and question3=="London":
    print("Great")
else:
    print("Not Great")
