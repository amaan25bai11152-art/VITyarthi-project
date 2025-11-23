# this is initial stock present in the machine alr111eady
water = 500
milk = 1000
coffee = 200
sugars = 400
icecream = 1000
chocolate = 500
choco_sparkles = 300


def owner(x):
    global water, milk, coffee, sugars, icecream, chocolate, choco_sparkles

    while True:
        quantity = int(input(f'Enter how much {x} you are adding: '))
        if x == 'water':
            water += quantity
        elif x == 'milk':
            milk += quantity
        elif x == 'coffee':
            coffee += quantity
        elif x == 'sugars':
            sugars += quantity
        elif x == 'icecream':
            icecream += quantity
        elif x == 'chocolate':
            chocolate += quantity
        elif x == 'choco_sparkles':
            choco_sparkles += quantity
        else:
            print('Enter a valid input')

        more = input("Do you want to add more? (y/n): ")
        if more.lower() != 'y':
            break


def user(h, q):
    global water, milk, coffee, sugars, icecream, chocolate, choco_sparkles

    if h == 1:  # Latte
        milk -= q / 2
        coffee -= q / 4
        sugars -= q / 4
        print(f"Latte prepared with {q / 2} milk, {q / 4} coffee, {q / 4} sugars")

    elif h == 2:  # Cappuccino
        milk -= q / 4
        coffee -= q / 4
        sugars -= q / 4
        print(f"Cappuccino prepared with {q / 4} milk, {q / 4} coffee, {q / 4} sugars")

    elif h == 3:  # Cold Coffee
        milk -= q / 4
        coffee -= q / 2
        sugars -= q / 4
        print(f"Cold Coffee prepared with {q / 4} milk, {q / 2} coffee, {q / 4} sugars")

        que = input("Do you want ice cream in cold coffee? (y/n): ")
        if que.lower() in ["yes", "y"]:
            quantity = int(input("Enter how much ice cream you want to add: "))
            icecream -= quantity
            print(f"Added {quantity} ice cream")

    elif h == 4:  # Choco Latte
        milk -= q / 2
        coffee -= q / 4
        chocolate -= q / 3
        choco_sparkles -= q / 5
        print(f"Choco Latte prepared with {q / 2} milk, {q / 4} coffee, {q / 3} chocolate, {q / 5} sparkles")

    else:
        print("Invalid choice")

    print("Remaining stock:", water, milk, coffee, sugars, icecream, chocolate, choco_sparkles)

while True:
    print("\n--- Coffee Machine Menu ---")
    print("1. User Mode")
    print("2. Owner Mode")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\n--- Coffee Menu ---")
        print("1. Latte")
        print("2. Cappuccino")
        print("3. Cold Coffee")
        print("4. Choco Latte")

        h = int(input("Select coffee type (1-4): "))
        q = int(input("Enter how much coffee you want: "))
        user(h, q)

    elif choice == '2':
        x = input("Enter what you want to add (water/milk/coffee/sugars/icecream/chocolate/choco_sparkles): ")
        owner(x)

    elif choice == '3':
        print("Exiting Coffee Machine... Goodbye!")
        break

    else:
        print("Invalid choice, try again.")