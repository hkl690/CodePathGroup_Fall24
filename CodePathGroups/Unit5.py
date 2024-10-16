class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) >= 20:
            print("Invalid catchphrase")            
        
        if len(new_catchphrase) < 20:
            for char in new_catchphrase:
                if not(char.isalpha() or char.isspace()):
                    print("Invalid catchphrase")
                    return
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")

    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_items:
            self.furniture.append(item_name)
        else:
            print("Invalid item")

    def print_inventory(self):
        if not self.furniture:
            print("Inventory empty")
            return
        else:
            inventory={}
            for item in self.furniture:
                if item in inventory:
                    inventory[item] += 1
                else:
                    inventory[item] = 1
            temp = ""
            for item in inventory:
                temp += item + ": "+ str(inventory[item]) +", "
            print(temp[:-2])




apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 


bones = Villager("Bones", "Dog", "yip yap")
bones.catchphrase = "ruff it up"
print(bones.greet_player("Jina"))

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)





alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()


# Cheatsheet examples:
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
    def call_dog(self):
        print(f"Here {self.name}!")

    def command_trick(self, trick):
        print(f"{self.name}, {trick}!")


my_dog = Dog('Fido', 'Cocker Spaniel', 'Ada Lovelace')
print(my_dog.name) # Prints Fido

my_dog.call_dog() # Prints 'Here Fido!'

my_dog.command_trick("roll over") # Prints 'Fido, roll over!'

class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def pair_nodes(head):
    # Check if the list is empty
    if not head:
        return None
    
    # Pass 1: Get the length of the list
    current = head
    length = 0
    while current:
        length += 1
        current = current.next

    # If the length is odd, return None
    if length % 2 != 0:
        return None

    # Pass 2: If the length is even, create tuples of pairs
    pairs = []
    current = head
    while current:
        # Since we know the list length is even, current.next should always be valid here
        pairs.append((current.value, current.next.value))
        current = current.next.next  # Move to the next pair

    return pairs

head = Node(1, Node(2, Node(3, Node(4))))
print(pair_nodes(head))  # Output should be [(1, 2), (3, 4)]
head = Node(1, Node(2, Node(3)))
print(pair_nodes(head))  # Output should be None
head = None
print(pair_nodes(head))  # Output should be None
