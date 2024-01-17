numbers = input("Enter your values (N/B: Only seperate values with single whitespace): ").split(" ")
num_sum = 0
for x in numbers:
    num_sum += int(x)
avg_calc = num_sum/len(numbers)
print(avg_calc)
