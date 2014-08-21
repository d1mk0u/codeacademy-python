grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    total = 0
    for i in grades:
        total =total + i
    return total
print grades_sum(grades)

def grades_average(grades):
    l = float(len(grades))
    average = 0
    average = grades_sum(grades) / l
    return average
print grades_average(grades)
