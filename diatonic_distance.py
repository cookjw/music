from operator import itemgetter
from prime_form import find_prime_form, find_normal_form




def lydian_index_of_pc(pc_1, pc_2):
    return ((pc_1 - pc_2)*7)%12    

def lydian_index_of_set(set, pc):
    return max([lydian_index_of_pc(x, pc) for x in set])     
    
def lydian_best_fit(set):
    lydian_indices = {}
    for pc in range(12):
        lydian_indices[pc] = lydian_index_of_set(set, pc)
    return sorted(lydian_indices.items(), key=itemgetter(1))


        
        
def locrian_index_of_pc(pc_1, pc_2):
    return ((pc_1 - pc_2)*5)%12
    
def locrian_index_of_set(set, pc):
    return max([locrian_index_of_pc(x, pc) for x in set])
    
    
def locrian_best_fit(set):
    locrian_indices = {}
    for pc in range(12):
        locrian_indices[pc] = locrian_index_of_set(set, pc)
    return sorted(locrian_indices.items(), key=itemgetter(1))
    
    
def true_normal_form(set):
    true_set = [(element*7)%12 for element in set]
    return find_normal_form(true_set)
    
def true_prime_form(set):
    true_set = [(element*7)%12 for element in set]
    return find_prime_form(true_set)