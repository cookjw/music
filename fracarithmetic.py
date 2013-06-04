# arithmetic with fractions

def max(a,b):
    if a >= b:
        return a
    elif a < b:
        return b
    else:
        return None

def min(a,b):
    if a<= b:
        return a
    elif a > b:
        return b
    else:
        return None

def gcd(num1,num2):
    a = max(num1, num2)
    b = min(num1, num2)
    r = a%b
    while r >0:
        a = b
        b = r
        r = a%b
    else:
        return b
        
def lcm(num1, num2):
    return num1*num2/gcd(num1, num2)
        
def reduce(frac):
    num = frac[0]
    denom = frac[1]
    if num == 0:
        return [0,1]
    else:
        return [num/gcd(num,denom), denom/gcd(num,denom)]
    
    
def fracplus(frac1, frac2):
    a = frac1[0]
    b = frac1[1]
    c = frac2[0]
    d = frac2[1]
    return reduce([a*d + b*c, b*d])
    
def fracminus(frac1, frac2):
    a = frac1[0]
    b = frac1[1]
    c = frac2[0]
    d = frac2[1]
    return reduce([a*d - b*c, b*d])

    
def fractimes(frac1, frac2):
    a = frac1[0]
    b = frac1[1]
    c = frac2[0]
    d = frac2[1]
    return reduce([a*c, b*d])
    
def recip(frac):
    return reduce([frac[1], frac[0]])
    
def fracdiv(frac1, frac2):
    return fractimes(frac1, recip(frac2))
    
    
def mixednum(frac):
    num = frac[0]
    denom = frac[1]
    if num > denom and reduce(frac)[1] != 1:
        return [num/denom, reduce([num%denom, denom])[0],reduce([num%denom, denom])[1]]
    else:
        return reduce(frac)
        
def improp(mixednum):
    if len(mixednum) > 2:
        return reduce(fracplus([mixednum[0]*mixednum[2],mixednum[2]], [mixednum[1], mixednum[2]]))
    else:
        return mixednum
    
def fracmax(frac1, frac2):
    a = float(frac1[0])
    b = float(frac1[1])
    c = float(frac2[0])
    d = float(frac2[1])
    if max(a/b, c/d) == a/b:
        return frac1
    elif max(a/b, c/d) == c/d:
        return frac2
   
    
def fracmin(frac1, frac2):
    a = float(frac1[0])
    b = float(frac1[1])
    c = float(frac2[0])
    d = float(frac2[1])
    if min(a/b, c/d) == a/b:
        return frac1
    elif min(a/b, c/d) == c/d:
        return frac2
        
def fraccheckorder(somelist):
        somelength = len(somelist)
        rightorder = True
        for index in range(somelength - 1):
            if fracmax(somelist[index], somelist[index + 1]) == somelist[index + 1]:
                continue
            else:
                rightorder = False
                break 
        return rightorder         
        
def fracsortlist(list):
    length = len(list)       
    while fraccheckorder(list) == False:     
        for index in range(length - 1):
            if fracmax(list[index], list[index + 1]) == list[index+1]:                
                continue
            else:
                a = list[index]
                b = list[index + 1]
                list[index] = b
                list[index + 1] = a
                        
    return list        
        

    
    
    

        
    
    

    

        
    

    