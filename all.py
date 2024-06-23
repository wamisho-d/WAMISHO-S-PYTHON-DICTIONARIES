# Question 1 Task 1: Restaurant Menu Update.
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#Add a new category called "Beverages" with at least two items.
restaurant_menu["Beverages"] = {
    "Coffee": 4.98, "Tea": 3.83
}
print(restaurant_menu)

#Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

#Remove "Bruschetta" from "Starters". 
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

# Question 2 Task 1:Customer Service Ticket Tracker.
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Open a new service ticket.
def open_new_service_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Ticket ID, {ticket_id} has been already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue":issue, "Status": "Open"}
        print(f"ticket {ticket_id} opend")

 # Update the status of an existing ticket.
def Update_existing_ticket(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id] ["Status"] = status
        print(f"Ticket{ticket_id} status updated to {status}.")
    else:
        print(f"Ticket ID{ticket_id} not found.")
def display_tickets(status = None):
    for ticket_id, details in service_tickets.items():
        if status is None or details ["Status"] == status:
            print(f"ID:{ticket_id}, Customer: {details["Customer"]} Issue:{details["Issue"]}, Status: {details["Status"]}")

open_new_service_ticket("Ticket003", "Franklin", "Account Locked") 
Update_existing_ticket("Ticket002", "closed")
display_tickets()
print("\nFiltered by status 'open':")
display_tickets("open")
