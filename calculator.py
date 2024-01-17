from math import sqrt
while True:
    op = int(input("Choose your operation:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for square root\n6 for power\n7 for Exit\n~"))

    if op in (1, 2, 3, 4, 6):
        x, y = input("Enter your operands: ").split(" ")
        x, y = int(x), int(y)
        if op == 1:
            result = x + y
        if op == 1:
            result = x + y
        elif op == 2:
            result = x - y
        elif op == 3:
            result = x * y        
        elif op == 4:
            result = x / y
        elif op == 6:
            result = x ** y
    elif op == 5:
        y = int(input("Enter only one value: "))
        result = sqrt(y)
    else:
        break
    print(result)
    