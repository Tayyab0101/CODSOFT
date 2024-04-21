class University:
  def __init__(self, name):
    self.name = name

  def show_details(self):
    print("University:", self.name)


class Department(University):
  def __init__(self, name, department_name):
    super().__init__(name)
    self.department_name = department_name

  def show_details(self):
    super().show_details()
    print("Department:", self.department_name)


class Student(Department):  # Remove Office from inheritance
  def __init__(self, name, department_name, student_name, department_object):  # Add department object
    super().__init__(self, name, department_name)
    self.student_name = student_name
    self.department_object = department_object  # Store department information

  def show_details(self):
    super().show_details()
    print("Student Name:", self.student_name)
    # You can access department details through the department_object here


class Faculty(Department):
  def __init__(self, name, department_name, faculty_name):
    super().__init__(name, department_name)
    self.faculty_name = faculty_name

  def show_details(self):
    super().show_details()
    print("Faculty Name:", self.faculty_name)


# Example usage:
uni = University("Example University")
dept = Department("Example University", "Computer Science")
student = Student("Example University", "Computer Science", "John Doe", dept)  # Pass department object
faculty = Faculty("Example University", "Computer Science", "Dr. Jane Smith")

uni.show_details()
print()
dept.show_details()
print()
student.show_details()  # Access department details through student.department_object if needed
print()
faculty.show_details()
