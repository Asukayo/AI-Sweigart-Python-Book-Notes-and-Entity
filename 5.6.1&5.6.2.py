Inventory = {'rope':1,'torch':6,'goldCoin':266,'dagger':4}
dragonLoot = ['goldCoin','dagger','rope','ruby']
def displayInventory(inventory):
    totalItemsNum = 0
    print('Inventory:')
    for k,v in inventory.items():
        totalItemsNum += v
        print(str(inventory[k])+' '+str(k))
    print('Total number of items: '+str(totalItemsNum))

def addLootToInventory(inventory,loot):
    for l in loot:
        if inventory.get(l,0)==0:
            inventory[l] = 1
        else:
            inventory[l] +=1


print('Before kill the Dragon')
displayInventory(Inventory)

addLootToInventory(Inventory,dragonLoot)
print('After kill the Dragon')
displayInventory(Inventory)

