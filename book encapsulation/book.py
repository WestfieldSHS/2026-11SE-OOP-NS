from datetime import date


class Book:
    def __init__(self, title, author, publication_date):
        self._title = title
        self._author = author
        self._publication_date = publication_date

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_publication_date(self):
        return self._publication_date
    
# Example
if __name__ == "__main__":
    book = Book("Sunrise on the Reaping", "Suzanne Collins", date(2025, 4, 18))
    print("Title:", book.get_title())
    print("Author:", book.get_author())
    print("Publication Date:", book.get_publication_date())


       
