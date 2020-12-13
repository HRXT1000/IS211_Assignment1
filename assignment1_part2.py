Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
class Book():
    def __init__(self, title, author):
        self.author = title
        self.title = author

        def display():
            print(title, author)

        display()

book1 = Book('Of Mice and Men,', 'written by John Steinbeck')
book2 = Book('To Kill a Mockingbird,', 'written by Harper Lee')
