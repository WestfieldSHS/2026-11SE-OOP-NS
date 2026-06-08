from datetime import date


class Book:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_date}"
    
    def get_book_age(self):
        current_year = date.today().year
        publication_year = int(self.publication_date.split("-")[0])
        return current_year - publication_year
    
