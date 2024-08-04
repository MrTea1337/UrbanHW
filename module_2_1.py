grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']

sorted_students = list(students)
sorted_students.sort()                                      # Получения алфавитного списка студентов

i = 0
average_grades = []
while i < len(grades):
    average_grades.append(sum(grades[i]) / len(grades[i]))
    i += 1                                                  # Получение списка средник оценок

student_GPA = dict(zip(sorted_students, average_grades))
print(student_GPA)                                          # Объеденение списков в словарь
