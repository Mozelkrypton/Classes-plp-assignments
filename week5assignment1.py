# Parent class
class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.__battery = battery   # encapsulation

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged to {self.__battery}%")

    def use(self, amount):
        if amount > self.__battery:
            print(f"{self.model} has low battery! Please charge.")
        else:
            self.__battery -= amount
            print(f"{self.model} used {amount}%, battery left: {self.__battery}%")

    def get_battery(self):
        return self.__battery


#Inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery=100, gpu="Adreno"):
        super().__init__(brand, model, battery)
        self.gpu = gpu

    # Polymorphism
    def use(self, amount):
        # Gaming consumes battery faster
        drain = amount * 2
        print(f"{self.model} running heavy games with {self.gpu} GPU...")
        super().use(drain)


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S10e")
gaming_phone = GamingPhone("Asus", "ROG Phone 6", gpu="Snapdragon Elite")

# Use methods
phone1.use(20)
phone1.charge(15)

gaming_phone.use(20)   # uses more battery because of overridden method
print("Battery left:", gaming_phone.get_battery())
