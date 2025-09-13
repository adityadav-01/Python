tic = 5
print(f"Total Tickets are :{tic} ")
while tic > 0:
    req = int(input("\nEnter number of tickets : (0 for end ) : "))
    
    if req == 0:
        print("Booking ended by user ")
        break
    elif req <= tic:
        print("Ticket Booked successfully")
        tic -= req
        print(f"Available Tickets are {tic}")
    else:
        print("Not Enough Ticket Available ")

if tic == 0:
    print("\nAll Ticket are sold out ")