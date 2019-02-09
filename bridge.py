class Bridge:

    def __init__ (self, name, rarity, experience, material, type, strength, length, width, height):
        #can't be longer than 128 characters
        if (name is None):
            name = random.choice(["Archie","Bridget","Trussel"])
        else:
            self.name = name

        #will be an integer between 0 and 10
        self.rarity = rarity
        #integer between 0 and 100
        self.experience = experience
        #integer between 0 and 2
            #0 = wood
            #1 = stone
            #2 = metal
        self.material = material
        #integer between 0 and 5

        self.type = type
        #strength between 0 and 1000

        self.strength = strength
        self.length = length
        self.width = width
        self.height = height

def birth(parent1, parent2):
    rar = random.choice(parent1.rarity,parent2.rarity)
    experience = 0+max(0,parent1+parent2-100)
    material = random.choice(parent1.material,parent2.material)
    type = random.choice(parent1.type,parent2.type)
    strength = randint(.4*(parent1.strength+parent2.strength),.65*(parent1.))
    baby = Bridge(name = None, rarity = rar, )
    return baby

def built(price):
