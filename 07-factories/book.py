class Book(object):
    def __init__(self, title, authors, isbn, publisher, copyright, categories) -> None:
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.publisher = publisher
        self.copyright = copyright
        self.categories = categories

    def __repr__(self) -> str:
        return repr(
            (
                self.title,
                self.authors,
                self.isbn,
                self.publisher,
                self.copyright,
                self.categories,
            )
        )
