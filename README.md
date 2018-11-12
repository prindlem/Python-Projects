We are going to create 2 classes:

1. Students
2. Assignments

The specification for these are as follows

Students
Properties
id - an integer representing the student id
first_name - a string representing the students first name
last_name - a string representing the students last name
assignments - a list of assignments
Constructor
Student(id, first_name, last_name)
So calling Student(123, "Sara", "smith") crates a new student with an id of 123, first name of Sara and last name of Smith.
Methods
get_full_name() - should return a string that combines the first and last name with a space, for example "Sara Smith".
get_assignments() - should return a list of all assignments the student has submitted.
get_assignment(name) - returns the first assignment in the list with a matching name. If no matching assignment is found it returns None.
get_average() - returns the average grade of all assignments equally weighted
ungraded assignments are not counted in the average
submit_assignment(assignment) - takes the supplied assignment and adds it to the list of the students submitted assignments
remove_assignment(name) - removes the first assignment with a matching name
Assignments
Properties
name - a string representing the assignment name
max_score - an integer representing the maximum possible score possible to get on the assignment
grade - an integer representing the actual score on the assignment
Constructor
Assignment(name, max_score) - instantiates a assignment with a name of name and a maximum score of max_score. The grade should be initialized to None
Methods
assign_grade(grade) - sets the grade to the supplied integer grade value. If grade is higher than max_score the grade should be set to None
Both of these should be defined in a file called classroom.py.

You should also create a file called classroom_test.py which imports classrom.py and tests it as follows:

It should create two students "Allen Allenson" and "Becky Beckyson" with ids of 123 and 456.

It should use the get_full_name method to get their name and print it along with their id numbers.

You should create two different instances of an assignment named "Assignment 1" and two instances of "Assignment 2" with a maximum score of 100.

Assign a grade of 75 and 85 to Assignment 1 and 2 and submit them to Allen.

Assign a grade of 90 and 100 to the other instances of Assignment 1 and 2 and submit them to Becky.

Use the get_assignment and get_full_name functions to get and print the scores of assignment 1 for Allen and Becky, printing out the name and the score.

Use the get_assignments function to get all of Beckys assignments printing out their name and grades.

Print the average grade of Becky.

Remove assignment 2 from Becky.

Print the average grade of Becky.
