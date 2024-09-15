class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.book_table = False
        self.customer_order = {}

    def add_item_to_menu(self, item):
        self.menu_items.append(item)
        print("Menu added!")
    
    def make_table_reservation(self):
        if(self.book_table == True) : 
            print("Table Already Booked!")
        else:
            self.book_table = True
            print("Table Booked!")

    def take_customer_order(self, customer_name, order):
        self.customer_order[customer_name] =  order
        print("Ordered Added")

    def print_menu(self):
        print("THE MENU OF RESTAURANT IS: ")
        for i, item in enumerate(self.menu_items, 1):
            print(f"{i}. {item}")

    def print_booked_table(self):
        print("The booking of tables is: ")
        print(self.book_table)
    
    def print_customer_order(self):
        print("The data of customer order is as follows: ")
        print(self.customer_order)


def main():
    # Create a Restaurant object
    my_restaurant = Restaurant()

    # Adding items to the menu
    my_restaurant.add_item_to_menu("Pizza")
    my_restaurant.add_item_to_menu("Pasta")
    my_restaurant.add_item_to_menu("Burger")

    # Printing the menu
    my_restaurant.print_menu()

    # Attempt to book a table
    my_restaurant.make_table_reservation()

    # Print the table booking status
    my_restaurant.print_booked_table()

    # Taking customer orders
    my_restaurant.take_customer_order("Laiba", "Pizza")
    my_restaurant.take_customer_order("Bilal", "Pasta")

    # Print the customer orders
    my_restaurant.print_customer_order()

main()
