from random import randint


def print_integers():
    a, b = [int(x) for x in input("Enter range(1, 100): ").split(",")]
    rng = b - a + 1
    unic = []
    while rng > 0:
        num = randint(a, b)
        no_of_tries = 1
        while unic.__contains__(num):
            num = randint(a, b)
            no_of_tries += 1
        unic.append(num)
        print(f"After {no_of_tries} time(s)- {num}")
        rng -= 1

print_integers()