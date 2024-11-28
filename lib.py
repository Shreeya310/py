class LIBRARY:
    def __init__(self,list_of_books,name):
     self.bookslist=list_of_books
     self.name=name
     self.lendDict={}
    def displayBooks(self):
       print(f"THE BOOKS WE HAVE ARE AS FOLLOWS:{self.name}")
       for books in self.bookList:
          print(books)
    def lendBooks(self,user,books):
       if books not in self.bookList:
          print(f"SORRY,WE DON'T HAVE THIS BOOK.")   
       elif books in self.bookList:
          print(f"THE BOOK IS READ BY{self.lendDict[books]}")
       else:
          self.lendDict[books]=user
          print("DATABASE HAS BEEN UPDATED.YOU CAN TAKE THE BOOK.")  
    def addBooks(self,book ):
       self.booksList.append(book)
       print(f"{book} your book has been added to your book list.")
    def returnBooks(self,book):
       if book in self.lendDict:
          del self.lendDict.pop[book]
      
if __name__ ==  '__main__':
   books =LIBRARY([
      'THE SAPIENS' , 'PERIL AT END HOUSE' , 'GRANDMA TALES', 'ALGORITHMS'], "LET'S UPSKILL")
   while(True):
    print(f"WELCOME{books.name}LIBRARY!!! ENTER YOUR CHOICE TO CONTINUE.")
    print("1-DISPLAY BOOKS")
    print("2-BORROW A BOOK")
    print("3-ADD A BOOK")
    print("4-RETURN A BOOK")
    print("5-BESTSELLERS")
    user_choice=input()
    if user_choice not in ['1','2','3','4','5']:
       print("PLEASE ENTER A VALID OPTION")
       continue
    else:
       user_choice=int(user_choice)
    if user_choice ==1:
     books.displayBooks()
     


   



       