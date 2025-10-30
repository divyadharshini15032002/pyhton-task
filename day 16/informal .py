class personal:
    def information(self,name,mail,moblie,address):
        self.name = name
        self.mail = mail
        self.moblie = moblie
        self.address = address

    def personal_info(self):
        print("personal name",self.name)
        print("personal mail",self.mail)
        print("personal moblie",self.moblie)
        print("personal address",self.address)

class educational(personal):
    def information(self,mark,total,percentage):
        self.mark = mark
        self.total = total
        self.percentage = percentage

    def educational_info(self):
        print("educational mark",self.mark)
        print("educational total",self.total)
        print("educational percentage",self.percentage)

student=educational()
personal.information(student,"divya","divya34@gamil.com","7865432587","45mainst.vadipatti")
student.information([85,90,80,95,88],438,87.6)
student.personal_info()
student.educational_info()

        
