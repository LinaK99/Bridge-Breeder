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
            #0 = beam
            #1 = truss
            #2 = arch
            #3 = cantilever
            #4 = suspension
            #5 = cable-stayed
        self.type = type
        #integer between 0 and 1000
        self.strength = strength
        #integer between 0 and 200000
        self.length = length
        #integer between 1 and 10
        self.width = width
        #integer between 0 and 9
        self.height = height

def birth(parent1, parent2):
    rar = random.choice(parent1.rarity,parent2.rarity)
    experience = 0+max(0,parent1+parent2-100)
    material = random.choice(parent1.material,parent2.material)
    type = random.choice(parent1.type,parent2.type)
    strength = randint(.4*(parent1.strength+parent2.strength),.65*(parent1.strength+parent2.strength))
    baby = Bridge(name = None, rarity = rar, )
    return baby

def built(price):
