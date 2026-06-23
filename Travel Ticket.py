# Creating Variables for travel ticket data and printing type of those variables
passenger_name = "Rahul"
destination = "Goa"
ticket_price = 850.50
number_of_tickets = 3
is_available = True
is_booking_confirmed = True

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

# Using arithmetic opertors to calculate total cost,discount,final cost,double ticket price, increased ticket price, and half ticket price
total_cost = ticket_price * number_of_tickets
discount = "20%"
final_cost = (ticket_price - 0.2 * ticket_price)  * number_of_tickets
double_ticket_price = ticket_price * 2
increased_ticket_price = ticket_price + 149.50
half_ticket_price = ticket_price / 2

# Using comparison operators to check if ticket price is below 1000, more than 2 tickets are booked, destination is Goa, and final cost is above 2000
print("Is ticket price below 1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination Goa?", destination == "Goa")
print("Is final cost above 2000?", final_cost > 2000)

# Writing a message using string concatenation,using .upper(),.lower(),index[],and len() function
Message = "Welcome" + " " + "Aboard"
print(Message)
print(Message.upper())
print(Message.lower())
print(Message[0])
print(len(Message))

# Creating morning ticket price and evening ticket price and swapping their values
morning_ticket_price = 700
evening_ticket_price = 900
print("Before prices are:", morning_ticket_price,"and", evening_ticket_price)
temp_price = evening_ticket_price
evening_ticket_price = morning_ticket_price
morning_ticket_price = temp_price
print("After prices are:", morning_ticket_price,"and", evening_ticket_price)

# Printing final details for travel ticket
print("Passenger Name:",passenger_name)
print("Destination:",destination)
print("No. of tickets booked:",number_of_tickets)
print("Final Amount:",final_cost)
print("Booking Confirmed:",is_booking_confirmed)
