import sqlite3
from datetime import datetime,timedelta

def create_circulation_table():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS CIRCULATION (serial_number INTEGER PRIMARY KEY, membership_number TEXT, accession_number TEXT, issue_date TEXT, return_date TEXT)")
    con.commit()
    cur.close()

def issue_date():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    membership_number = str(input("Enter membership number: "))
    accession_number = str(input("Enter accession Number: "))
    issue_date = datetime.now().strftime("%Y-%m-%d")
    return_date = None
    cur.execute("INSERT INTO CIRCULATION (membership_number, accession_number, issue_date, return_date) VALUES (?,?,?,?)", (membership_number, accession_number, issue_date, return_date))
    con.commit()
    cur.close()
    print("Book Issued Successfully")




def return_date():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    membership_number = str(input("Enter Membership Number: "))
    accession_number = str(input("Enter Accession Number: "))
    return_date = datetime.now().strftime("%Y-%m-%d")
    cur.execute("UPDATE CIRCULATION SET return_date = ? WHERE membership_number = ? AND accession_number = ?  AND return_date IS NULL",(return_date,membership_number,accession_number))
    con.commit()
    cur.close()
    print("Book Returned.")

def search_circulation():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    membership_number = str(input("Enter Membership number: "))
    accession_number = str(input("Enter Accession number: "))
    cur.execute("SELECT membership_number , accession_number , issue_date , return_date FROM CIRCULATION WHERE membership_number = ? AND accession_number = ?  ", (membership_number,accession_number))
    cir = cur.fetchone()
    if cir :
        print(cir)
    else:
        print("Record not found.")
def list_all__circulation():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT membership_number , accession_number , issue_date , return_date FROM CIRCULATION ")
    circulation_book = cur.fetchall()
    if circulation_book: 
        for row in circulation_book:
            print(row)
    
    else:
        print("Book not found.")

def main():
    create_circulation_table()
    while True:
        print("\nDisply Menu")
        print("i) Issue date r) return date s) search circulation l) list all circulation q) quit the progarm ")
        choice = str(input("Enter your choice: "))
        if choice == "i":
            issue_date()
        elif choice == "r":
            return_date()
        elif choice == "s":
            search_circulation()
        elif choice == "l":
            list_all__circulation()
        elif choice == "q":
            print("Your program has ended.")
            break
        else:
            print("Invalid Option. Please choice valid option.")
        
if __name__ == "__main__":
    main()