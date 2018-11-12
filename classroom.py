class Assignments:
    def __init__(self, name, max_score, grade):
        self.name = name
        self.max_score = max_score
        self.grade = grade

    def Assignment(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = None


    def assign_grade(self, grade):
        if self.max_score < grade:
            self.grade = None
        else:
            self.grade = grade

class students(Assignments):
    def __init__ (self, id, first_name, last_name, assignments):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = assignments

    def __Student__ (self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        assignments = []
        print("New student created")

    def get_full_name(self):
        return(str(self.id) + ': ' + str(self.first_name) + ' ' + str(self.last_name))

    def get_assignments(self):
        return(self.assignments)

    def get_assignment(self, assignment_name):
        if any(assignment_name in s for s, j in self.assignments):
            return_grade = [j for i,j in self.assignments if i == assignment_name]
            return(('Assignment = ' + assignment_name, 'Grade = '+ str(return_grade[0])))
        else:
            None

    def get_average(self):
        numofAssignment = len(self.assignments)
        totalPoints = sum(j for i, j in self.assignments)
        average = totalPoints / numofAssignment
        return(average)

    def submit_assignment(self, Assignment):
        self.assignments.append((Assignment.name, Assignment.grade))

    def remove_assignment(self, assignment_name):
        self.assignments = [i for i in self.assignments if i[0] != assignment_name]
