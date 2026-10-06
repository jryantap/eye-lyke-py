# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

name = "Jherico"
numberOfLesson = 5
numberOflessonRemaining = 10

print("Name: " , name)
print("Number of Lessons: " , numberOfLesson)

tickets = int(input("How many tickets do you have?"))

if tickets == 0;
  print("your queue is clean")
else:
  print("you still have", tickets, " open tickets.")


tickets = int(input("How many tickets do you have?"))

if tickets >= 10;
  print("Daily goal reached!")
else:
  print("Keep going!")

calls = int(input("How many calls did you handle? "))

if calls >= 15:
    print("Goal exceeded!")
elif calls >= 10:
    print("Goal reached!")
else:
    print("Keep going!")

# lesson 
department = input ("department: ").lower()
multiple_users = input ("multiple: ").lower()

if department == "clinical" and multiple_users == "yes":
  print("Escalate the issue.")
else: 
  print("Not an outage.")

# lesson 7 review
applications = ["Epic", "Outlook", "Duo"]
for apps in applications;
  print (applications)

open_tickets = ["ticket_1", "ticket_2", "ticket_3"]

for ticket in open_tickets;
  print("Reviewing ticket: ", ticket)

print("Total Tickets: ", len(open_tickets))




