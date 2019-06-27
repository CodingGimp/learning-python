import random 

class Thief:
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for k, v in kwargs.items():
            setattr(self, k, v)


    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10
        

Gimp = Thief('Omair', scars=None, favorite_weapon='dagger')       
print(Gimp.name)
print(Gimp.sneaky)
print(Gimp.favorite_weapon)
