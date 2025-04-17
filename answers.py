# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_info(self):
        return f"Brand: {self.brand},Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours"
    
    # Adding an inheritance layer
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_life, strap_material):
        super().__init__(brand, model, storage, battery_life)
        self.strap_material = strap_material

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Strap Material: {self.strap_material}"
    
# Testing the Smartphone and Smartwatch classes

# Create an instance of Smartphone
phone = Smartphone(brand="Apple", model="iPhone 14", storage=128, battery_life=20)
print(phone.display_info())  # Expected output: Brand: Apple, Model: iPhone 14, Storage: 128GB, Battery Life: 20 hours

# Create an instance of Smartwatch
watch = Smartwatch(brand="Samsung", model="Galaxy Watch 5", storage=16, battery_life=48, strap_material="Leather")
print(watch.display_info())  
# Expected output: Brand: Samsung, Model: Galaxy Watch 5, Storage: 16GB, Battery Life: 48 hours, Strap Material: Leather

# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles
# with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move()
#  prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
 # Polymorphism Challenge: Vehicles with the same action but different implementations

class Car:
    def move(self):
        print("🚗 Driving on the road")

class Plane:
    def move(self):
        print("✈️ Flying in the sky")

class Boat:
    def move(self):
        print("🚤 Sailing on water")

class Train:
    def move(self):
        print("🚆 Running on tracks")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Train()]

for vehicle in vehicles:
    vehicle.move()
