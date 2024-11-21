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
          del self.lendDict[book]
          print(f"YOUR BOOK HAS BEEN RETURNED.")
       else:
          print(f"THAT BOOK WAS NOT BORROWED FROM US.")
if __name__== '__main__':
   books =LIBRARY([
      'THE SAPIENS' , 'PERIL AT END HOUSE' , 'GRANDMA TALES', 'ALGORITHMS'], "LET'S UPSKILL")
   user_name=input("THIS IS OUR LIBRARY!! KINDLY ENTER YOUR NAME:")
   



       