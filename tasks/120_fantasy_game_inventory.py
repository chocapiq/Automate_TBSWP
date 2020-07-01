from collections import Counter
import random

def displayInventory(inventory, loot=0):
    if loot == 0:
        print("Your current inventory has:")
    else:
        print("You looted from dragon:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    newInventory = Counter(inventory) + Counter(addedItems)
    return newInventory

def randomizeDragonLoot():
    dragonLootD = {}
    dragonLoot = []
    a = 0
    b = 0
    c = 0
    goldcoinCount = random.randint(5,15)
    healthpotionCount = random.randint(0,4)
    torchCount = random.randint(0,2)
    rubyCount = random.randint(1,10)
    sapphireCount = random.randint(1,20)
    while a < goldcoinCount:
        dragonLoot.append('gold coin')
        a += 1
    while b < healthpotionCount:
        dragonLoot.append('health potion')
        b += 1
    while c < torchCount:
        dragonLoot.append('torch')
        c += 1
    if rubyCount == 3:
        dragonLoot.append('ruby')
    if sapphireCount == 5:
        dragonLoot.append('sapphire')
    for i in dragonLoot:
        dragonLootD.setdefault(i, 0)
        dragonLootD[i] += 1
    return dragonLootD



inv = {'gold coin': 42, 'rope': 1}
dragonLoot = randomizeDragonLoot()
addToInventory(inv, dragonLoot)
inv = addToInventory(inv, dragonLoot)
displayInventory(dragonLoot, 1)
displayInventory(inv)