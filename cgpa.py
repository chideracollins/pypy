# A CGPA Calculator!


def sortInput(semester):
    course_list = {}
    course_no = input("How many courses offered for " + semester + "Semester? ")
    print("Okay\nProvide them below;")
    i = 1
    while i <= int(course_no):
        courseName, score, unitLoad = input(
            (str(i))
            + ") Please provide your course name, score and unit load (eg: GSP101 78 3): "
        ).split(" ")
        for j, y in {5: 30, 4: 40, 3: 50, 2: 55, 1: 60, 0: 100}.items():
            if (100 - int(score)) <= y:
                course_list[j] = int(unitLoad)
                break
        i += 1
    return course_list


def workGP(a, b):
    cgpa, c, q = 0, a, 1
    while q <= 2:
        list1 = []
        for j, k in c.items():
            list1.append(j * k)
        cgpa += sum(list1) / sum(c.values())
        c = b
        q += 1
    return cgpa / 2


def generateResult():
    global cgpa, years
    year = input("Which year?(First, Second...): ")
    years.append(year)
    course_list1 = sortInput("first ").copy()
    course_list2 = sortInput("second ").copy()
    cgpa += workGP(course_list1, course_list2)
    reply = input(
        "Your CGPA has been calculated, would you like to see it? (1) \nOr continue to provide your scores for other years? (2) (1/2): "
    )
    if reply == "2":
        generateResult()
    else:
        if len(years) == 1:
            print("Your CGPA for {} year is: ".format(year) + str(cgpa) + "\nCongrats!")
        elif len(years) > 1:
            cgpa = cgpa / len(years)
            print("Your total CGPA is: " + str(cgpa) + "\nCongrats!")


cgpa = 0
years = []
generateResult()
