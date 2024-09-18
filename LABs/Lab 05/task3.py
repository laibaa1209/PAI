class Account:
    __account_no = 0
    __account__bal = 0.0
    __security_code = 0.0

    def initializze_data(self, num, bal, code):
        self.__account_no = num
        self.__account__bal = bal
        self.__security_code =  code

    def print_data(self):
        print(f"Account number: {self.__account_no}\nAccount balance: {self.__account__bal}\nSecurity Code: {self.__security_code}")

a = Account()

a.initializze_data(2345, 45670, 76532)
a.print_data()