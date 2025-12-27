''''
question snipit
'''

answer=str(input("Do you have a card? (yes/no) \n"))

answer=answer.lower()
print(answer, "Lowercase")

answer=answer.upper()
print(answer, "Uppercase")

answer=answer.strip()
print(answer, "strip")

answer=answer.capitalize()
print(answer, "capitalize")


if answer not in ["YES", "Y", "yes", "Yes", "YES", "Yes"]:
    print("Not Right", answer)