class School():
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
    
    def add_student(self, full_name, grade_level):
        if grade_level in self.roster.keys():
            students_in_grade = self.roster[grade_level]
            students_in_grade.append(full_name)
            self.roster[grade_level] = students_in_grade
        else:
            self.roster[grade_level] = [full_name]

    def grade(self, grade_level):
        return self.roster[grade_level]
    
    def sort_roster(self):
        for key in self.roster.keys():
            self.roster[key].sort()
        return self.roster


