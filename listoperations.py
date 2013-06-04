def checkorder(somelist):
        somelength = len(somelist)
        rightorder = True
        for index in range(somelength - 1):
            if somelist[index] <= somelist[index + 1]:
                continue
            else:
                rightorder = False
                break 
        return rightorder 


def sortlist(list):
    length = len(list)       
    while checkorder(list) == False:     
        for index in range(length - 1):
            if list[index] <= list[index + 1]:
                continue
            else:
                a = list[index]
                b = list[index + 1]
                list[index] = b
                list[index + 1] = a
                        
    return list


def listmax(list):
    newlist = sortlist(list)
    maxindex = len(newlist) - 1
    return newlist[maxindex]
    
def listsum(list):
    length = len(list)
    total = 0
    for i in range(length):
        total = total+list[i]
    return total
    
def listprod(list):
    length = len(list)
    product = list[0]
    for i in range(1,length):
        product = product*list[i]
    return product

def listcount(list, item):
    L = []
    for x in list:
        if x == item:
            L.append(x)
    return len(L)       

def eliminate_duplicates(list):
	for item in list:
		while listcount(list, item) > 1:
		    list.remove(item)
	return list
    
    
def getindices(item, list):
    listlength = len(list)
    L = []
    for index in range(listlength):
        if list[index] == item:
            L.append(index)
    return L
    