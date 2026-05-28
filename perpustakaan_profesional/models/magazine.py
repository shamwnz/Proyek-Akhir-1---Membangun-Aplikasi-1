from models.item import Item


class Magazine(Item):
    def __init__(self, item_id, title, publisher, edition):
        super().__init__(item_id, title)
        self.__publisher = publisher
        self.__edition = edition

    def display_info(self):
        print(f"""
=== DATA MAJALAH ===
ID Majalah : {self.get_item_id()}
Judul      : {self.get_title()}
Penerbit   : {self.__publisher}
Edisi      : {self.__edition}
Update     : {self.get_timestamp()}
""")