'''
nested conditions snipit
'''

student_score = int(input("\nEnter the student score: "))
if student_score >= 60:
    if student_score >= 90:
        print("\nThe student score is greater than or equal to 90 - Grade A")
    elif student_score >= 80:
        print("\nThe student score is greater than or equal to 80 - Grade B")
    elif student_score >= 70:
        print("\nThe student score is greater than or equal to 70 - Grade C")
    else:
        print("\nGrade D")
else:
    print("\nThe student score is :",student_score)
    print("\n Grade : F")
