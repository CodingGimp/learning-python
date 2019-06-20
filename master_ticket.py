TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining > 0:
    name = str(input('Hello, welcome to MasterTicket! What is your name?\n'))

    print('Hello there, {}! Currently, there are {} tickets remaining. Each ticket is $10.'.format(name, tickets_remaining))
 
    try:
        how_many_tickets = int(input('How many tickets would you like to purchase?\n'))
        if how_many_tickets > tickets_remaining:
            raise ValueError("Unfortunately, we don't have that many tickets available at this time.")            
    except ValueError as err:
        print("Sorry, we've encountered an error. {} Please try again.".format(err))
    else:
        answer = input("Okay, {}...that will be ${}. Would you like to continue? Type 'Y' or 'N'...\n".format(name, how_many_tickets*TICKET_PRICE)).lower()

        if answer == 'y':
            print('Great! I will send over those tickets to you very soon! Thanks, {}.'.format(name))
            tickets_remaining -= how_many_tickets
            print('There are now {} tickets remaining.'.format(tickets_remaining))
        else:
            print('Okay, that\'s cool...' )

print('I apologize...we are completely sold out of tickets at this time.')


