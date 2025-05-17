class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name


class Student(Person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number = roll_number
        self.courses = []
        
    def register_for_course(self,course_name):
        self.courses.append(course_name)
        
        
class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.__salary = salary
        self.courses = []
        

class Course:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.students = []
        self.instructors = []
        
    def add_student(self,student_name):
        self.student_name = student_name
        self.students.append(self.student_name)
        print(f"{student_name} is added to course {self.name}.")
    
    def set_instructor(self,instructor_name):
        self.instructor_name = instructor_name
        self.instructors.append(self.instructor_name)
        print(f"{self.instructor_name} id added to the faculty for {self.name} course.")
        
    def enrolled_students(self):
        result = ''    
        for index,student in enumerate(self.students):
            result += f"\n{index + 1} - {student}"
        return result
        
class Department:
    def __init__(self,name):
        self.name = name
        self.courses = []           
        
    def add_course(self,course_name):
        self.course_name = course_name
        self.courses.append(course_name)
        print(f"{self.course_name} is added to the department {self.name}")
        

# create a department
cs_dept = Department("Computer Science")
print(cs_dept.courses)

# create a oop course
oop = Course(101,"Object Oriented Programming")
print(oop.name)

# add oop course in the department
cs_dept.add_course(oop.name)
print(cs_dept.courses)
cs_dept.add_course("Calculus")
print(cs_dept.courses)

# create an instructor and set it for oop course
instructor1 = Teacher("Hamzah",23,10000)
oop.set_instructor(instructor1.name)
print(oop.instructors)

# enroll studeents in the course
oop.add_student("Huzair")
oop.add_student("Huzaifa")
oop.add_student("Hamza")
print(oop.students)
