

menu = {
    "breakfast":{
        "1":{"name":"rolex","price":5000}, 
        "2":{"name":"katogo","price":8000}, 
        "3":{"name":"tea","price":2000}},

    "lunch":{
        "1":{"name":"posho and beans","price":7000}, 
        "2":{"name":" matooke and groundnuts" , "price":9000}, 
        "3":{"name":"soda","price":3000}
    },

    "supper":{
        "1":{"name":"chips and chicken","price":15000}, 
        "2":{"name":"pilau","price":12000}, 
        "3":{"name":"water","price":1500}
    }
}

orders=[]
running_total = 0

# DISPLAY MENU FUNCTION
def display_menu():
    print("\nEBENEZER RESTAURANT!")
    print("CHECK OUT OUR MENU PLIZ!!:")
    for meal, items in menu.items():
        print(f"{meal.capitalize()}:")
        for item_number, item in items.items():
            print(f"  {item_number}. {item['name']} - {item['price']} UGX")

def display_single_menu(meal_type):
    print(f"\n--- {meal_type.capitalize()} Menu ---")
    for item_number, item in menu[meal_type].items():
        print(f"  {item_number}. {item['name']} - {item['price']} UGX")

# TAKE ORDER FUNCTION
def take_order():
    global running_total
    while True:
        print("\nEBENEZER RESTAURANT")
        print("CHECK OUT OUR MENU PLIZ!!!")
        print("\nSelect a meal type:")
        print("1. Breakfast")
        print("2. Lunch")
        print("3. Supper")
        meal_choice = input("enter your meal choice (1-3): ").strip()

        if meal_choice == "1":
            meal_type = "breakfast"
        elif meal_choice == "2":
            meal_type = "lunch"
        elif meal_choice == "3":
            meal_type = "supper"
        else:
            print("sorry we dont have that meal.")
            continue
        
        # Show only selected menu
        display_single_menu(meal_type)

        # allowing the customer choose
        while True:
            item_number = input("\nEnter the item number you want to order (or type 'done' to finish): ").strip()
            if item_number.lower() == "done":
                break

            if item_number not in menu[meal_type]:
                print("Invalid item number.")
                continue
            
            qty_input = input("enter the quantity you want to order: ").strip()
            if qty_input.lower() == "done":
                break

            try:
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Quantity must be > 0")
                    continue
            except ValueError:
                print("Enter a valid quantity number")
                continue

            # getting the item selected
            item = menu[meal_type][item_number]
            # getting the subtotal
            subtotal = item['price'] * quantity
            running_total += subtotal  # <-- You forgot to add this

            print(f"Subtotal for {item['name']}: {subtotal} UGX")
            orders.append({
                "meal": meal_type,
                "item": item['name'], 
                "quantity": quantity,
                "subtotal": subtotal
            })
            print(f"Running Total: UGX {running_total} ,Order added successfully!") 
        
        # Ask if they want to order from another meal time
        more = input("\nDo you want to order from another meal time? (yes/no): ").lower()
        if more != "yes":
            break

def display_bill():
    print("\nEBENEZER RESTAURANT BILL")
    print("------------------------")
    total = 0
    for order in orders:
        print(f"{order['quantity']} x {order['item']} - {order['subtotal']} UGX")
        total += order['subtotal']
    print("------------------------")
    print(f"Total: {total} UGX")

def process_payment():
    global running_total
    total = sum(order['subtotal'] for order in orders)
    print(f"\nTotal amount due: {total} UGX")
    while True:
        payment = input("Enter payment amount (or type 'cancel' to cancel): ").strip()
        if payment.lower() == "cancel":
            print("Payment cancelled.")
            return 0, 0
        
        try:
            payment_amount = int(payment)
            if payment_amount < total:
                print(f"Insufficient payment. Need {total - payment_amount} UGX more.")
            else:
                change = payment_amount - total
                print(f"Payment accepted. Change: {change} UGX")
                return payment_amount, change
        except ValueError:
            print("Invalid input. Please enter a valid number.") 

# generating the receipt
def generate_receipt(paid, change):
    print("\nEBENEZER RESTAURANT RECEIPT")
    print("----------------------------")
    for order in orders:
        print(f"{order['quantity']} x {order['item']} - {order['subtotal']} UGX")
    total = sum(order['subtotal'] for order in orders)
    print("----------------------------")
    print(f"Total Bill: {total} UGX")
    print(f"Amount Paid: {paid} UGX")
    print(f"Change Due: {change} UGX")
    print("----------------------------")
    print("Thank you for dining with us!")

def main():
    display_menu()
    print("\nPlease place your order, ENTER YOUR MENU SELECTION: the meal type and item number!!!.")
    take_order()
    if orders:
        display_bill()
        paid, change = process_payment()
        if paid != 0:
            generate_receipt(paid, change)

main()