class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    
    def checkBalance(self):
        print('Your Present Balance Is 15000')
   
    def withdrawl(self,amount):
        newAmount=15000-amount
        print('Your Withdrawl Amount Is '+str(amount)+'. Your Present Balance Is '+str(newAmount))
    
    def deposit(self,amount):
        newAmount2=15000+amount
        print('Your Deposit Amount Is '+str(amount)+'. Your Present Balance Is '+str(newAmount2))

def main():
    cardNumber=input('Insert Your Card Number: ')
    
    pinNumber=input('Enter Your Pin Number: ')
    
    user=Atm(cardNumber,pinNumber)
    print('Choose Your Activity')
    print('1. Balance Enquiry  2. Withdrawl  3. Deposit')
    
    activity=int(input('Enter Activity Number: '))

    if(activity==1):
        user.checkBalance()
    elif(activity==2):
        amount=int(input('Enter The Amount: '))
        user.withdrawl(amount)
    elif(activity==3):
        amount=int(input('Enter The Amount: '))
        user.deposit(amount)
    else:
        print('Enter A Valid Number')

if __name__=='__main__':
    main()