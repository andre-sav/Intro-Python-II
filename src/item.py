class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories

class Egg(Food):
    def __init__(self):
        super().__init__("Egg", "It is an egg", 100)