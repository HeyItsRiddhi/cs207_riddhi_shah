
from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

#Class Bank Account
class BankAccount():
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0
    
    def withdraw(self, amount):
        #Check for sufficient funds
        if(amount < 0):
            raise ValueError("Withdrawl amount must be positive")
        if(amount > self.balance):
            raise ValueError("Not sufficent funds for transaction! Balance = ",
                             self.balance, "and withdraw requested = ", amount)
        self.balance = self.balance - amount
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def __str__(self):
        return "{} has a {}.".format(self.owner, self.accountType.name)
    
    def __len__(self):
        class_name = type(self).__name__
        return "Balance of the account is: {: d}".format(class_name, self)

#Class BankUser
class BankUser():
    def __init__(self,owner):
        self.owner = owner
    
    def addAccount(self,accountType):
        #check if accountype already exists or create it
        if (accountType.value == 1):
            try:
                self.savingsAccount
                raise ValueError("An savings account already exists!")
            except AttributeError:
                self.savingsAccount = BankAccount(self.owner,accountType)
        if (accountType.value == 2):
            try:
                self.checkingsAccount
                raise ValueError("An checkings account already exists!")
            except AttributeError:
                self.checkingsAccount = BankAccount(self.owner,accountType)
    
    def deposit(self, accountType, amount):
        if (accountType.value == 1):
            try:
                self.savingsAccount
                self.savingsAccount.deposit(amount)
            except AttributeError:
                raise AttributeError("No savings account associated with this owner")
                
        if (accountType.value == 2):
            try:
                self.checkingsAccount
                self.checkingsAccount.deposit(amount)
            except AttributeError:
                raise AttributeError("No checkings account associated with this owner")
    
    def withdraw(self, accountType, amount):
        #check positivity of withdrawl amount
        if(amount < 1):
            raise ValueError("Withdrawl amount must be positive")
            
        if (accountType.value == 2):
            try:
                self.checkingsAccount
                if(amount > self.checkingsAccount.balance):
                    raise ValueError("Not sufficent funds for transaction! Balance = ",
                                     self.balance, "and withdraw requested = ", amount)
                self.checkingsAccount.withdraw(amount)
            except AttributeError:
                raise AttributeError("No checkings account associated with this owner")
    
    def getBalance(self, accountType):
        if (accountType.value == 1):
            try:
                self.savingsAccount
                return self.savingsAccount.balance
            except AttributeError:
                raise AttributeError("No savings account associated with this owner")
                
        if (accountType.value == 2):
            try:
                self.checkingsAccount
                return self.checkingsAccount.balance
            except AttributeError:
                raise AttributeError("No checkings account associated with this owner")
    def __str__(self):
        try:
            self.savingsAccount
            savings = "Savings account has {: d} funds".format(self.savingsAccount.balance)
        except AttributeError:
            savings = "No savings account"
        try:
            self.checkingsAccount
            checkings = "Savings account has {: d} funds".format(self.savingsAccount.balance)
        except AttributeError:
            checkings = "No savings account"
        return "{} has {} funds.".format(savings, checkings)

#Tests for Bank User
def test_addAccountMultipleCheckings():
    try:
        user = BankUser("riddhi")
        user.addAccount(AccountType.CHECKING)
        user.addAccount(AccountType.CHECKING)
    except ValueError as err:
        assert(type(err) == ValueError)

def test_addAccountMultipleSavings():
    try:
        user = BankUser("riddhi")
        user.addAccount(AccountType.SAVINGS)
        user.addAccount(AccountType.SAVINGS)
    except ValueError as err:
        assert(type(err) == ValueError)

def test_addAccountSavings():
    user = BankUser("riddhi")
    user.addAccount(AccountType.SAVINGS)
    assert(type(user.savingsAccount) == BankAccount)

def test_addAccountCheckings():
    user = BankUser("riddhi")
    user.addAccount(AccountType.CHECKING)
    assert(type(user.checkingsAccount) == BankAccount)

def test_noSavingsDeposit():
    try:
        user = BankUser("riddhi")
        user.deposit(AccountType.SAVINGS,100)
    except AttributeError as err:
        assert(type(err) == AttributeError)
        
def test_noCheckingsDeposit():
    try:
        user = BankUser("riddhi")
        user.deposit(AccountType.CHECKING,100)
    except AttributeError as err:
        assert(type(err) == AttributeError)

