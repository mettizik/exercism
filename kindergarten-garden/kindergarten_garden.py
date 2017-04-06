from textwrap import wrap

default_students = [
    'Alice', 'Bob', 'Charlie', 'David', 
    'Eve', 'Fred', 'Ginny', 'Harriet', 
    'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

plants = dict([(plant[0:1], plant) for plant in ['Violets', 'Clover', 'Radishes', 'Grass']])

def _students_plants(student_id, row):
    return row[student_id:student_id + Garden._each_student_plants]

class Garden(object):
    _each_student_plants = 2
    def __init__(self, garden_rows: str, students=None):
        if students is None:
            students = default_students        
        students = sorted(students)
        rows = garden_rows.split('\n')
        rows = [wrap(rows[0], 2), wrap(rows[1], 2)]        
        self.students = {}
        for i in range(len(rows[0])):
            self.students[students[i]] = [plants[key] for key in rows[0][i] + rows[1][i]]

    def plants(self, student):
        return self.students[student]
