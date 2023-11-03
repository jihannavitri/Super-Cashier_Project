# ID transaksi tr127 sebagai instance
tr127 = Transaction()

# menambahkan barang ke daftar belanja
transaction1.add_item('Pasts Gigi', 3, 15000)
transaction1.add_item('Sabun', 1, 25000)
transaction1.add_item('Buku Tulis', 5, 6000)

# mengubah nama item Pasta Gigi
transaction1.update_item_name('Pasts Gigi', 'Pasta Gigi')

# Mengubah jumlah item sabun menjadi 2
transaction1.update_item_qty('Sabun', 2)

# mengubah harga item Sabun dan Buku Tulis
transaction1.update_item_price('Sabun', 32000)
transaction1.update_item_price('Buku Tulis', 7000)

# menghapus item pasta gigi
transaction1.delete_item('Pasta Gigi')

# menambahkan item baru
transaction1.add_item('Lampu', 3, 48000)

# cek daftar belanja dan menghitung total harga
transaction1.check_order()
transaction1.total_price()