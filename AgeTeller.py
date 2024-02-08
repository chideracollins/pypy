# An Age Telling Program in Detail
from datetime import datetime
from calendar import monthrange

currDate = datetime.date(datetime.now())
tYY, tMM, tDD = str(currDate).split("-")
tYY, tMM, tDD = int(tYY), int(tMM), int(tDD)
print(tYY, tMM, tDD)


def findAge(year, month, day):
    global nYY, nMM, nDD
    monthLen = monthrange(tYY, (tMM - 1))
    print(monthLen)
    monthLength = monthLen[1]
    nYY = tYY - year - 1
    nMM = (12 - month) + (tMM - 1)
    nDD = monthLength - day + tDD
    if nDD >= monthLength:
        nDD = nDD - monthLength
        nMM += 1
    if nMM >= 12:
        nMM -= 12
        nYY += 1


YY, MM, DD = input("Enter your date of birth (YYYY/MM/DD): ").split("/")
YY, MM, DD = int(YY), int(MM), int(DD)
findAge(YY, MM, DD)
print(
    "You are "
    + str(nYY)
    + " year(s), "
    + str(nMM)
    + " month(s), and "
    + str(nDD)
    + " day(s) old."
)
