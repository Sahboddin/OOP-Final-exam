class User:
    def __init__(self) -> None:
        self.name = ''
        self.User_balance=0
        self.loan=0
        self.transaction_history = []

    def create_account(self, name, phone, nid):
        self.name = name
        self.phone = phone
        self.nid = nid

    def deposit(self,deposit_amount):
        if deposit_amount > 0:
            self.User_balance += deposit_amount
            admin1.total_bank_balance += deposit_amount
            self.transaction_history.append(f"The deposited balance is : {deposit_amount} TK.")
        else:
            print("Cannot Deposit this negetive balance")

    def withdrawal(self,withdrawal_amount):
        if withdrawal_amount <= self.User_balance:
            self.User_balance -= withdrawal_amount
            admin1.total_bank_balance -= withdrawal_amount
            self.transaction_history.append(f"The withdraw balance is : {withdrawal_amount} TK.")
            return withdrawal_amount
        else: 
            return "The bank is bankrupt."
    
    def available_balance(self):
        return self.User_balance
    
    def transfer_amount(self,another_user_account,T_money):
        if T_money <=  self.User_balance:
            self.User_balance -= T_money
            another_user_account.deposit(T_money)
            self.transaction_history.append(f"The transfer balane is : {T_money} TK.")
        else:
            print(f"insufficient balance on {self.name} account")


    def user_transaction_history(self):
        return self.transaction_history

    def take_loan(self,admin):
        if self.User_balance > 0:
            self.loan = 2*self.User_balance
            self.User_balance += self.loan
            admin.give_loan(self.loan)
        else:
            print("You don't have enough balace to take loan")


class Admin(User):
    def __init__(self) -> None:
        self.total_bank_balance = 0
        self.total_bank_loan = 0
        self.loan_feature = False
        super().__init__()

    def create_account(self, name, phone, nid, admin_id):
        self.admin_id = admin_id
        return super().create_account(name, phone, nid)
    
    def total_balance(self):
        return self.total_bank_balance

    def total_loan(self):
        return self.total_bank_loan

    def enable_loan(self):
        self.loan_feature = True

    def disable_loan(self):
        self.loan_feature = False

    def give_loan(self, loan_amount):
        if loan_amount <= self.total_bank_balance:
            if self.loan_feature == True:
                self.total_bank_loan += loan_amount
                self.total_bank_balance -= loan_amount
                self.transaction_history.append(f"The loan : {loan_amount} TK.")
        else:
            print(f"Your loan request feature is currently off")

    
admin1 = Admin()
admin1.create_account("admin",133434,223232,2233)

user1 = User()
user2 = User()
user3 = User()

user1.create_account("shahab",199999,874832740)
user1.deposit(10000)
user1.withdrawal(5000)
print(f"the available balance is : {user1.available_balance()} TK.")
user1.transfer_amount(user2,100)
print(user1.user_transaction_history())
print(f"the available balance is : {user1.available_balance()} TK.")
print(user1.user_transaction_history())

admin1.enable_loan()

user2.create_account("jalal",84335,947385)
user2.deposit(100)
user2.withdrawal(50)
print(f"the available balance is : {user2.available_balance()} TK.")
user2.take_loan(admin1)
print(user2.user_transaction_history())

print(f"Total balance in the bank : {admin1.total_balance()} TK.")
print(f"Total Loan in the bank : {admin1.total_loan()} TK.")

admin1.disable_loan()

user3.create_account("abul",9333,49343)
user3.deposit(10000)
user3.withdrawal(500)
print(f"the available balance is : {user3.available_balance()} TK.")
user3.transfer_amount(user2,1000)
print(user3.user_transaction_history())
print(f"the available balance is : {user3.available_balance()} TK.")
print(user1.user_transaction_history())
user3.take_loan(admin1)
print(user3.user_transaction_history())


print(f"Total balance in the bank : {admin1.total_balance()} TK.")
print(f"Total Loan in the bank : {admin1.total_loan()} TK.")