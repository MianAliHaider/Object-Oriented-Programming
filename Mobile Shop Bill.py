from datetime import datetime
from Address import Address
from datetime import datetime
class Bill:
    def __init__(self,bill_number,bill_date,customer_name,cell_no,address,shop_ad):
        self.__Bill_number = bill_number
        self.__Bill_date = bill_date
        self.__Customer_name = customer_name
        self.__Cell_no = cell_no
        self.__Address = address
        self.__Shop_ad = shop_ad
        self.__items = []
    
    @property
    def Bill_number(self):
        return self.__bill_number
    Bill_number.setter
    def Bill_number(self,n):
        self.__bill_number = n
    
    @property
    def Bill_date(self):
        return self.__bill_date
    Bill_date.setter
    def Bill_date(self,n):
        self.__bill_date = n
        
    @property
    def Customer__name(self):
        return self.__customer_name
    Customer__name.setter
    def Customer__name(self,n):
        self.__customer_name = n
    
    @property
    def Cell_no(self):
       return self.__cell_no
    Cell_no.setter
    def Cell_no(self,n):
       self.__cell_no = n
       
    @property
    def Address(self):
       return self.__address
    Address.setter
    def Address(self,n):
       self.__address = n
       
    @property
    def Shop_ad(self):
       return self.__shop_ad
    Shop_ad.setter
    def Shop_ad(self,n):
       self.__shop_ad = n
    
    def add_item(self,quantity,particulars,rate):
        item = {"quantity" : quantity, "particulars" : particulars, "rate" : rate}
        self.__items.append(item)
    
    def Totalamount(self):
        total = 0 
        for item in self.__items:
            total += item["quantity"] * item["rate"]
            return total
    
 
    def __str__(self):
        a = " _______________________________________________________________"
        a += "\n|                         Mobilo                                |"
        a += "\n|                       Mobile City                             |"
        a += "\n|               Deals in all kind of accessories                |"
        a += "\n|                   Cell NO: 0300-2569874                       |"              
        a += "\n|_______________________________________________________________|"
        a += f"\n|Customer Cell: "
        a += f"{str(self.__Cell_no).ljust(48)}|"
        a += f"\n|Bill Number: "
        a += f"{str(self.__Bill_number).ljust(50)}|"
        a += f"\n|Date: "
        a += f"{str(self.__Bill_date.strftime('%d-%b-%Y')).ljust(57)}|"
        a += f"\n|Customer Name: " 
        a += f"{str(self.__Customer_name).ljust(48)}| "
        a += f"\n|Customer Address: "
        a += f"{str(self.__Address).ljust(45)}|"
        a += "\n|_______________________________________________________________|\n"
        a += f"|{'Qty'.center(7)}|{'Particulars'.center(39)}|{'Rate'.center(7)}|{'Amount'.center(7)}|\n"

        a += "|---------------------------------------------------------------|\n"
        
        total = 0
        for item in self.__items:
            amount = item['quantity'] * item['rate']
            total += amount
            a += f"|{str(item['quantity']).center(7)}|{str(item['particulars']).center(39)}|{str(item['rate']).center(7)}|{str(amount).center(7)}|"
            a += "\n"
            a += "|---------------------------------------------------------------|\n"

        a += f"|Total:{str(total).rjust(57)}|\n"
        a += "|---------------------------------------------------------------|\n"
        a += f"|{str(self.__Shop_ad).ljust(63)}|\n"
        a += "|_______________________________________________________________|\n"
        return a
    
class Shop_Address:
    def __init__(self,shop_number,plaza,market,city):
        self.__Shop_number = shop_number
        self.__Plaza = plaza
        self.__Market = market
        self.__City = city
        
    
    @property
    def Shop_number (self):
        return self.__shop_number
    Shop_number.setter
    def Shop_Address (self,n):
        self.__shop_number = n
    
    @property
    def Plaza(self):
        return self.__plaza
    Plaza.setter
    def Plaza(self,n):
        self.__plaza = n
    
    
    @property
    def Market (self):
        return self.__market
    Market.setter
    def Market(self,n):
        self.__market = n
    
    @property
    def City (self):
        return self.__city
    City.setter
    def City(self,n):
        self.__city = n
        
    def __str__(self):
        a = "Address:  "
        a += str(self.__Shop_number)
        a += " , " 
        a += str(self.__Plaza)
        a += " , "
        a += str(self.__Market)
        a += " , "
        a += str(self.__City)
        return a
    
class Address:
    def __init__(self,home_number,town,city):
        self.__Home_number = home_number
        self.__Town = town
        self.__City = city
        
    @property
    def Home_number (self):
        return self.__home_number
    Home_number.setter
    def Home_number(self,n):
        self.__home_number = n
    @property
    def Town(self):
        return self.__town
    Town.setter
    def Town(self,n):
        self.__town = n
    
    @property
    def City(self):
        return self.__city
    City.setter
    def City(self,n):
        self.__city = n
    
    
    def __str__(self):
        a = str(self.__Home_number)
        a += "  "
        a += str(self.__Town)
        a += "  "
        a += str(self.__City)
        return a

def main():    
    

    address = (Address("000","Johr_Town","LHR"))
    shop_add = Shop_Address("000","Azam","Firdous","ISB")
    cus = str(input("Enter the Customer name: "))
    bill = Bill("95",datetime.now(),cus,"03000000000",address,shop_add)
    items = int(input("How much quantity you want to add: "))
    for i in range(items):
        quantity = int(input(f"How much quantity of item {i+1} is: "))
        particulars = str(input(f"What kind of item {i+1} is: "))
        rate = int(input(f"What is the rate of this item {i+1}: "))
        bill.add_item(quantity=quantity,particulars=particulars, rate = rate)
    print(bill)

    
    
if __name__=="__main__":
    main()
    
   

