from prime_form import find_prime_form
from completeness import is_complete


def upward_resolution(pc, triad):
    for n in [1,2]:
        if (pc + n) % 12 in triad:
            return set([(pc + n) % 12])
    return set([])
    
def downward_resolution(pc, triad):
    for n in [1,2]:
        if (pc - n) % 12 in triad:
            return set([(pc - n) % 12])
    return set([])

def resolutions(pc, triad):
    return upward_resolution(pc, triad) | downward_resolution(pc, triad)
    


def dissonance_score(set, triad):
    if find_prime_form(triad) == [0,3,7] and is_complete(set):
        score = 0
        for pc in set - triad:            
            if resolutions(pc, triad) <= set:
                score += 1
            else:
                score += 2
        return score
    elif not find_prime_form(triad) == [0,3,7]:
        raise Exception("second argument must be a triad (type [0,3,7])")
    else:
        raise Exception("harmonically incomplete set")  

print dissonance_score({7,11,2}, {0,4,7})       

print dissonance_score({7,11,4}, {0,4,7}) 



        



    

    
    