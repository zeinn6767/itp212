numbers = [10, 20, 30, 40, 50, 60]
numbers.insert(3, 99)
print("1.", numbers)

tasks= ["email", "meeting", "report", "call"]
tasks.remove("meeting")
print("2.", tasks)

SIZE = 4
array = [10, 20, 30, 40]

if len(array) >= SIZE:
    print("3. Error: Array is full.")
else: 
    array.append(50)

print(array)

prices = [25, 40, 15, 60, 35]
lowest = prices[0]

for price in prices:
        if price < lowest:
            lowest = price

            print("4. lowest price:", lowest)

            ages = [12, 17, 20, 15, 22, 30]
            count = 0

            for age in ages:
                if age >= 18:
                    count += 1

                    print("5. Number of ages 18 or older:", count)

                    numbers = [10, 20, 30, 40, 50]
                    numbers.pop(0)
                    numbers.pop()
                    print("6.", numbers)    