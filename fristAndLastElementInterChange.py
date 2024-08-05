def swapList(newList): 
    newList[0], newList[-1]=newList[-1], newList[0] 
    return newList

newList=[12,35,9,56,24] 
print("old list befor interchage: ", newList)
print("new list after interchnage:",swapList(newList)) 