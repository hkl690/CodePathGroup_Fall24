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