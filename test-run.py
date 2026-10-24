# Import the numpy package as np
try:
    import numpy as np
except ImportError:
    np = None

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

if np is not None:
    # Create a numpy array from baseball: np_baseball
    np_baseball = np.array(baseball)

    # Print out type of np_baseball
    print(type(np_baseball))
else:
    print("NumPy is not installed. Install it with: pip install numpy")

## Concept Review ##
name = "Jherico"
numberOfLesson = 5
numberOflessonRemaining = 10

print("Name: " , name)
print("Number of Lessons: " , numberOfLesson)

tickets = int(input("How many tickets do you have?"))

if tickets == 0:
  print("your queue is clean")
else:
  print("you still have", tickets, " open tickets.")


tickets = int(input("How many tickets do you have?"))

if tickets >= 10:
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
for apps in applications:
  print (applications)

open_tickets = ["ticket_1", "ticket_2", "ticket_3"]

for ticket in open_tickets:
  print("Reviewing ticket: ", ticket)

print("Total Tickets: ", len(open_tickets))

# lesson 8 review 
commands = ["ping", "ipconfig", "tracert"]
for number, command in enumerate(commands):
  print(number, command)

tickets = ["INC1001", "INC1002", "INC1003"]
for number, ticket in enumerate(tickets):
  print(number, "-", ticket)

applications = ["Epic", "WebEx", "VMware"]
for number, apps in enumerate(applications, start = 1):
  print (number, "-", apps)

#lesson 9 review
  
password = ""
while password != "python123":
   password = input("Enter your password: ").lower()
print("Access granted!")

#lesson 10 
def check_ticket_count(ticket_count):
   if ticket_count == 0:
      return "No tickets to review."
   else:
      return "You have tickets to review."

ticket_count = int(input("Enter the number of tickets: "))
check_ticket_count(ticket_count)

computers = [
    {"name": "PC-1001", "status": "Online"},
    {"name": "PC-1002", "status": "Offline"},
    {"name": "PC-1003", "status": "Offline"}
]

offline_count = 0;

for computer in computers:
   if computer["status"] == "Offline":
      offline_count +1;
print("Offlinec computers: ", offline_count)

tickets = [
    {"number": "INC1001", "priority": "High"},
    {"number": "INC1002", "priority": "Low"},
    {"number": "INC1003", "priority": "High"},
    {"number": "INC1004", "priority": "Medium"}
]

ticket_priority = 0

for ticket in tickets:
   if ticket["priority"] == "High":
    ticket_priority +=1;
print("Number of High Priority tickets = ", ticket_priority)




      