# Lesson 10
def check_ticket_count(ticket_count):
    if ticket_count == 0:
        print("clear.")
    else:
        print("Your have ticket to review!", "look: ", ticket_count)

tickets = int(input("How many tickets do you have?"))

check_ticket_count(tickets)

# Create a function named show_command() that accepts a command and prints:
def show_command(command):
    print("Run this command: ", command)

show_command("ping")
show_command("prints")

# Create a function named count_apps() that accepts a list and returns the number of items in it. Use the function with this list:
def count_app(app_list):
    print("applications: ", app_list)
    print(len(app_list))
    
applications = ["Epic", "Outlook", "Duo", "Vmware"]
count_app(applications)


