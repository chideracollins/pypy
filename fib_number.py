index = int(input("Which fibonacci number will you like to see: "))
prev_num, curr_num = 0, 1

for x in range(3,index+1):
    fib_num = prev_num + curr_num
    prev_num = curr_num
    curr_num = fib_num
print(fib_num)