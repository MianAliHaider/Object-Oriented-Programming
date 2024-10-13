import sqlite3
from datetime import datetime, timedelta
def category_wise_active_members():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cur.execute("SELECT  category, COUNT(*) FROM MEMBERS WHERE (membership_expiry_date > ? ) AND (membership_closing_date > ?) GROUP BY category",(date,date))
    active = cur.fetchall()
    if active:
        print("Active members are: ")
        for category, row in active:
            print(f"Count is {row} of Category {category} ")
    else:
        print("Not Active Members are Found.")
    con.commit()    
    cur.close()
def count_of_each_title_issued_to_a_member():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT accession_number,title, COUNT(*) FROM CIRCULATION JOIN BOOKS ON CIRCULATION.accession_number = BOOKS.accno GROUP BY accession_number")
    issue = cur.fetchall()
    if issue:
        for title,row,accno in issue:
            print(f"Count of {row} is {accno} to a member with accession Number {title}")
    else:
        print("book is not issue.")
    con.commit()
    cur.close()
def count_and_total_price_of_each_title_issued_to_members():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT title,accession_number, COUNT(*), SUM(price) FROM CIRCULATION JOIN BOOKS ON CIRCULATION.accession_number = BOOKS.accno GROUP BY accession_number")
    title = cur.fetchall()
    if title:
        for title,accno,row, price in title:
            print(f"Count is {row} with title {title} to a accession number {accno} with price {price}")
    else:
        print("Books is not founded")
    con.commit()
    cur.close()
    
def books_have_only_one_copy_in_the_library():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT title, COUNT(*) FROM BOOKS GROUP BY title HAVING COUNT(*) = 1 ")
    only_1_copies = cur.fetchall()
    if only_1_copies:
        for title,row in only_1_copies:
            print(f"Book of title {title} have {row} copies in the library")
    else:
        print("Books have greater than one copies")
    con.commit()
    cur.close()
def books_having_less_than_5_copies_in_the_library():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT title, COUNT(*) FROM BOOKS GROUP BY title HAVING COUNT(*) < 5 ")
    less_than_5_copies = cur.fetchall()
    if less_than_5_copies:
        for title,row in less_than_5_copies:
            print(f"Book of title {title} have {row} copies in the library")
    else:
        print("Books have greater than five copies")
    con.commit()
    cur.close()
def members_list_with_their_unpiad_fine():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT member_full_name FROM MEMBERS JOIN CIRCULATION ON MEMBERS.membership_number = CIRCULATION.membership_number WHERE circulation.return_date IS NULL AND fine_paid > 0 GROUP BY member_full_name")
    unpaid_fine = cur.fetchall()
    if unpaid_fine:
        for member, row in unpaid_fine:
            print(f"Member: {member}, Total Unpaid Fine: {row}")
    else:
        print("No members with unpaid fine.")
def main():
    while True:
        print("\nDisplay menu") 
        print(" 1) Category wise active members list")
        print(" 2) Count of each title issued to members")
        print(" 3) Count and total price of each title issued to members")
        print(" 4) Books having only one copy in the library")
        print(" 5) Books having less than five copies in the library")
        print(" 6) Members list with their total unpaid fine")
        print(" 7) Quit the progarm")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            category_wise_active_members()
        elif choice == 2:
            count_of_each_title_issued_to_a_member()
        elif choice == 3:
            count_and_total_price_of_each_title_issued_to_members()
        elif choice == 4:
            books_have_only_one_copy_in_the_library()
        elif choice == 5:
            books_having_less_than_5_copies_in_the_library()
        elif choice == 6:
            members_list_with_their_unpiad_fine()
        elif choice == 7:
            print("Quit the program.")
            break
        else:
            print("Invalid Option!. Please choose from the above display menu.")



if __name__ == "__main__":
    main()
