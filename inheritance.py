#You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

lass Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
  def __init__(self, firstName, lastName, idNum, scores):
    super().__init__(firstName, lastName, idNum)
    self.scores = scores

  def calculate(self):
    Grade = sum(self.scores)//len(self.scores)
    if (90 <= Grade <=100):
      return "O"
    elif(80 <= Grade <=90):
      return "E"
    elif(70 <= Grade <=80):
      return "A"
    elif(55 <= Grade <=70):
      return "P"
    elif(40 <= Grade <=55):
      return "D"
    elif(Grade <=40 ):
      return "T"
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
