class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        return list({c.book for c in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        return list({c.author for c in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # validations
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that match given date, sorted by date."""
        # date format is dd/mm/yyyy — string comparison works
        same_date_contracts = [c for c in cls.all if c.date == date]

        # Sort by date (string format ensures correct sorting)
        return sorted(same_date_contracts, key=lambda c: c.date)
