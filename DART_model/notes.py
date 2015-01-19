

class Note:
    def __init__(
    self, lines, onset_time=None, duration=None, pitch_class=None,
    pitch=None, instrument=None
    ):
        if isinstance(lines, list):
            self.lines = lines
        else:
            self.lines = [lines]
        self.duration = duration
        self.pitch_class = pitch_class
        self.pitch = pitch
        
        
class PitchClass:
    def __init__(self, pc):
        self.pc_number = get_pc_number(pc)           
 
def get_pc_number(pc):
    pc_dict = {"A":9, "B":11, "C":0, "D":2, "E":4, "F":5, "G":7} 
    if isinstance(pc, int):
        return pc % 12
    elif isinstance(pc, str):
        if len(pc) == 1:
            if pc.upper() == "H":
               raise Exception(
               "Are you German? (Perhaps you meant B...)"
               )
            else:
                return pc_dict[pc.upper()]
        else:
            pc_number = pc_dict[pc[0].upper()]
            for symbol in pc[1:]:
                if symbol == "b":
                    pc_number -= 1
                elif symbol == "#":
                    pc_number += 1
                elif symbol == "x":
                    pc_number += 2
                else:
                    raise Exception("I don't understand the input.")
            return pc_number                   
    
    else:
        raise Exception("pc must be int or str")
        
if __name__ == "__main__":
    pc = raw_input("Enter a pitch class. \n")
    print "pc number: {}".format(get_pc_number(pc))
    
            