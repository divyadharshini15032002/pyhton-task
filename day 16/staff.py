class school:
    def information(self,name,mail,moblie,address):
        self.name = name
        self.mail = mail
        self.moblie = moblie
        self.address = address

    def school_info(self):
        print("personal name",self.name)
        print("personal mail",self.mail)
        print("personal moblie",self.moblie)
        print("personal address",self.address)

class staff(school):
    def  information (self,name,mail,moblie,address,dept):
        super().information(name,mail,moblie,address,dept)
        self.dept = dept

    def staff_info(self):
            print("staffinformation:")
            self.school_info()
            print("staff_info",self.dept)


class student(school):
    def student_info(self,name,mail,moblie,address,dept):
        super().information(name,mail,moblie,address,dept)
        self.dept = dept

    def student_info(self):
        self.school_info()
        print("student_info",self.dept)

print("Are you a student or staff?")
user_choice = input("Enter 'student' or 'staff':").strip().lower()

sch = student()
student.information(sch,"divya","divya34@gamil.com","7865432587","45mainst.vadipatti")
staff.information(sch,"divya","divya34@gamil.com","7865432587","45mainst.vadipatti","ece")
school.information(sch,"divya","divya34@gamil.com","7865432587","45mainst.vadipatti")

sch.student_info()
sch.staff_info()
scg.school_info()
