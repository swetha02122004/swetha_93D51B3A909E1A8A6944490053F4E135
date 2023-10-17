class student:
  def __init__(self,name,roll_no,cgpa):
    self.name=name
    self.roll_no=roll_no
    self.cgpa=cgpa
def sort_stud(stud_list):
  sort_stud=sorted(stud_list,key=lambda student:student.cgpa,reverse=True)
  return sort_stud
student=[student("manc","001",9.0),
         student("vishnu","002",9.8),
         student("pavi","003",8.4),
         student("hari","004",7.2),
         student("harshi","005",7.8)]
sort_stud=sort_stud(student)

for student in sort_stud:
  print("Name:{}   Roll_no:{}   CGPA : {}".format(student.name,student.roll_no,student.cgpa))