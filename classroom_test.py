from classroom import students, Assignments



aa_student = students(123, 'Allen', 'Allenson', [])
bb_student = students(456, 'Becky', 'Beckyson', [])

print(aa_student.get_full_name())
print(bb_student.get_full_name())

assign1 = Assignments("Assignment 1", 100, 0)
assign2 = Assignments('Assignment 2', 100, 0)

assign1.assign_grade(75)
assign2.assign_grade(85)
print(assign1.grade)

aa_student.submit_assignment(assign1)
aa_student.submit_assignment(assign2)

assign1.assign_grade(90)
assign2.assign_grade(100)
print(assign1.grade)

bb_student.submit_assignment(assign1)
bb_student.submit_assignment(assign2)

assign1.assign_grade(75)
print(aa_student.get_full_name() + ' - ' + aa_student.get_assignment("Assignment 1")[1])
assign1.assign_grade(90)
print(bb_student.get_full_name() + ' - ' + aa_student.get_assignment("Assignment 1")[1])

print(bb_student.get_assignments())

print(bb_student.get_average())
bb_student.remove_assignment("Assignment 2")
print(bb_student.get_average())



