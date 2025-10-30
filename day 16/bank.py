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

class bank(educational):
    
    def information(self,acc_num,branch_name,bank_name,ifsc_code,available_balance):
        self.acc_num = acc_num
        self.branch_name = branch_name
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.available_balance = available_balance

    def bank_info(self):
        print("bank acc_num",self.acc_num)
        print("bank branch_name",self.branch_name)
        print("bank bank_name",self.bank_name)
        print("ifsc_code",self.ifsc_code)
        print("available_balance",self.available_balance)

customer =  bank()

personal.information(customer,"divya","divya34@gamil.com","7865432587","45mainst.vadipatti")
educational.information(customer,[85,90,80,95,88],438,87.6)
customer.information("54332567896","vadipatti","SBI","SBI006536",56788)

customer.personal_info()
customer.educational_info()
customer.bank_info()
        




