class BankAccount:
    def __init__(self,minbal,curbal):
        self.__Minbal = minbal
        self.__Curbal = curbal

    @property
    def Minbal(self):
        return self.__minbal
    Minbal.setter
    def Minbal(self,n):
        self.__minbal = n
    @property
    def Curbal(self):
        return self.__curbal
    Curbal.setter
    def Curbal(self,n):
        self.__curbal = n

    def __str__(self):
        return f"Minimum Balance: {self.___minbal}\nCurrent Balance: {self.__curbal}"

    def withdraw(self,amount):
        if amount > self.__Curbal - self.__Minbal:
            raise Exception("Withdraw amount has exceed current balance")
        else:
            self.__Curbal -= amount
            print(f"Withdraw amont has occured successfully. {self.__Curbal}")


def main():
    b = BankAccount(1000,10000)

    a = b.withdraw(5000)
main()
    
            
