import random 

class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for k, v in kwargs.items():
            setattr(self, k, v)

class Thief(Character):
    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10
        

Gimp = Thief('Omair', sneaky=False, scars=None, favorite_weapon='dagger')       
print(Gimp.name)
print(Gimp.sneaky)
print(Gimp.favorite_weapon)

'''
Now, let's try an experiment. I have a class:

class Animal:
    def __init__(self, **kwargs):
        self.species = kwargs.get("species")
        self.age = kwargs.get("age")
        self.sound = kwargs.get("sound")
I'm using **kwargs here to pack any and all keyword arguments into a dictionary. And then I'll make a wolf using that class.

>>> wolf = Animal(species="Canus Lupus", age=5, sound="howl", color="gray")
>>> wolf.species
"Canus Lupus"
Great. No errors, Python's happy, I have an instance of my Animal class. In the __init__, I set three attributes: species, age, and sound. I didn't set color, though. Is it available?

>>> wolf.color
AttributeError...
No, it's not! But there weren't any errors when I created the instance. Why isn't the attribute available?

Well, because I didn't create it. Remember, Python is very explicit. If I don't do something explicitly, Python doesn't do it at all. Since I didn't assign a color attribute to self, my instance doesn't have a color attribute.

This is where setattr comes in. setattr lets me set attributes that I don't know about beforehand. I can, of course, go back and explicitly define a color attribute but what if the next user comes along and she wants a height or weight attribute? A year from now, Animal.__init__ might be hundreds of lines long with attribute declarations! And some of those attributes will only apply to a few animals!

But...if I'm clever and use setattr, I can just happily accept any and all attributes that someone gives for a particular Animal instance without having to continually update __init__.

class Animal:
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
So, since I have a handy-dandy kwargs dict due to using **kwargs in the method parameters, I can loop through it's items method and pull out the two values from each iteration into attribute and value variables.

The setattr function takes three arguments: the object to work on, the attribute name to define, and the value to give that attribute. Now, no matter what attribute values I give to my object (assuming they're valid attribute names), my class will happily apply them.

So what's the sneakier way than using setattr()? Every object has an attribute named __dict__ that is a dictionary representation of the writable attributes of an object. You can update dictionaries so you could do:

class Thief:
    def __init__(self, name, **kwargs):
        self.name = name
        self.__dict__.update(kwargs)
Usually, though, you don't want to update .__dict__ directly as it's mostly meant to be a read-only resource. Just because you can write to it doesn't mean you should!

'''

''' Notes about software design:
-- Keep your code as simple as possible
-- Don't repeat yourself (DRY)
-- Your code should have only the bells and whistles that it needs (YAGNI)
-- Write Python like Python, not like any other language

This is a great time to familiar yourself with PEP 8 and PEP 20, two documents that most Python developers use to guide what their code looks like and how they think about code while creating it.
'''