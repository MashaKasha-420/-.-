grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [4, 5, 5, 2]] #содержит списки оценок для каждого ученика в алфавитном порядке.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #содержит неупорядоченную последовательность имён всех учеников в классе.

students_sort = sorted(students)
grades_m = []
for i in grades:
     s = sum(i)/ len(i)
     grades_m.append(s)

dict1 = dict(zip(students_sort, grades_m))
print(dict1)
