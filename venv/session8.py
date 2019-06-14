"""
student
 name
 phone
 email
 password
  isCollegeTraining
  college name
  rollNum


class students:
    pass
s1 = students()         #object is created here
s1.name= "john"
s1.phone = "+91 9999988888"
s1.email = "john@example.com"
s1.password = "pass123"
s1.isCollegeTraining = True
s1.collegeName = "abc international"
s1.rollNum = 22
print(s1.__dict__)

s2 = students()         #object is created here
s2.name= "jennie"
s2.phn = "+91 8888888888"
s2.email = "jennie@example.com"
s2.passphrase = "pass5555"
s2.isCollegeTraining = True
s2.collegeName = "xyz international"
s2.roll = 23

print(s2.__dict__)

students = [s1,s2]
print(students)
"""
class student:
    schoolName = "ATPL"
    #self is a reference varibale which will hold hashcode of current object
    #__init__ is known as constructtor
    # constructor is property of class

    def __init__(self,name,phone,email,password,iscollegetraining,collegename,rollnum):
        print("self is:",self)
        self.fullname = name
        self.phone = phone
        self.email = email
        self.password = password
        self.iscollegetraining = iscollegetraining
        self.collegename = collegename
        self.rollnum = rollnum




        #overwriting -> this is a new constructor will be created any old will be removed


"""
    def __init__(self,name,phone):
        self.name= name
        self.phone= phone"""
#      showStudentsDetails(self): is property of class
    #def showStudentsDetails(self):
       # print("details of:",self.fullname)
       # print("phone:\t",self.phone)
       # print("===========")

s1 = student("john","+91 9999988888","john@example.com","pass123", True,"abc internation",22)# student.__init__(s1,)
print("s1 is:",s1)
s2 = student("jennie","+91 888888888","jennie@example.com","pass5555", True,"xyz internation",23)
print("s2 is:",s2)

s1.age = 25
s1.vehicle = "pbx1"

s1.fullname = "john watson"
s2.fullname = "fienna flynn"
"""
print(s1.__dict__)
print(s2.__dict__)

#del s1.age
#del s1.phone
print()
print(s1.__dict__)
print(s2.__dict__)
"""
#s1.showStudentDetails()
#s2.showStudentsDetails()

print()
print(s1.__dict__)
print(student.__dict__)

