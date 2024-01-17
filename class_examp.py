'''caps_and_countries=[['Accra', 'Ghana'], ['Abuja', 'Nigeria']]
for cap_country in caps_and_countries:
    print(f"{cap_country[0]} is the capital of {cap_country[1]}")
'''


# num=int(input("enter a number"))
# count=2
# times=0
# while(count<=num/2):
#     if(num==0):
#         print("the number is 0")
#         break
#     if(num==1):
#         print("the number is 1")
#     if(num%count==0):
#         times+=1

# print([x for x in range(1, 1000, 2)])

# import time
# example_list=list(range(1000000))
# start_time=time.time()
# scalar_val=20
# result=[]
# for el in example_list:
#     result.append(el*scalar_val)
# end_time = time.time()
# print(f"finished in {end_time-start_time}")

import numpy as np
import time
start = time.time()
examp_arr = np.array(list(range(1,1000000)))
end1 = time.time()
res_arr = examp_arr * 20
print(f"finished in {end1-start}")
    