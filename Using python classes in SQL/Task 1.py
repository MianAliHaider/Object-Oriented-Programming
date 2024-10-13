import sqlite3 

def create_books_table():

    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BOOKS (accno TEXT, title TEXT, subtitle TEXT, author TEXT, coauthor TEXT, pages INTEGER, price REAL, category TEXT )")
    con.commit()
    cur.close()

def add_books():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    account_number = str(input("Enter Accession Number of book: "))
    title = str(input("Enter Title of Book: "))
    subtitle = str(input("Enter subtitle of book: "))
    author = str(input("Enter author of Book: "))
    coauthor = str(input("Enter coauthor of Book: "))
    pages = int(input("Enter pages of Book: "))
    price = float(input("Enter price of Book: "))
    category = str(input("Enter the category(Is it issuable or not) "))

    cur.execute("INSERT INTO BOOKS (accno, title, subtitle, author,coauthor,pages,price,category) VALUES (?,?,?,?,?,?,?,?)", (account_number, title, subtitle, author,coauthor,pages,price,category))
    print("Book Added Successfully")
    con.commit()
    cur.close()
    con.close()

def search_books():
    accno = str(input("ENter Accession number to search: "))
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute( "SELECT accno,title, subtitle, author,coauthor,pages,price,category FROM BOOKS WHERE accno = ?" , (accno,))
    BOOKS = cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    if BOOKS:
        print("Book found")
        print(BOOKS)
    else:
        print("BOOK not found") 
    
def list_all_books():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT accno, title, subtitle, author,coauthor,pages,price,category FROM BOOKS ")
    BOOKS = cur.fetchall()
    if BOOKS:
        print("List of all books ")
        for row in BOOKS:
            print(row)
    else:
        print("Books not founded")

    con.commit()
    con.close()

def delete_book():
    accno = str(input("Enter Accession Number: "))
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("DELETE FROM BOOKS  WHERE accno =?", (accno,))
    print("Book Deletd successfully")
    con.commit()
    cur.close()

def edit_book():
    accno = input("Enter Accession Number: ")
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT accno, title, subtitle, author,coauthor,pages,price,category FROM BOOKS WHERE accno=?", (accno,))
    BOOKS = cur.fetchone()
    if BOOKS:
        print("Your New Book Detailed ")
        print(BOOKS)

        title = input("Enter New title: ")
        subtitle = input("Enter New subtitle: ")
        author = input("Enter New author: ")
        coauthor = input("Enter New coauthor: ")
        pages = input("Enter New pages: ")
        price = input("Enter New price: ")
        category = input("Enter New category (ISUABLE OR NOT): ")
        cur.execute("UPDATE BOOKS Set title = ? , subtitle = ? , author = ? , coauthor = ? , pages = ? , price = ?, category = ? WHERE accno = ? ",(title, subtitle, author,coauthor,pages,price,category,accno))
        con.commit()
        print("Book Edited Successfully")
    else:
        print("Book Not Available for editing")

def main():
    create_books_table()
        
    while True :
        print("\nMenu:")
        print("a) Add, s) Search, d) Delete, l) List All, e) Edit, q) Quit")

        choice  = str(input("Enter your choice: "))
        if choice == "a":
            add_books()
        elif choice == "s":
            search_books()
        elif choice == "l":
            list_all_books()
        elif choice == "d":
            delete_book()
        elif choice == "e":
            edit_book()
        elif choice == "q":
            print("Your program has ended")   
            break; 
        else:
            print("Invalid Option: Please try again")
if __name__ == "__main__":
    main()