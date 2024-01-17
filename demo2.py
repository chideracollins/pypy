# A Program to Determine the Prime Numbers Within a Given Range of Numbers
rng_start, rng_stop = input("Enter the range: ").split("to")
if int(rng_start) % 2 == 0:
    rng_start = int(rng_start) + 1
rng = range(int(rng_start), int(rng_stop), 2)
for i in rng:
    if i < 4:
        print(i)
    else:
        t_f = True
        for j in range(3, i, 2):
            if i % j == 0:
                t_f = False
        if t_f == True:
            print(i)
