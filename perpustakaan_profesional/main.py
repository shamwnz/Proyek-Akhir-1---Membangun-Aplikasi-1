from models.book import Book
from models.magazine import Magazine
from services.library_service import LibraryService
from services.report_service import ReportService
from utils.helper import garis


def main():
    library = LibraryService()

    while True:
        garis()
        print(" SISTEM PERPUSTAKAAN PROFESIONAL ")
        garis()

        print("""
1. Tambah Buku
2. Tambah Majalah
3. Tampilkan Semua Koleksi
4. Update Judul Item
5. Hapus Item
6. Laporan Total Koleksi
7. Keluar
""")

        pilihan = input("Pilih menu: ")

        # Tambah Buku
        if pilihan == "1":
            item_id = input("ID Buku      : ")
            title = input("Judul Buku   : ")
            author = input("Penulis      : ")
            stock = int(input("Stok Buku    : "))

            book = Book(item_id, title, author, stock)
            library.add_item(book)

        # Tambah Majalah
        elif pilihan == "2":
            item_id = input("ID Majalah   : ")
            title = input("Judul        : ")
            publisher = input("Penerbit     : ")
            edition = input("Edisi        : ")

            magazine = Magazine(item_id, title, publisher, edition)
            library.add_item(magazine)

        # Tampilkan Semua
        elif pilihan == "3":
            library.show_all_items()

        # Update Judul
        elif pilihan == "4":
            item_id = input("Masukkan ID item: ")
            new_title = input("Judul baru: ")

            library.update_item_title(item_id, new_title)

        # Hapus Item
        elif pilihan == "5":
            item_id = input("Masukkan ID item yang ingin dihapus: ")
            library.remove_item(item_id)

        # Laporan
        elif pilihan == "6":
            ReportService.total_items(library.get_items())

        # Keluar
        elif pilihan == "7":
            print("Program selesai...")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()