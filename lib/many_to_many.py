class Author:

    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    #Returns a list of related contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    #Returns a list of related books using the Contract class as an Intermediary
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    #Creates and returns a new Contract Object between the author and the specified book with the specified date and royalties
    def sign_contract(self, author, book, royalties):
        return Contract(self, author, book, royalties)
    
    #Returns the total amount of royalties that the author has earned from all of their contracts.
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
        

class Book:

    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book

        if isinstance(author, Author) and isinstance(book, Book):
            Contract.all.append(self)
        else:
            raise Exception ('Author or Book must be an instance of the Author or Book classes')

        if isinstance(date, str) and isinstance(royalties, int):
            self.date = date
            self.royalties = royalties
        else:
            raise Exception ('Date must be a string and royalties must be an integer')
    
    #Returns a list  all contracts that have the same date as the date 
    #passed into the method. 
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    

 