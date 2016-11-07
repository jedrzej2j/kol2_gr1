class School(object):
  def __init__(self):
    self.classes={}
  def add_class(self,class_name):
    self.classes[class_name]=Class(class_name)

class Class(object):
  def __init__(self,name):
    self.students={}
    self.name=name
    self.subjects=[]
  def add_person(self,name,surname):
    self.students[(name,surname)] = {}
  def add_score(self,name,surname,score,subject):
    if not subject in self.students[(name,surname)].keys():
      self.students[(name,surname)][subject]=[float(score),float(1)] 
    else:
      self.students[(name,surname)][subject][0]+=float(score)
      self.students[(name,surname)][subject][1]+=float(1)
  def add_subject(self,subject_name):
    if subject_name not in self.subjects:
      self.subjects.append(subject_name)
  def print_average_subject(self,name,surname,subject):
    return str(self.students[(name,surname)][subject][0]/self.students[(name,surname)][subject][1])
  def print_full_class_average_subject(self,subject):
    full_sum=0
    full_number=0
    for i,j in self.students:
      full_sum+=self.students[i,j][subject][0]
      full_number+=self.students[i,j][subject][1]
    return full_sum/full_number
  def print_average(self,name,surname):
    full_sum=0
    full_number=0
    for s in self.students[name,surname]:
      full_sum+=self.students[name,surname][s][0]
      full_number+=self.students[name,surname][s][1]
    return full_sum/full_number
  def print_full_class_average(self):
    full_sum=0
    full_number=0
    for i,j in self.students:
      for s in self.students[i,j]:
        full_sum+=self.students[i,j][s][0]
        full_number+=self.students[i,j][s][1]
    return full_sum/full_number
      
if __name__=="__main__":
  
  szkola=School()
  szkola.add_class("1f")

  szkola.classes["1f"].add_person("Janusz","Rusek")
  szkola.classes["1f"].add_score("Janusz","Rusek",3,"biologia")
  szkola.classes["1f"].add_score("Janusz","Rusek",1,"biologia")
  szkola.classes["1f"].add_score("Janusz","Rusek",3,"chemia")
  print "srednia Janusz Rusek z biologii "+szkola.classes["1f"].print_average_subject("Janusz","Rusek","biologia")
  print "srednia Janusz Rusek z chemii "+szkola.classes["1f"].print_average_subject("Janusz","Rusek","chemia")

  szkola.classes["1f"].add_person("Ben","Szybki")
  szkola.classes["1f"].add_score("Ben","Szybki",1,"biologia")
  szkola.classes["1f"].add_score("Ben","Szybki",1,"chemia")
  szkola.classes["1f"].add_score("Ben","Szybki",3,"chemia")
  szkola.classes["1f"].add_score("Ben","Szybki",5,"chemia")
  print "srednia Ben Szybki z biologii "+szkola.classes["1f"].print_average_subject("Ben","Szybki","biologia")
  print "srednia Ben Szybki z chemii "+szkola.classes["1f"].print_average_subject("Ben","Szybki","chemia")
  
  print "srednia klasy z biologii "+str(szkola.classes["1f"].print_full_class_average_subject('biologia'))
  print "srednia Ben Szybki "+str(szkola.classes["1f"].print_average("Ben","Szybki"))
  print "srednia klasy ze wszystkich przedmiotow "+str(szkola.classes["1f"].print_full_class_average())














