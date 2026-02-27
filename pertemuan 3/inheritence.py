class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass 

x = Person("John", "Doe")
x.printname() 
x = Student("Mike", "Olsen")
x.printname()

#fungsi __init__()
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 

#fungsi super()
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 

#tambahkan properti
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019) 

#method
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 