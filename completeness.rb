# Checks whether a pc set is "complete", i.e. whether every pc is 
# reachable by conjunct motion (interval <= 2) from some pc in the 
# set. The central example, of course, is the triad (set-class [037]),
# for which reason I had been in the habit of mentally referring to these
# collections as "triadically complete"; but there exist collections not
# containing triads -- in fact, even collections of cardinality 3, such as
# those of type [027] -- that have this property. 


def reachable_by_step(pc)
  (-2..2).map {|x| (x + pc) %12}
end

def complete?(collection)
  all_reachable_by_step = []
  for pc in collection
    all_reachable_by_step += reachable_by_step(pc)    
  end
  for pc in (0...12)
    unless all_reachable_by_step.include?(pc)
      return false
    end
  end
  return true
end

print complete?([0,3,7])

print "\n"

print complete?([0,2,7])

print "\n"

print complete?([0,1,6])

print "\n"




