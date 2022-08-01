#import models.py
# main meun (Add, Search, Exit)
# functions to CRUD the database
# data cleaning function
# loop to run our program


#github repo: https://github.com/PrettyActiveSloth/book-database-sqlalchemy


from posixpath import split
from models import (Base, session, 
                    Book, engine)
import datetime
import csv
import os


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(" ")
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(",")[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)



def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title == row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = round(float(row[3]))
                new_book = Book(title=title, author=author, published_date = date, price = price)
                session.add(new_book)
        session.commit()
            



def menu():
    while True:
        print('''
        \nPROGRAMMMING BOOKS
        \r1) ADD BOOK
        \r2) VIEW ALL BOOKS
        \r3) SEARCH FOR BOOKS
        \r4) BOOK ANALYSIS
        \r5) EXIT
        ''')
        choice = input ("What would you like to do? ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print('''
            
            \nPlease try again. Press enter & then enter a number from 1 to 5. ''')



def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #add book
            pass
        elif choice == '2':
            #view books
            pass
        elif choice == '3':
            #view books
            pass
        elif choice == '4':
            #view books
            pass
        else:
            print('Goodbye!')
            app_running = False




if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    os.system('clear')
    add_csv()
    for book in session.query(Book):
        print(book)


