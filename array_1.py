numbers = [27, 45, 69, 65, 62]
total = 0
highest = numbers[0]
for number in numbers:  
    total += number
    if number > highest:
     highest = number

average = total / len(numbers)

print("Total sum:", total)
print("Average:", f"{average:.2f}")
print("Highest value:", highest)


