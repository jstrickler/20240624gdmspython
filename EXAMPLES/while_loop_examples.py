
print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("Please enter quantity...")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    try:
        quantity = int(raw_quantity)  # could validate via try/except
    except ValueError as err:
        print("Invalid quantity -- please enter only digits")
#        print(err)
    else:
        print(f"sending {quantity} ticket(s)")
