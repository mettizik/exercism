class School(object):
    def __init__(self, schoolname):
        self.name = schoolname
        self.grades = {}

    def add(self, student, grade):
        if grade in self.grades:
            self.grades[grade].append(student)
        else:
            self.grades[grade] = [student]

    def sort(self):
        return tuple([
            (grade, self.grade(grade)) for grade, students in self.grades.items()
        ])

    def grade(self, grade):
        if grade not in self.grades:
            return []
        
        return tuple(sorted(self.grades[grade]))
