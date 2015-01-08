
def composite_order(list_list):  
    # Why doesn't this work??:  
    # superlist = sum(list for list in list_list)
    superlist = []
    for list in list_list:
        superlist += list
    return sorted(superlist)