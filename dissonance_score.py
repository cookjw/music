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
        raise Exception("second argument must be a triad (type [037])")
    else:
        raise Exception("harmonically incomplete set")  

if __name__ == "__main__":
    input_set = raw_input(
    """
    Enter a pc set (integers mod 12, separated by commas).
    Set must be harmonically complete, i.e. every chromatic pc
    must within an interval of <= 2 of some pc in the set.
    """
    )
    input_triad = raw_input(
    "Enter a triad (in form of pc set, e.g. 0,4,7 for C major) \n"
    )
    pc_set = set([int(pc) for pc in input_set.split(",")])
    triad = set([int(pc) for pc in input_triad.split(",")])
    
    print "dissonance score: " + str(dissonance_score(pc_set, triad))
    




        



    

    
    