import sqlite3
from datetime import datetime,timedelta

def create_members_table():
    con = sqlite3.connect("Library.db")
    cur =con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS MEMBERS (membership_number TEXT, member_full_name TEXT ,  address TEXT, contact_number INTEGER ,category TEXT , membership_start_date TEXT , membership_expiry_date TEXT, membership_closing_date TEXT , fine_paid REAL)")
    con.commit()
    cur.close()

def add_members():
    membership_number = str(input("Enter Mambership number: "))
    member_full_name = str(input("Enter Full name of Member: "))
    address = str(input("Enter address of member: "))
    contact_number = str(input("Enter contact Number: "))
    category = str(input("Enter Category (A, B, C and M)")).upper()
    membership_start_date = str(input("ENter Menbership start date (YYYY-MM-DD): "))
    membership_expiry_date = expiry_date(membership_start_date ,category)
    membership_closing_date = None
    fine_paid = 0.0

    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("INSERT INTO MEMBERS (membership_number, member_full_name, address, contact_number, category, membership_start_date , membership_expiry_date , membership_closing_date , fine_paid) VALUES (?,?,?,?,?,?,?,?,?)", (membership_number, member_full_name,address,contact_number,category , membership_start_date,membership_expiry_date,membership_closing_date,fine_paid ) )
    print("Member added Successfully.")
    con.commit()
    cur.close()

def expiry_date(membership_start_date,category):
    membership_start_date = datetime.strptime(membership_start_date,"%Y-%m-%d")
    year = 365
    if category =="A":
        expiry_date = membership_start_date + timedelta(days = year * 5)
    elif category == "B":
        expiry_date = membership_start_date + timedelta(days = year * 3)
    elif category == "C":
        expiry_date =  membership_start_date + timedelta(days = year * 1)
    elif category == "M":
        expiry_date = membership_start_date + timedelta(days =  year * 1)
    else:
        raise Exception ("INVALID CATEGORY. ")
    return expiry_date.strftime("%Y-%m-%d")

def search_members():
    membership_number = str(input("ENter Membership Number: "))
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT membership_number, member_full_name, address, contact_number, category, membership_start_date , membership_expiry_date , membership_closing_date , fine_paid FROM MEMBERS WHERE membership_number = ?" ,(membership_number,))
    member=cur.fetchone()
    if member:
        print(member)
    else:
        ("Membership Number Not Found")
    con.commit()
    cur.close()

def list_all_members():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT membership_number, member_full_name, address, contact_number, category, membership_start_date , membership_expiry_date , membership_closing_date , fine_paid FROM MEMBERS ")
    members = cur.fetchall()
    con.commit()
    cur.close()
    if members :
        for row in members:
            print(row)
    else:
        print("Members not available. ")
    
def delete_member():
    membership_number = str(input("Enter Membership Number: "))
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("DELETE FROM MEMBERS WHERE membership_number = ?", (membership_number,)) 
    print("Deleted Successfully.")
    con.commit()
    cur.close()

def extend_expiry_date():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    membership_number = str(input("Enter membership number: "))
    required_expiry_date = str(input("Enter new Expiry date: "))
    cur.execute("SELECT membership_expiry_date FROM MEMBERS WHERE membership_number = ? ",(membership_number,))
    expiry_date = cur.fetchone()
    if expiry_date:
        new_expiry_date = datetime.strftime(expiry_date, '%Y-%m-%d') + timedelta(days=required_expiry_date)
        cur.execute("UPDATE MEMBERS SET membership_expiry_date = ? WHERE membership_number = ?" ,(required_expiry_date.strftime('%Y-%m-%d'),membership_number))
        print("Members Expiry date Updated Successfully.")
    else:
        print("Members not found.")    
    con.commit()
    cur.close()

def update_closing_date():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    membership_number = str(input("Enter membership number: "))
    closing_date = str(input("Enter Closing date: "))
    cur.execute("UPDATE MEMBERS SET membership_closing_date =? WHERE membership_number = ? ",(closing_date,membership_number))
    print("Updated CLosing date Successfully. ")
    con.commit()
    cur.close
def edit_member():
    con = sqlite3.connect("Library.db")
    cur =con.cursor()
    membership_number = str(input("Enter Memberhsip Number: "))
    cur.execute("SELECT FROM MEMBER WHERE membership_number = ? ",(membership_number,))
    member = cur.fetchone()
    if member:
        print("Details of Current Member: ")
        print(member)
        membership_number = str(input("Enter Mambership number: "))
        member_full_name = str(input("Enter Full name of Member: "))
        address = str(input("Enter address of member: "))
        contact_number = str(input("Enter contact Number: "))
        cur.execute("UPDATE SET address = ? , contact_number = ? , contact_number = ? , member_full_name = ? , membership_number = ?",(address,contact_number,member_full_name, membership_number))
        print("New Members detailed Succeddfully.")        
    else:
        print("Member Not Found.") 
    con.commit()
    cur.close()

def main():
    create_members_table()
    
    while True:
        print("\nMenu")
        print("a) add_member s) search member l) list all member d) delete member e) edit member u) update_closing date x) extend expiry date q) quit the program")
        choice = str(input("Enter Your Choice: "))
        if choice == "a":
            add_members()
        elif choice == "s":
            search_members()
        elif choice  == "l":
            list_all_members()
        elif choice == "e":
            edit_member()
        elif choice == "d":
            delete_member()
        elif choice == "u":
            update_closing_date()
        elif choice == "x":
            extend_expiry_date()
        elif choice == "q":
            print("Your program has ended.")
            break
        else:
            print("Invalid option!. Please choose from the menu.")
if __name__ == "__main__":
    main()
