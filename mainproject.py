



                       # project=>... Student library......

# Implement a student library system using oops where students can barrow a book from 
# the list of books.
# create a separate library and student class.your programe must be mean driven.
# you are free to choose methods and attribute of your choice to implement this functionality.

class Library:
    def __init__(self,listofBooks):
        self.books=listofBooks
    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" * "+ book)
    def boorowBook(self,bookName):
        if bookName in self.books:
         print(f"You have been issued {bookName}.please keep it safe and return it within 30 days") 
         self.books.remove(bookName)
         return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. please wait untill the book is available")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book hope you enjoyed reading it have a great day ahead")                

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to be borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to be return: ")
        return self.book      

if __name__=="__main__":
    centraLibrary= Library(["Algorithms","Django","clrs","Python Notes"])
    student= Student()
    centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg='''====Welcome to Central Library=====
        Please choose an option:
        1. List all the books
        2. Request all the books
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a= int(input("Enter a choice: "))
        if a== 1:
            centraLibrary.displayAvailableBooks()
        elif a==2:
            centraLibrary.boorowBook(student.requestBook())
        elif a==3:
            centraLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central  library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")                    

        

