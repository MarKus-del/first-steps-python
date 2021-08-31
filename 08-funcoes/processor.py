from typing import List


def process_numbers(lista):
    if isinstance(lista, list) == False:
        return []
    
    number_list = []
    for item in lista:
        if isinstance(item, int):
            number_list.append(item)
        elif isinstance(item, str) and item.isnumeric():
            number_list.append(int(item))
    
    number_list.sort()
    return number_list

def process_names(lista):
    if isinstance(lista, list) == False:
        return []
    
    names_list = []
    for item in lista:
        if isinstance(item, str) and not item.isnumeric():
            names_list.append(item)
    
    names_list.sort()
    return names_list