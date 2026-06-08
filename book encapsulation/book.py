from datetime import date


class Book:
    def __init__(self, title, author, publication_date, num_pages):
        if not num_pages > 0:
            raise ValueError("Number of pages must be greater than zero.")
        
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._num_pages = num_pages

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_publication_date(self):
        return self._publication_date
    
    def get_num_pages(self):
        return self._num_pages
    

# Example
if __name__ == "__main__":
    book = Book("Sunrise on the Reaping", "Suzanne Collins", date(2025, 4, 18), 400)
    print("Title:", book.get_title())
    print("Author:", book.get_author())
    print("Publication Date:", book.get_publication_date())
    print("Number of Pages:", book.get_num_pages())

       
