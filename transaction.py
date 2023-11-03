import pandas as pd

class Transaction():
    """
    A class representing a transacrion of a supermarket.

    This class stores information about customer's groceries.
    including the item name, quantity, and price.
    
    Attributes:
        item_name : item name
        item_qty : quantity of the item
        item_price : price per item
        total : quantity * price
        order : summary list of the groceries
        
    Methods:
        add_item : adding item to order list
        check_order : print the order list
        update_item_name : update an item name
        update_item_qty : update the quantity of an item
        update_item_price : update the price of an item
        delete_item : delete an item including its quantity and price
                      from the list
        reset_transaction : delete the order list
        total_price : calculate the total price of the orders
        
    """
    
    def __init__(self):
        """
        Initialize a new transaction.
        """
        
        self.item_name = []
        self.item_qty = []
        self.item_price = []
        self.total = []
        self.order = {'Nama Barang' : self.item_name,
                      'Jumlah' : self.item_qty,
                      'Harga' : self.item_price,
                      'Total Harga' : self.total}
        
    def add_item(self, item_name, item_qty, item_price):
        """
        Adding item to order list
        """
        if not (isinstance(item_qty, int) and isinstance(item_price, int)):
            raise ValueError('Masukkan jumlah dan/atau harga yang benar.')
        else: # menambahkan barang ke daftar belanja
            self.item_name.append(item_name)
            self.item_qty.append(item_qty)
            self.item_price.append(item_price)
            self.total.append(item_qty * item_price)
    
    def check_order(self):
        """
        Print the order list
        """
        data_order = pd.DataFrame(self.order)
        print('Barang yang ingin dibeli adalah :')
        print(data_order)
        
    def update_item_name(self, item_name, new_item_name):
        """
        Update an item name
        """
        for item in self.item_name:
            if item == item_name:
                index = self.item_name.index(item_name)
                self.item_name[index] = new_item_name
                
    def update_item_qty(self, item_name, new_item_qty):
        """
        Update the quantity of an item
        """
        if not (isinstance(new_item_qty, int)):
            raise ValueError('Masukkan jumlah yang benar.')
        else:
            for item in self.item_name:
                if item == item_name:
                    index = self.item_name.index(item_name)
                    self.item_qty[index] = new_item_qty
                    self.total[index] = new_item_qty * self.item_price[index]
                
    
    def update_item_price(self, item_name, new_item_price):
        """
        Update the price of an item
        """
        if not (isinstance(new_item_price, int)):
            raise ValueError('Masukkan harga yang benar.')
        else:
            for item in self.item_name:
                if item == item_name:
                    index = self.item_name.index(item_name)
                    self.item_price[index] = new_item_price
                    self.total[index] = new_item_price * self.item_qty[index]
                
    
    def delete_item(self, item_name):
        """
        Delete an item including its quantity and price
        from the list
        """
        for item in self.item_name:
            if item == item_name:
                index = self.item_name.index(item_name)
                self.item_name[index] = '---'
                self.item_qty[index] = 0
                self.item_price[index] = 0
                self.total[index] = 0
                

    def reset_transaction(self):
        """
        Delete the order list
        """
        self.order.clear()
        print('Transaksi Dibatalkan')
        
        
    def total_price(self):
        """
        Calculate the total price of the orders
        """
        total = sum(self.total)
        
        # Jika total belanja memenuhi syarat discount
        if total > 500000:
            total = total - 0.10*total
            print('Selamat anda mendapatkan potongan harga 10%!')
        elif total > 300000:
            total = total- 0.08*total
            print('Selamat anda mendapatkan potongan harga 8%!')
        elif total > 200000:
            total = total - 0.05*total
            print('Selamat anda mendapatkan potongan harga 5%!')
        
        print(f'Total belanja anda adalah {total}')
        