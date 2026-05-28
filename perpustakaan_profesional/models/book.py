from models.item import Item


class Book(Item):
    def __init__(self, item_id, title, author, stock):
        super().__init__(item_id, title)
        self.__author = author
        self.__stock = stock

    # Getter
    def get_author(self):
        return self.__author

    def get_stock(self):
        return self.__stock

    # Setter
    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
            self.update_timestamp()
        else:
            print("Stock tidak boleh negatif!")

    # Polymorphism
    def display_info(self):
        print(f"""
=== DATA BUKU ===
ID Buku    : {self.get_item_id()}
Judul      : {self.get_title()}
Penulis    : {self.__author}
Stok       : {self.__stock}
Update     : {self.get_timestamp()}
""")