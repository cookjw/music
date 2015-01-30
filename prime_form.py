#CURRENT_STATUS: seems to work.


#This is an implementation of the Forte algorithm for computing the
#prime form of a pitch-class set. See e.g.
#http://composertools.com/Theory/PCSets/PCSets3.htm.

#TODO: also implement Rahn-Morris algorithm



def remove_duplicates(list): # Shouldn't this be built in?
    new_list = []
    for item in list:
        if not item in new_list:
            new_list.append(item)
    return new_list
    
def rotate(pc_set, number): # "pc_set" is actually a list
    return pc_set[number:] + pc_set[:number]
    
def distance(pc_set):
    return (pc_set[-1] - pc_set[0]) % 12
    
def tiebreaker(candidate_list, cardinality):
    n = 2
    list = candidate_list
    while len(list) > 1:
        list = remove_duplicates([candidate for candidate in 
                                    list if distance(
                                    candidate[:n]
                                    )
                                    == min(
                                    [distance(pc_set[:n]) for 
                                     pc_set in list])])
        n += 1
        if n > cardinality: 
            raise Exception(
            "the variable n has gotten larger than it was supposed to."
            )
    return list[0]     

def find_normal_form(pc_set):
    pc_set = sorted(remove_duplicates(pc_set))
    rotations = [rotate(pc_set, i) for i in range(len(pc_set))]
    distances = [distance(pc_set) for pc_set in rotations]
    minimum_distance = min(distances)
    minimum_distance_list = remove_duplicates([rotation for rotation in
                                               rotations if 
                                               distance(rotation) ==
                                               minimum_distance])                                                       
    if len(minimum_distance_list) == 1:
        normal_form = minimum_distance_list[0]
        
    else:
        normal_form = tiebreaker(minimum_distance_list, len(pc_set))
    normal_form_from_zero = [(x - normal_form[0]) % 12 for x in normal_form]
    return normal_form_from_zero    
        
def find_prime_form(pc_set):
    pc_set = find_normal_form(pc_set)
    inversion = find_normal_form([(0 - x) % 12 for x in pc_set])
    candidates = [pc_set, inversion]
    minimum_distance_list = remove_duplicates([candidate for candidate in
                                               candidates if
                                               distance(candidate) == 
                                               min([distance(cand) for
                                                    cand in
                                                    candidates])])
    prime_form = tiebreaker(minimum_distance_list, len(pc_set))
    return prime_form

# print find_prime_form([0,5,6]) 

# print find_prime_form([2,4,5,7,9])   
    
# print find_normal_form([0,7,6])




            
    