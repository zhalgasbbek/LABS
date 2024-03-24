class Person:
    def __init__(self , fname ,lname):
        self.firstname = fname
        self.lastname  = lname
    def printname(self):
        print(self.firstname , self.lastname)
x = Person("John" , "Doe")
x.printname()


class Student(Person):
  pass


x = Student("Mike" , "Olsen")
x.printname()


class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.




    class Person:
       def __init__(self, fname, lname):
         self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()



class Person:
    def __init__(self ,fname , lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname , self.lastname)
class student(Person):
    def __init__(self , fname , lname):
       super().__init__(fname , lname)
       self.graduationyear = 2019
       
x = student("Mike" , "Olsen")
print(x.graduationyear)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()