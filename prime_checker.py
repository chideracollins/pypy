num = int(input("Enter a number: "))
for n in range(2, num//2):
    if num % n == 0:
        print(f"{num} is not a prime number")
        break
    elif n == num-1:
        print(f"{num} is a prime number")
        