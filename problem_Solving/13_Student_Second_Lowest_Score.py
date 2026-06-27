# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.





students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
all_scores = [student[1] for student in students]
second_lowest = sorted(set(all_scores))[1]
    
names = [student[0] for student in students if student[1] == second_lowest]
names.sort()
for name in names:
    print (name)
        











    
