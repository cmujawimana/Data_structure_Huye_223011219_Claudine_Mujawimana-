from collections import deque

class ClothingStore:
    def __init__(self):
        self.inventory = [] 
        self.undo_stack = []  
        self.restock_queue = deque()  

    def add_item(self, item):
        self.inventory.append(item)
        self.undo_stack.append(("add", item))
        print(f"Added {item} to inventory.")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.undo_stack.append(("remove", item))
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not found in inventory.")

    def undo_last_action(self):
        if self.undo_stack:
            action, item = self.undo_stack.pop()
            if action == "add":
                self.inventory.remove(item)
                print(f"Undid addition: Removed {item} from inventory.")
            elif action == "remove":
                self.inventory.append(item)
                print(f"Undid removal: Added {item} back to inventory.")
        else:
            print("No actions to undo.")

    def request_restock(self, item):
        self.restock_queue.append(item)
        print(f"Added {item} to restock queue.")

    def process_restock_request(self):
        if self.restock_queue:
            item = self.restock_queue.popleft()
            print(f"Processing restock request for {item}.")
            self.add_item(item)
        else:
            print("No restock requests to process.")

    def display_inventory(self):
        print("Current Inventory:")
        for item in self.inventory:
            print(f"- {item}")

    def display_restock_queue(self):
        print("Restock Queue:")
        for item in self.restock_queue:
            print(f"- {item}")

# Example usage
store = ClothingStore()

store.add_item("T-shirt")
store.add_item("Jeans")
store.add_item("Sweater")
store.add_item("dress")
store.add_item("Jumper")
store.add_item("Skirt")


store.display_inventory()

store.remove_item("Jeans")
store.display_inventory()

store.undo_last_action()
store.display_inventory()

store.request_restock("Socks")
store.request_restock("Jacket")
store.display_restock_queue()

store.process_restock_request()
store.display_inventory()
store.display_restock_queue()