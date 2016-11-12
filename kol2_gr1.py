import json
import os
    
class School(object):
  
    def __init__(self):
        self.classes={}
      
    def add_class(self,class_name):
        self.classes[class_name]=Class(class_name)
  
    def load_from_file(self,filename):
        if os.path.isfile(filename):
            with open(filename) as file:
                data=json.load(file)
            self.parse_data(data)
                
    def save_to_file(self,filename):
        data={}
        for key in self.classes:
            data[key]=self.classes[key].students
        with open(filename, 'w') as outfile:
            json.dump(data, outfile) 
              
    def parse_data(self,data):
        for key in data:
            self.add_class(key)
            self.classes[key].students=data[key] 
            

class Class(object):

    def __init__(self,name):
        self.students={}
        self.name=name
      
    def add_person(self,name,surname):
       self.students[name+" "+surname] = {}
      
    def add_score(self,name,surname,score,subject):
        if not subject in self.students[name+" "+surname].keys():
            self.students[name+" "+surname][subject]=[score] 
        else:
            self.students[name+" "+surname][subject].append(score)


class Print_content(object):

    @staticmethod
    def print_average_subject(class_name,name,surname,subject):
        return str(sum(class_name.students[name+" "+surname][subject])/float(len(class_name.students[name+" "+surname][subject])))
    
    @staticmethod  
    def print_full_class_average_subject(class_name,subject):
        list_of_grades=[]
        for i in class_name.students:
            list_of_grades.extend(class_name.students[i][subject])
        return sum(list_of_grades)/float(len(list_of_grades))
    
    @staticmethod  
    def print_average_of_student(class_name,name,surname):
        list_of_grades=[]
        for s in class_name.students[name+" "+surname]:
            list_of_grades.extend(class_name.students[name+" "+surname][s])
        return sum(list_of_grades)/float(len(list_of_grades))
    
    @staticmethod  
    def print_full_class_average(class_name):
        list_of_grades=[]
        for i in class_name.students:
            for s in class_name.students[i]:
                list_of_grades.extend(class_name.students[i][s])
        return sum(list_of_grades)/float(len(list_of_grades))
              
      
if __name__=="__main__":
  
    szkola=School()
    szkola.load_from_file("data.json")
    szkola.classes["1f"].add_person("Stefan","Wykalaczka")
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",1,"biologia")
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",1,"biologia")
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",6,"chemia")  
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",3,"biologia")
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",1,"chemia")
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",5,"chemia")
    szkola.classes["1f"].add_score("Stefan","Wykalaczka",6,"chemia")
    
    print "srednia Janusz Rusek z biologii "+Print_content.print_average_subject(szkola.classes["1f"],"Janusz","Rusek","biologia")
    print "srednia Janusz Rusek z chemii "+Print_content.print_average_subject(szkola.classes["1f"],"Janusz","Rusek","chemia")
    print "srednia Ben Szybki z biologii "+Print_content.print_average_subject(szkola.classes["1f"],"Ben","Szybki","biologia")
    print "srednia Ben Szybki z chemii "+Print_content.print_average_subject(szkola.classes["1f"],"Ben","Szybki","chemia")
    print "srednia Stefan Wykalaczka z biologii "+Print_content.print_average_subject(szkola.classes["1f"],"Stefan","Wykalaczka","biologia")
    print "srednia Stefan Wykalaczka z chemii "+Print_content.print_average_subject(szkola.classes["1f"],"Stefan","Wykalaczka","chemia")
    print "srednia klasy z biologii "+str(Print_content.print_full_class_average_subject(szkola.classes["1f"],'biologia'))
    print "srednia Ben Szybki "+str(Print_content.print_average_of_student(szkola.classes["1f"],"Ben","Szybki"))
    print "srednia klasy ze wszystkich przedmiotow "+str(Print_content.print_full_class_average(szkola.classes["1f"]))
  
    #szkola.save_to_file("data.json")













