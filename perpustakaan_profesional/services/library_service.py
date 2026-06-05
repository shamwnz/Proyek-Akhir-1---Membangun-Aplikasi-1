class LibraryService:
    def __init__(self):
        self.__items = []

    # Tambah item
    def add_item(self, item):
        self.__items.append(item)
        print("Item berhasil ditambahkan!")

    # Hapus item
    def remove_item(self, item_id):
        for item in self.__items:
            if item.get_item_id() == item_id:
                self.__items.remove(item)
                print("Item berhasil dihapus!")
                return

        print("Item tidak ditemukan!")

    # Update judul
    def update_item_title(self, item_id, new_title):
        for item in self.__items:
            if item.get_item_id() == item_id:
                item.set_title(new_title)
                print("Judul berhasil diupdate!")
                return

        print("Item tidak ditemukan!")

    # Tampilkan semua item
    def show_all_items(self):
        if len(self.__items) == 0:
            print("Data kosong!")
        else:
            for item in self.__items:
                item.display_info()

    def get_items(self):
        return self.__items