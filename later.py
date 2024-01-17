op = int(input("Choose your operation:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for square root\n6 for power\n~"))
if op in (1, 2, 3, 4, 6):
    x, y = input("Enter your operands: ").split(" ")
    print(x,y)
