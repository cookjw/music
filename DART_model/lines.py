
class Line(list):
    def __init__(self, name, notes=None):
        self.name = name
        if  notes is not None:
            self.notes = notes
        else:
            self.notes = []
    
    def __repr__(self):
        return self.name + ": " + repr(list(self))
        
    
        
    
class PitchClassLine(Line): # notes move conjunctly in pitch-class space
    pass
    
class PitchLine(PitchClassLine): # notes move conjunctly in pitch-space
    pass
    
  
class TexturalLine(Line):
    pass
 
 
class InstrumentalLine(Line):
    pass


     