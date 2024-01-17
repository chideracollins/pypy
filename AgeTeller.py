# An Age Telling Program in Detail
from datetime import datetime
from calendar import monthrange
currDate = datetime.date(datetime.now())
tYY, tMM, tDD= str(currDate).split("-")
tYY, tMM, tDD = int(tYY), int(tMM), int(tDD)
def findAge(a, b, c):
    global nYY, nMM, nDD
    monthLen = monthrange(tYY, (tMM - 1))
    monthLenght = monthLen[1]
    nYY = tYY - a - 1
    nMM = (12 - b) + (tMM - 1)
    nDD = monthLenght - c + tDD
    if nDD >= monthLenght:
        nDD = nDD - monthLenght
        nMM += 1
    if nMM >= 12:
        nMM -= 12
        nYY += 1
YY, MM, DD = input("Enter your date of birth (YYYY/MM/DD): ").split("/")
YY, MM, DD = int(YY), int(MM), int(DD)
findAge(YY, MM, DD)
print("You are " + str(nYY) + " year(s), " + str(nMM) + " month(s), and " + str(nDD) + " day(s) old.")
