#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.




class Class(object):
	def __init__(self):
		self.students={}
	def add_person(self,name,surname):
		self.students[(name,surname)] = [0,0]
	def add_score(self,name,surname,score):
		self.students[(name,surname)][0]+=float(score)
		self.students[(name,surname)][1]+=float(1)
	def print_average(self,name,surname):
		return str(self.students[(name,surname)][0]/self.students[(name,surname)][1])
if __name__=="__main__":
	test=Class()
	test.add_person("a","b")
	test.add_score("a","b",3)
	test.add_score("a","b",5)
	print test.print_average("a","b")



