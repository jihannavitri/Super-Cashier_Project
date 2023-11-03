from transaction import Transaction

# ID transaksi tr127 sebagai instance
tr127 = Transaction()

# menambahkan barang ke daftar belanja
tr127.add_item('Pasts Gigi', 3, 15000)
tr127.add_item('Sabun', 1, 25000)
tr127.add_item('Buku Tulis', 5, 6000)

# mengubah nama item Pasta Gigi
tr127.update_item_name('Pasts Gigi', 'Pasta Gigi')

# Mengubah jumlah item sabun menjadi 2
tr127.update_item_qty('Sabun', 2)

# mengubah harga item Sabun dan Buku Tulis
tr127.update_item_price('Sabun', 32000)
tr127.update_item_price('Buku Tulis', 7000)

# menghapus item pasta gigi
tr127.delete_item('Pasta Gigi')

# menambahkan item baru
tr127.add_item('Lampu', 3, 48000)

# cek daftar belanja dan menghitung total harga
tr127.check_order()
tr127.total_price()
