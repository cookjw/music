# Checks whether a pc set is "complete", i.e. whether every pc is 
# reachable by conjunct motion (interval <= 2) from some pc in the 
# set. The central example, of course, is the triad (set-class [037]),
# for which reason I had been in the habit of mentally referring to these
# collections as "triadically complete"; but there exist collections not
# containing triads -- in fact, even collections of cardinality 3, such as
# those of type [027] -- that have this property. 


def reachable_by_step(pc):
    return [(x + pc) % 12 for x in range(-2,3)]
    
def is_complete(collection):
    all_reachable_by_step = []
    for pc in collection:
        all_reachable_by_step += reachable_by_step(pc)
    for pc in range(12):
        if not pc in all_reachable_by_step:
            print "unreachable: " + str(pc)
            return False
    return True   
    
    
    
if __name__ == '__main__':    
# print is_complete([0,3,7])

# print is_complete([0,2,7])

# print is_complete([0,1,6])

    input = raw_input("Enter pcs in set, separated by commas. \n")

    collection = [int(pc) for pc in input.split(",")]
                            
    if is_complete(collection):
        print "Complete."

    else:
        print "Not complete."    

    