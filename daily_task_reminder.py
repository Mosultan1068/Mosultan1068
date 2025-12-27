'''
program to illustrate the usage of loop
this is a simple task snipit
'''

 #Daily Task Reminder

# Step: 1 - Welcome message
print("Welcome to the Daily Task Reminder Program!")
print("You'll be asked to enter tasks along with their deadlines.\n")

#  Step: 2 - Number of tasks for the day
num_tasks = int(input("Enter the number of tasks for today: "))

#  Step: 3 - Variables to store task summary
task_summary = ""

# Step: 4 - Using a for loop to take task inputs and deadlines
print("\nEnter your tasks and their deadlines:")

for task_number in range(1, num_tasks + 1):
    task = input(f"\nEnter Task {task_number}: ")
    deadline = input(f"Enter the deadline for '{task}' (e.g., 5 PM): ")
    print(f"Reminder Set: Complete '{task}' by {deadline} today.")
    task_summary += f"Task {task_number}: {task} (Deadline: {deadline})\n"

#  Step: 5 - End message
print("\nAll tasks and deadlines have been entered.")
print("Stay productive and make sure to complete your tasks on time!\n")

# Step: 6 - Display Summary
print("Summary of Today's Tasks and Deadlines:")
print(task_summary)

print("\nThank you for using the Daily Task Reminder Program!")
