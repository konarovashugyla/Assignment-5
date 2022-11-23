
def unique(l):
    new_list= []
    for element in l:
        if element not in new_list:
            new_list.append(element)
    return new_list
#print(unique([8,9,9,7,6,5,5,3]))-> [8, 9, 7, 6, 5, 3] 