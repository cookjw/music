# This program automatically generates parameters for compositional 
# exercises of a type I invented in late 2012. These exercises may be
# thought of as a modern analogue of species counterpoint, 
# and allow one to practice thinking in terms of my musical theory
# (itself invented simultaneously in late 2012). Integral to their 
# nature, however, is the randomness of the parameters generated for 
# each new exercise: the intention is that the composer be forced to
# confront novel compositional situations outside of his or her 
# "typical" experience, and thereby be stimulated to develop a 
# larger compositional vocabulary and experience creative growth.

from random import choice, randrange
from time import strftime


class EnsembleError(Exception):
    pass

def score_order(ensemble, convention):
    try:
        indices = sorted([convention.index(instrument)
                            for instrument in ensemble])
    except ValueError:
        raise EnsembleError("You have un-convention-al instruments!")
    ordered_ensemble = [convention[index] for index in indices
                           if convention[index] in ensemble]
    if set(ensemble) == set(ordered_ensemble):
        return ordered_ensemble
    else:
        raise EnsembleError(
            "Instrument set somehow got changed during reordering."
            )  
        
def generate_ensemble(number, instrument_list):
    ensemble = []
    for instrument_number in range(number):
        instrument = choice(instrument_list)
        ensemble.append(instrument)
    return ensemble
    
    
pcs = {0: ["B#", "C"], 1: ["C#", "Db"], 2: ["D"], 3: ["D#", "Eb"],
           4: ["E", "Fb"] , 5: ["E#, F"] , 6: ["F#", "Gb"] , 7: ["G"], 
           8: ["G#", "Ab"] , 9: ["A"] , 
           10: ["A#", "Bb"] , 11: ["B", "Cb"] }
modes = ["major", "minor"]
instrument_list = ["Piccolo", "Flute", "Alto Flute", "Oboe", "English Horn", 
                  "Eb Clarinet", "Bb (or A) Clarinet", "Alto Clarinet",
                  "Bass Clarinet",
                  "Bassoon", "Contrabassoon", "Horn", "Trumpet", "Trombone",
                  "Euphonium", "Tuba", "Glockenspiel", "Xylophone", "Marimba",
                  "Celesta", "Harp", "Piano (R.H.)", "Piano (L.H.)",
                  "Guitar", "Mandolin", "Lute", "Ukelele",
                  "Soprano Voice", "Alto Voice", "Tenor Voice", "Bass Voice",
                  "Violin", "Viola", "Violoncello", "Double Bass"]

events = str(randrange(10, 100))
beats = str(randrange(10, 30))
textural_lines = str(randrange(1, 10))
instruments = randrange(1, 10)
ensemble = str(score_order(generate_ensemble(instruments, instrument_list),
                               instrument_list,
                               ))                
tonic = choice(pcs[randrange(12)])
mode = choice(modes)

now = strftime("%Y-%m-%d %H:%M:%S")

output = """Composition Exercise Parameters, generated {now}         
         Events: {events}
         Beats: {beats}
         Textural Lines: {textural_lines}
         Instruments in Ensemble: {ensemble}
         Key: {tonic} {mode}""".format(now=now, events=events, beats=beats, 
                                          textural_lines=textural_lines,
                                          ensemble=ensemble,
                                          tonic=tonic, mode=mode)
                                          
#Saving the output in a text file, since each exercise is unique and special...
f = open('exercise_parameters.txt', 'a')
f.write("\n \n" + output)
f.close()

print output

    
    




        



        
    
    
          
          