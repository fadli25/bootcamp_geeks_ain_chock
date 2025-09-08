import psycopg2

connection = psycopg2.connect(
    dbname="restaurant",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
connection.autocommit = True

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        with connection.cursor() as cur:
            cur.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (self.name, self.price))

    def delete(self):
        with connection.cursor() as cur:
            cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))

    def update(self, new_name, new_price):
        with connection.cursor() as cur:
            cur.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                        (new_name, new_price, self.name))
            self.name = new_name
            self.price = new_price

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
            item = cur.fetchone()
            if item:
                return MenuItem(item[1], item[2])
            return None

    @classmethod
    def all_items(cls):
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM Menu_Items")
            items = cur.fetchall()
            return [MenuItem(item[1], item[2]) for item in items]

def show_user_menu():
    while True:
        choice = input("View(V) Add(A) Delete(D) Update(U) Show(S) Exit(E): ").upper()
        if choice == "V":
            name = input("Enter item name: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name} - {item.price}")
            else:
                print("Item not found")
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            show_restaurant_menu()
            break

def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name, price)
    item.save()
    print("Item added successfully")

def remove_item_from_menu():
    name = input("Enter item name to delete: ")
    item = MenuItem(name, 0)
    if MenuManager.get_by_name(name):
        item.delete()
        print("Item deleted successfully")
    else:
        print("Error: Item not found")

def update_item_from_menu():
    name = input("Enter current item name: ")
    price = int(input("Enter current item price: "))
    new_name = input("Enter new item name: ")
    new_price = int(input("Enter new item price: "))
    item = MenuItem(name, price)
    if MenuManager.get_by_name(name):
        item.update(new_name, new_price)
        print("Item updated successfully")
    else:
        print("Error: Item not found")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("Restaurant Menu:")
    for item in items:
        print(f"{item.name} - {item.price}")

if __name__ == "__main__":
    show_user_menu()
