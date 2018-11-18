import json
from collections import defaultdict
'''
TO DO:
-Make a place to enter and validate the section/section priortiy choices
-If class choice was previously entered, make it throw an error
-Customized error messages
-individual logins
-THE SCHEDULING ALGORITHM

'''

class Scheduler:
  def __init__(self, class_list, prevkey, not_full, full, conflict, x):
    self.class_list = class_list
    self.prevkey = prevkey
    self.not_full = not_full
    self.full = full
    self.conflict = conflict
    self.x = x

  def studentInput(self):
    rawdata = open("classes.json").read()
    data = json.loads(rawdata)
    scheduler.makeClassList(data)
    studentClasses = open("studentClasses.txt","w")
    studentClasses = open("studentClasses.txt","a")
    #del scheduler.class_list[0]
    for x in range(5):
      student = "Student " + str(x+1)
      print (student + " choose your 4 classes: ")
      student = "Student " + str(x+1) + ":"
      studentClasses.write(student)
      for y in range (4):
        valid = False
        while valid == False:
          class_choice = input ('Enter name of class ' + str(y+1) + ': ')
          valid = scheduler.validateChoice(class_choice)

        section_choice = input
        studentClasses.write(class_choice)
        studentClasses.write(" ")
      studentClasses.write("\n")
    studentClasses.close()

  def validateChoice(self, choice):
    for i in scheduler.class_list:
      if i == choice:
        return True
    print("That is not a valid class. Please try again.")
    return False
  
  '''
  def getFileLength(self, filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
  '''

  def importClasses(self):
    #with open("classes.json") as json_file:
    rawdata = open("classes.json").read()
    data = json.loads(rawdata)
    print(data["Classes"]["CHEM1"]["b"]["credits"])
    print(data["Classes"]["CALC1"]["a"]["department"])

  def makeClassList(self, d):
    for key, value in d.items():
      if isinstance(value, dict) and key != 'a' and key != 'b' and key != 'c':
        scheduler.class_list.append(key)
        scheduler.makeClassList(value)
        #scheduler.printValues(value)
        #print("{0} : {1}".format(key, value))

  def publishUnderfilledClasses(self, d, e):
    for key, value in d.items():
      if key == 'a' or key == 'b' or key == 'c':
        #Find value inside of classes json file
        #print (scheduler.prevkey)
        #print (key)
        #print(len(value))
        #print(e[scheduler.prevkey][key]['size'])
        if len(value) < e[scheduler.prevkey][key]['size']:
          scheduler.not_full.append(scheduler.prevkey + " " + key)
        elif len(value ) == e[scheduler.prevkey][key]['size']:
          scheduler.full.append(scheduler.prevkey + " " + key)
        else:
          scheduler.conflict.append(scheduler.prevkey + " " + key)
      elif isinstance(value, dict):
        scheduler.prevkey = key
        scheduler.publishUnderfilledClasses(value, e)
    
  def resolveConflicts(self, d, b):
    scheduler.x = scheduler.x + 1
    for item in scheduler.conflict:
      if len(scheduler.conflict) == 0:
        #print('broken broken broken broken')
        return 0
      #print("0000000000000" + str(len(scheduler.conflict)))
      student_list = d["Classes"][item.split()[0]][item.split()[1]]
      for student in student_list:
        second_choice = item.split()[0] + " " + (b["Students"][student][item.split()[0]])[1]
        for item2 in scheduler.not_full:
          if second_choice == item2:
            #print("four four four four four four")
            #my_dict['myKey'].update({"nestedDictKey1" : a_value })
            #print(d["Classes"][item.split()[0]])
            #print(student_list)
            student_list.append(student)
            d["Classes"][item.split()[0]].update({item2.split()[1] : student_list})
            student_list.remove(student)
            d["Classes"][item.split()[0]].update({item2.split()[0] : student_list})
            #print(student_list)
            #print(d["Classes"][item.split()[0]])
            with open('schedule.json', 'w') as outfile: 
              json.dump(d, outfile)
            scheduler.full = []
            scheduler.not_full = []
            scheduler.conflict = []
            srawdata = open("schedule.json").read()
            sdata = json.loads(srawdata)
            crawdata = open("classes.json").read()
            cdata = json.loads(crawdata)
            brawdata = open("students.json").read()
            bdata = json.loads(brawdata)
            scheduler.publishUnderfilledClasses(sdata, cdata)
            #scheduler.resolveConflicts(sdata, bdata)
            if len(scheduler.conflict) == 0:
              return 0
              
      ''' get list of students in class
          take a look at each student's second choice
          ------students should already be in their first choice----
          go line by line and if a student's second choice is underfilled, move them to that class
          and put that class in the appropriate list
          remove class from contact list after it is resolved
          check at the end if the length of the focntact list is 0
        '''
  def printSchedule(self, d):
    for key, value in d.items():
      if isinstance(value, dict): 
        print(key)
        scheduler.printSchedule(value)
      else:
        print(key, value)
    
scheduler = Scheduler([], "", [], [], [], 0)
#scheduler.importClasses()
#scheduler.studentInput()
srawdata = open("schedule.json").read()
sdata = json.loads(srawdata)
crawdata = open("classes.json").read()
cdata = json.loads(crawdata)
brawdata = open("students.json").read()
bdata = json.loads(brawdata)
scheduler.publishUnderfilledClasses(sdata, cdata)
#print(scheduler.not_full)
#print(scheduler.full)
#print(scheduler.conflict)
scheduler.resolveConflicts(sdata, bdata)
#print(scheduler.not_full)
#print(scheduler.full)
#print(scheduler.conflict)
scheduler.printSchedule(sdata)
