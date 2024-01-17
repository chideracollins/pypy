import re

words = re.split(", |,| ", input("Enter the words, seperating each one from the other with a comma: "))

long_words = [""]
for i in words:
    if len(i) > len(long_words[0]):
        long_words.clear()
        long_words.append(i)
    elif len(i) == len(long_words[0]) and i not in long_words:
        long_words.append(i)

print("Here are the longest word(s): ", end="")
for x in long_words[:-1]:
    print(x, end=", ")
print(f"{long_words[-1]}.")