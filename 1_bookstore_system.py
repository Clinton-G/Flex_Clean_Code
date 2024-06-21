class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def check_availability(self):
        if self.stock > 0:
            return f"{self.title} is in stock."
        else:
            return f"{self.title} is out of stock."
    
    def sell_book(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            return f"Sold {quantity} copies of {self.title}."
        else:
            return f"Only {self.stock} copies of {self.title} are available."
    
    def update_stock(self, quantity):
        self.stock += quantity
        return f"Stock for {self.title} is now {self.stock}"

    def update_title(self, new_title):
        self.title = new_title
        return f"Changed title to {self.title}"

    def update_author(self, new_author):
        self.author = new_author
        return f"Changd author to {self.author}"

def change_price(book, new_price):
    book.price = new_price
    return f"Price of {book.title} has been raised to ${new_price}."


if __name__ == "__main__":
    book1 = Book("Python Programming", "Mr. Python", 19.99, 10)
    book2 = Book("Cook Book", "Gordon Ramsay", 49.99, 5)

    print(book1)
    print(book1.check_availability())
    print()

    print(book1.sell_book(2))
    print(book1.check_availability())
    print()

    print(change_price(book2, 45.99))
    print()

    print(book1.update_stock(4))
    print()

    print(book2.update_title("Advanced Python Skills"))

    print(book1.update_author("The Great Mr. Python"))
