class Item:

    """Summary
    
    Attributes:
        price (int): Description
    """
    
    price = 10

    def get_price(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return self.price


class Box:

    """Summary
    """
    
    def __init__(self, items):
        """Summary
        
        Args:
            items (TYPE): Description
        """
        self.__items = items

    def get_price(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        price = 0
        for item in self.__items:
            price += item.get_price()
        return price


class Cart:

    """Summary
    """
    
    def __init__(self):
        """Summary
        """
        self.__items = []

    def add_item(self, item):
        """Summary
        
        Args:
            item (TYPE): Description
        """
        self.__items.append(item)

    def get_price(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        price = 0
        for item in self.__items:
            price += item.get_price()
        return price


if __name__ == '__main__':
    my_items = [Item(),
                Item(),
                Item(),
                Item(),
                Box([Item(), Item(), Item()]),
                Box([Item(), Item(), Item(), Item(), Item(), Item()]),
                Item(),
                Item(),
                Item(),
                Item()]
    cart = Cart()
    while True:
        choice = input('Add product - 1\nCalculate amount cart - 2: ')
        if choice == '1':
            number = input('Enter number 0 to 9 :')
            if number.isdigit() and 0 <= int(number) <= 10:
                cart.add_item(my_items[int(number)])
                print('Product added')
        if choice == '2':
            print(cart.get_price())
        if choice == '3':
            break
