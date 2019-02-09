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
    rty = random.choice(parent1.rarity,parent2.rarity)
    exp = 0+max(0,parent1+parent2-100)
    mtrl = random.choice(parent1.material,parent2.material)
    typ = random.choice(parent1.type,parent2.type)
    str = randint(.4*(parent1.strength+parent2.strength),.65*(parent1.strength+parent2.strength))
    len = randint(.4*(parent1.strength+parent2.length),.65*(parent1.strength+parent2.length))
    wid = randint(.4*(parent1.strength+parent2.width),.65*(parent1.strength+parent2.width))
    hght = randint(.4*(parent1.strength+parent2.height),.65*(parent1.strength+parent2.height))
    baby = Bridge(name = None, rarity = rty, experience = exp, material = mtrl, type = typ, strength = str, length = len, width = wid, height = hght)
    return baby

def built(price):
    #price should be an integer between 0 and 3, depending on which option they selected in the store
    if (price == 0):
        rty = random.choices(population=[0,1,2,3,4], weights=[40,40,17,2,1], k=1)
    elif (price == 1):
        rty = random.choices(population=[0,1,2,3,4], weights=[10,30,45,10,5], k=1)
    elif (price == 2):
        rty = random.choices(population=[0,1,2,3,4], weights=[1,2,22,55,20], k=1)
    else:
        rty = random.choices(population=[0,1,2,3,4], weights=[1,2,7,35,50], k=1)

    exp = rty*3;
    typ = random.choice([0,1,2,3,4,5]);

    if (rty = 0):
        mtrl = random.choices(population=[0,1,2], weights = [60,40,5], k=1)
        str = randint(5,200)
        len = randint(10,900)
        wid = randint(1,3)
        hght = randint(0,2)
    elif (rty = 1):
        mtrl = random.choices(population=[0,1,2], weights = [40,45,10], k=1)
        str = randint(200,350)
        len = randint(750,1200)
        wid = randint(1,4)
        hght = randint(1,3)
    elif (rty = 2):
        mtrl = random.choices(population=[0,1,2], weights = [30,55,15], k=1)
        str = randint(400,600)
        len = randint(2000,10000)
        wid = randint(2,6)
        hght = randint(3,5)
    elif (rty = 3):
        mtrl = random.choices(population=[0,1,2], weights = [10,45,45], k=1)
        str = randint(600,800)
        len = randint(50000,100000)
        wid = randint(4,8)
        hght = randint(4,7)
    else:
        mtrl = random.choices(population=[0,1,2], weights = [5,25,75], k=1)
        str = randint(850,950)
        len = randint(100000,150000)
        wid = randint(4,9)
        hght = randint(7,8)

    #add something later that adjust things according to the material and whatnot
    newbie = Bridge(name = None, rarity = rty, experience = exp, material = mtrl, type = typ, strength = str, length = len, width = wid, height = hght)
    return newbie
