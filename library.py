#LIBRARY.PY

books=[]
issued_books=[]

# ^ Add Books
def add_books():
    name=input("Enter the name of the book: ")
    books.append(name)
    print("Book added")

# ^ Show Books
def show_books():
    if len(books)==0:
        print("No books found")
    else:
        print("Books Available")
        for b in books:
            print(b)

#_^ Issue Books
def issue_books():
    show_books()
    name=input("Enter the book name: ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Books Issued")
    else:
        print("Book not found")

#^ Return Books
def return_books():
    name=input("Enter the name of the book: ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Book returned successfully")
    else:
        print("No such issued book")    
        


#main body
def library():
    while True:

         print("\n1.Add Books")
         print("2.Show Books")
         print("3.Issue Books")
         print("4.Return Book")
         print("5.exit")

         choice=int(input("Enter your choice: "))

         if choice == 1:
          add_books()
         elif choice == 2:
          show_books()
         elif choice == 3:
          issue_books() 
         elif choice == 4:
          return_books() 
         elif choice == 5:
          print("Thank You")
         else:
          print("Invalid Choice")
    
library()
     