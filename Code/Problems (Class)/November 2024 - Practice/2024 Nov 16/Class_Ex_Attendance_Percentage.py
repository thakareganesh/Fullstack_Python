class Student:
    nwdays = 120
    cid = 1120
    def assign(self,sid,sname,npdays):
        self.sid = sid
        self.sname = sname
        self.npdays = npdays
    def calAttendance(self):
        self.ap = self.npdays / Student.nwdays * 100
    @staticmethod
    def clginfo():
        print("Collage Code is:",Student.cid)
        print("No. of working days is:",Student.nwdays)
    def display(self):
        print("Student ID:",self.sid)
        print("Student Name:",self.sname)
        print("Attendance Percentage:{:.2f}%".format(self.ap))

s1 = Student()
s1.assign(101,"Ganesh",85)
s1.calAttendance()
print("Student 1 - Information")
Student.clginfo()
s1.display()

s2 = Student()
s2.assign(102,"Mukesh",90)
s2.calAttendance()
print("Student 2 - Information")
Student.clginfo()
s1.display()