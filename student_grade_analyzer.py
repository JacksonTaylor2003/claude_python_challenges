grades = {
    "Alice": [85, 92, 78],
    "Bob": [60, 55, 70],
    "Charlie": [90, 95, 100],
    "Dana": [72, 68, 75],
}

def analyze_grades(grades:dict):
    averages = {}
    for student in grades:
        averages[student] = round(sum(grades[student])/len(grades[student]), 1)
    return averages

def top_student(grades):
    averages = analyze_grades(grades)
    averages = sorted(averages.items(), key=lambda item: item[1], reverse=True)
    return averages[0][0]

def passing_students(grades, threshold=70):
    averages = analyze_grades(grades)
    passing = {}
    for item in averages.items():
        if item[1] >= threshold:
            passing[item[0]] = item[1]

    return passing



print(analyze_grades(grades))
print(top_student(grades))
print(passing_students(grades))