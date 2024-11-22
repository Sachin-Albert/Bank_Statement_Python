class Bank_account:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(f"Balance is: Rs.{self.balance:.2f}")
    def deposit(self):
        amount = float(input('Enter The Amount : '))
        if amount<=0:
            print( 'Please Enter Amount Greater Than 0')
        else:
            self.balance += amount

    def withdraw(self):
        amount = float(input('Enter The Amount For Withdraw : '))
        if amount>self.balance:
            print('Insufficient Funds')
        else:
            self.balance -= amount

    def exits(self):
        print("Exited ...")
        exit()

    print('BANK STATEMENT')
    print('--------------')
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Exit...')

    def menu(self):
        while True:
            choice = int(input('Enter Operation To Perform : '))

            if choice == 1:
               self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.exits()
            else:
                print('Invalid Choice..Please Choose Valid Choice...')

obj = Bank_account()
obj.menu()