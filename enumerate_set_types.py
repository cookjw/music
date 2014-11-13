# CURRENT STATUS: needs efficiency improvement


from prime_form import find_prime_form

# print find_prime_form([6])

# print find_prime_form([])


# Procedure:
# - for each subset, find the prime form; if not already in list, add it.
# -- enumerate subsets
# --- for each cardinality between 1 and n/2, enumerate subsets of that
# cardinality, plus their complements
# ---- enumerate subsets of a given cardinality
# ----- if cardinality > 0, for each element, enumerate subsets of 
# complement of that element; then add element to a copy of each of those subsets
# ----- otherwise, in the base case of cardinality = 0, return [[]]


def enumerate_subsets(set):
    if len(set) == 0:
        subsets = [[]]
    else:        
        for element in set:
            complement = [x for x in set if x != element]
            complement_subsets = enumerate_subsets(complement)
            subsets = complement_subsets + ([subset + [element] 
                                               for subset in 
                                               complement_subsets])
    if len(subsets) == 2**(len(set)):                                            
        return ([sorted(subset) for subset in subsets])
    else:
        raise Exception("wrong number of subsets!")
    



def enumerate_set_types():
    types = []
    for set in enumerate_subsets(range(12)):
        if len(set) != 0:
            prime_form = find_prime_form(set)
            if not prime_form in types:
                types.append(prime_form)
                
# print len([x for x in enumerate_set_types() if len(x) >= 3])
        
    
        
# print enumerate_subsets([1,2,3,4])  

for n in range(12):
    print n, len(enumerate_subsets(range(n)))          
            
    

