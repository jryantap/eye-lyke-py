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
