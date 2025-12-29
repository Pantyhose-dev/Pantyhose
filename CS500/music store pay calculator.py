
# Jared West
# CS-500
# In the spotlight Commission in Functions
# Mr. Chou

# This program calculates and determines
# a salesperson's pay at a music store, including commission.

def main():
    sales = get_sales()  # Get amount of sales
    advanced_pay = get_advanced_pay()  # Get the amount of advanced pay
    comm_rate = determine_comm_rate(sales)  # Determine the commission rate
    sales_pay = sales * comm_rate  # Calculate the total commission
    pay = sales_pay - advanced_pay  # Subtract advance pay from commission

    print()
    print(f"Your sales have given you a commission of ${sales_pay:.2f}.")
    print(f"You have taken ${advanced_pay:.2f} in advanced pay this month.")
    print(f"Your pay after returning advance is ${pay:.2f} this month.")

    # Determine whether the pay is negative
    if pay < 0:
        print("The salesperson must reimburse the company.")

# Get a salesperson's monthly sales from user; returns value
def get_sales():
    while True:
        try:
            monthly_sales = float(input("Enter the monthly sales: $"))  # Get monthly sales
            if monthly_sales < 0:
                print("Sales cannot be negative. Please enter a valid amount.")
            else:
                return monthly_sales
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get the amount of advanced pay from the user
def get_advanced_pay():
    print("Enter the amount of advanced pay, or enter 0 if no advanced pay was given.")
    while True:
        try:
            advanced = float(input("Advanced pay: $"))  # Get amount of advanced pay
            if 0 <= advanced <= 2000:
                return advanced  # Return the amount entered
            else:
                print("Invalid amount. Advanced pay must be between $0 and $2000. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Determine the commission rate based on sales
def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales <= 14999.99:
        rate = 0.12
    elif sales <= 17999.99:
        rate = 0.14
    elif sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    return rate  # Return the commission rate

# Call main function
if __name__ == "__main__":
    main()
3
