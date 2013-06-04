# rhythmic values in Perspectives II

import fracarithmetic
import listoperations


def dilate(array, num): 
    for i in range(len(array)):
        array[i] = fracarithmetic.mixednum(fracarithmetic.fractimes(fracarithmetic.improp(array[i]),num))
    return array
    

def timepoints(durations): 
    points = [[0,1], durations[0]]         
    for i in range(2, len(durations)+1):                
        points.append(fracarithmetic.mixednum(fracarithmetic.fracplus(fracarithmetic.improp(points[i-1]),fracarithmetic.improp(durations[i-1]))))
              
    return points      
    

def motivejuxtapose(motive1, motive2):
    T1 = [fracarithmetic.improp(x) for x in timepoints(motive1)]
    T2 = [fracarithmetic.fracplus(fracarithmetic.improp(x), T1[-1]) for x in timepoints(motive2)]
    L = T1 + T2               
    return listoperations.eliminate_duplicates([fracarithmetic.mixednum(x) for x in L])

def timejuxtapose(timepoints1, timepoints2):
    T1 = [fracarithmetic.improp(x) for x in timepoints1]
    T2 = [fracarithmetic.fracplus(fracarithmetic.improp(x), T1[-1]) for x in timepoints2]
    L = T1 + T2               
    return listoperations.eliminate_duplicates([fracarithmetic.mixednum(x) for x in L])
    

def timejuxtaposelist(list):
    L = list[0]
    for i in range(1,len(list)):
        L = timejuxtapose(L, list[i])
    return L
    
def motivejuxtaposelist(list):
    L = timepoints(list[0])
    for i in range(1,len(list)):
        L = timejuxtapose(L, timepoints(list[i]))
    return L

def timecombine(timepoints1, timepoints2):
    L = listoperations.eliminate_duplicates(fracarithmetic.fracsortlist([fracarithmetic.improp(x) for x in timepoints1 + timepoints2]))
    return [fracarithmetic.mixednum(x) for x in L]
    
def motivecombine(motive1, motive2):
    L = listoperations.eliminate_duplicates(fracarithmetic.fracsortlist([fracarithmetic.improp(x) for x in timepoints(motive1) + timepoints(motive2)]))
    return [fracarithmetic.mixednum(x) for x in L]

def timecombinelist(list):
    L = list[0]
    for i in range(1,len(list)):
        L = timecombine(L, list[i])
    return L
    
def motivecombinelist(list):
    L = timepoints(list[0])
    for i in range(1,len(list)):
        L = timecombine(L, timepoints(list[i]))
    return L
    
  
    
def combrhythm(motives, factor):
    return dilate(motivecombinelist(motives), factor)

    
def secrhythm(combos, factor):
    return timejuxtaposelist([combrhythm(x, factor) for x in combos])
    
    

    
def rhythm(sections):
    return timejuxtaposelist([secrhythm(sections[i][0],sections[i][1]) for i in range(len(sections))])
    


A = [[1,1], [4,1], [10,3], [22,15]]
B = [[4,5], [8,5], [4,5], [4,1]]
C = [[4,5], [12,5], [4,5], [6,1]]
D = [[1,1], [1,1], [4,3], [5,3]]

print rhythm([ [[[A],[B],[C],[D]], [1,1]], [[[A,B,C,D]],[4,1]], [[[A,B],[C,D]], [10,3]], [[[A,C],[B,D]], [22,5]], [[[A,B,C],[D]],[4,5]], [ [[A],[B,C,D]], [8,5]],
 [[[A,B],[D,C]], [4,5]], [[[A],[B],[C],[D]] , [4,1]],
  [[[A,B,C,D]], [4,5]], [[[A,B],[C,D]], [12,5]], [[[A,C], [B,D]], [4,5]]])








    
    