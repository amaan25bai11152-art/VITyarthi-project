import json
import random
import os
import math

# File name variable
fname = "college_data.json"
data = {}

# Check if file exists and load it
if os.path.exists(fname):
    f = open(fname, "r")
    try:
        data = json.load(f)
    except:
        data = {}
    f.close()

print("COLLEGE MONEY MANAGER")

while True:
    print("\n1. New Student")
    print("2. Login")
    print("3. Exit")

    op = input("Choice: ")

    if op == "1":
        n = input("Your Name: ")
        # Generate random number for ID
        r = random.randint(1000, 9999)
        uid = "STU" + str(r)

        data[uid] = {
            "name": n,
            "expenses": {}
        }
        print("Registered. ID: " + uid)

    elif op == "2":
        i = input("Enter ID: ")

        if i in data:
            stu = data[i]

            # Ask for today's date
            d = int(input("Today's Date (e.g. 5): "))

            # Fill in missing days
            print("Checking old days...")
            for x in range(1, d + 1):
                day_str = str(x)
                if day_str not in stu["expenses"]:
                    print("Day " + day_str + " is empty.")
                    cost = int(input("How much spent? "))
                    stu["expenses"][day_str] = cost

            # Calculate Average
            total = 0
            cnt = 0
            nums = []  # List to hold values for math later

            for k in stu["expenses"]:
                v = stu["expenses"][k]
                nums.append(v)
                total = total + v
                cnt = cnt + 1

            if cnt > 0:
                avg = total / cnt
            else:
                avg = 0

            # Calculate Standard Deviation manually
            sq_sum = 0
            for x in nums:
                diff = x - avg
                sq = diff * diff
                sq_sum = sq_sum + sq

            if cnt > 0:
                var = sq_sum / cnt
                sd = math.sqrt(var)
            else:
                sd = 0

            print("\nWelcome " + stu["name"])
            print("Total Spent: " + str(total))
            print("Average: " + str(int(avg)))
            print("Variation (Std Dev): " + str(int(sd)))

            # Logical Prediction
            low = avg - sd
            high = avg + sd
            if low < 0:
                low = 0

            print("\nPREDICTION:")
            print("Normal Range: " + str(int(low)) + " to " + str(int(high)))
            print("Safe limit for tomorrow: " + str(int(high)))

            # Budget check
            b = int(input("\nMonthly Budget (0 for no): "))
            if b > 0:
                rem = b - total
                days = 30 - d
                print("Remaining: " + str(rem))

                if days > 0:
                    per_day = rem / days
                    print("Spend max in rs " + str(int(per_day)) + " daily")

                if total > b:
                    print("Over Budget!")

            ch = input("\nEdit today's expense? (y/n): ")
            if ch == "y":
                new_amt = int(input("New amount: "))
                stu["expenses"][str(d)] = new_amt
                print("Done.")

        else:
            print("Wrong ID")

    elif op == "3":
        print("Bye")
        break

    # Save to file
    f = open(fname, "w")
    json.dump(data, f, indent=4)
    f.close()