def test_deposit():
    user = BankUser("riddhi")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS,100)
    assert(user.getBalance(AccountType.SAVINGS) == 100)

def test_LackOfFunds():
    try:
        user = BankUser("riddhi")
        user.addAccount(AccountType.SAVINGS)
        user.deposit(AccountType.SAVINGS,100)
        user.withdraw(AccountType.SAVINGS,200)
    except ValueError as err:
        assert(type(err) == ValueError)


test_addAccountCheckings()
test_addAccountSavings()
test_addAccountMultipleCheckings()
test_addAccountMultipleSavings()
test_deposit()
test_noCheckingsDeposit()
test_noSavingsDeposit()
test_LackOfFunds()

#ATM Session Closure
def ATMSession(bankUser):
    def interface():
        while(True):
            inputMessage1 = 'Enter Option: \n 1)Exit \n 2)Create Account \n 3)Check Balance \n 4)Deposit \n 5)Withdraw \n'
            answer = input(inputMessage1)
            if (int(answer) == 1):
                break
            elif (int(answer) == 2):
                inputMessage2 = 'Enter Option: \n 1)Checkings \n 2)Savings \n'
                accountAns = input(inputMessage2)
                if(int(accountAns) == 2):
                    try:
                        bankUser.addAccount(AccountType.SAVINGS)
                        print("A savings account was created")
                        next
                    except ValueError:
                        print("Savings account already exists.")
                        next
                else:
                    try:
                        bankUser.addAccount(AccountType.CHECKING)
                        print("A checkings account was created")
                        next
                    except ValueError:
                        print("Checkings account already exists.")
                        next
            elif (int(answer) == 3):
                inputMessage2 = 'Enter Option: \n 1)Checkings \n 2)Savings \n'
                accountAns = input(inputMessage2)
                if(int(accountAns) == 2):
                    try:
                        balance = bankUser.getBalance(AccountType.SAVINGS)
                        print("Your current savings balance is ", balance)
                        next
                    except AttributeError: 
                        print("You do not have a savings account!")
                        next
                else:
                    try:
                        balance = bankUser.getBalance(AccountType.CHECKING)
                        print("Your current savings balance is ", balance)
                        next
                    except AttributeError: 
                        print("You do not have a checkings account!")
                        next
            elif (int(answer) == 4):
                inputMessage2 = 'Enter Option: \n 1)Checkings \n 2)Savings \n'
                accountAns = input(inputMessage2)
                inputMessage3 = 'Enter Amount: \n'
                amount = input(inputMessage3)
                while (amount < 1):
                    print("Amount need to be positive")
                    amount = input(inputMessage3)
                if(int(accountAns) == 2):
                    try:
                        bankUser.deposit(AccountType.SAVINGS,amount)
                        bankUser.getBalance(AccountType.SAVINGS)
                        print("Successful Deposit! Your current savings balance is ", balance)
                        next
                    except AttributeError: 
                        print("You do not have a savings account!")
                        next
                else:
                    try:
                        bankUser.deposit(AccountType.CHECKING,amount)
                        balance = bankUser.getBalance(AccountType.CHECKING)
                        print("Successful Deposit! Your current checkings balance is ", balance)
                        next
                    except AttributeError: 
                        print("You do not have a checkings account!")
                        next
            elif (int(answer) == 5):
                inputMessage2 = 'Enter Option: \n 1)Checkings \n 2)Savings \n'
                accountAns = input(inputMessage2)
                inputMessage3 = 'Enter Amount: \n'
                amount = input(inputMessage3)
                while (amount < 1):
                    print("Amount needs to be positive")
                    amount = input(inputMessage3)
                if(int(accountAns) == 2):
                    try:
                        bankUser.withdraw(AccountType.SAVINGS,amount)
                        bankUser.getBalance(AccountType.SAVINGS)
                        print("Successful Withdrawl! Your current savings balance is ", balance)
                        next
                    except AttributeError: 
                        print("You do not have a savings account!")
                        next
                    except ValueError:
                        print("You do not have enough funds!")
                        next
                else:
                    try:
                        bankUser.deposit(AccountType.CHECKING,amount)
                        balance = bankUser.getBalance(AccountType.CHECKING)
                        print("Successful Withdrawl! Your current checkings balance is ", balance)
                        next
                    except AttributeError: 
                        print("You do not have a checkings account!")
                        next
                    except ValueError:
                        print("You do not have enough funds!")
                        next
            else: 
                print("Did not enter a valid option!")
                next
    return interface