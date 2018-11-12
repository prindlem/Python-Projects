from operator import itemgetter, attrgetter, methodcaller

#This is an example of the structure of a student dictionary
#They have an id number
#They have a first name, last name and a list of assignments
#Assignments are tuples of an assignment name and grade
#The grade is a 4 point scale from 0 to 4

student_list = [
    {'id':12346, 'first_name':'Alice', 'last_name':'Anderson',
'assignments':[('assignment_1',0),('assignment_2',2),('assignment_3',4)]},
    {'id':12345, 'first_name':'Wendy', 'last_name':'Anderson',
'assignments':[('assignment_1',0),('assignment_2',2),('assignment_3',4)]},
    {'id': 1234, 'first_name': 'Ben', 'last_name': 'Green',
     'assignments': [('assignment_1', 0), ('assignment_2', 2), ('assignment_3', 4)]}
]

singleStudent = {'id':12346, 'first_name':'Alice', 'last_name':'Anderson',
'assignments':[('assignment_1',2),('assignment_2',4),('assignment_3',4)]}

#This should return the average grade of all assignments from all students
#every assignment is equally weighted
def average_grade(students):
    averageList = []
    for student in students:
        numofAssignment = len(student['assignments'])
        totalPoints = sum(j for i, j in student['assignments'])
        average = totalPoints/numofAssignment
        averageList.append(average)
    classAverage = sum(averageList)/len(averageList)
    return(classAverage)

#This function should return a list of the n student dictionaries with the
#highest grades on the assignment passed in as assignment name
#If there is a tie then it is broken by returning the student(s) with the
#lowest id number(s)
def highest_n_grades(students, assignment_name, n):
    keys = list()
    for num in range(0,len(students)):
        assignmentDict = dict(students[num]['assignments'])
        keys.append((students[num]['id'],assignmentDict[assignment_name]))
        keys.sort()
        keys.sort(key=lambda tup: tup[1], reverse=True)
        filteredKeysList = keys[:n]
        filteredIds = [i[0] for i in filteredKeysList]
        finalList = list(filter(lambda d: d['id'] in filteredIds, students))
    return(sorted(finalList, key=lambda k: k['id']) )

#This function should accept a student dictionary, a string representing
#an assignment name and a grade. If that assignment name does not exist
#the assignment and grade should be added to the end of the list of assignments. If
#this was successful it should return true, otherwise it should return false.
def add_grade(student, assignment_name, grade):
    if [item for item in student['assignments'] if assignment_name in item]:
        return(False)
    else:
        student['assignments'].append((assignment_name, grade))
        return(True)

#This function should accept a student dictionary, a string
#representing an assignment name and a grade. If that assignment name exists
#the grade should be changed to the supplied grade. If the assignment was found
#and updated the function should return true, otherwise it should return false.
#The order of assignments should be preserved.
def update_grade(student, assignment_name, grade):
    if [item for item in student['assignments'] if assignment_name in item]:
        for i, t in enumerate(student['assignments']):
            if t[0] == assignment_name:
                student['assignments'][i] = assignment_name, grade
                break
        return(True)
    else:
        return(False)

#Write a function called passing_student_ids which accepts as an argument a list
#of students. It should return a list of student ids which represent students
#having an average grade on all of their assignments which is >= 2.0
def passing_student_ids(students):
    averageList = []
    finalList = []
    for student in students:
        numofAssignment = len(student['assignments'])
        totalPoints = sum(j for i, j in student['assignments'])
        average = totalPoints/numofAssignment
        averageList.append((student['id'], average))
        filterList = list(filter(lambda x: x[1] >= 2.0, averageList))
        finalList = [a[0] for a in filterList]
    return(finalList)


#Variables
numberOfStudents = 2
assign_name = 'assignment_3'
newassign_name = 'assignment_4'
student_grade = 3

#Print results
print(average_grade(student_list))

print(highest_n_grades(student_list, assign_name, numberOfStudents))

print(add_grade(singleStudent, newassign_name, student_grade))

print(update_grade(singleStudent, assign_name, student_grade))

print(passing_student_ids(student_list))