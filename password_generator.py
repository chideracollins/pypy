import random
password_lenght = 0
while password_lenght < 8 or password_lenght > 15:
    password_lenght = int(input("Plesase provide your password lenght that is not more than 15 characters nor less than 8 characters:\n"))
password_ch = {
    "alpha" : ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
               "num" : ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), "special_ch" : ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')')
               }
password = ""
while password_lenght > 0:
    ch_type = ("alpha", "num", "special_ch")
    char = password_ch[ch_type[random.randint(0,2)]][random.randint(0, 8)]
    password = password + char
    password_lenght -= 1
print("Your generated password is: " + password)

    
