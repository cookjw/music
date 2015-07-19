# (Ruby version of exercise_generator.py)

# This program automatically generates parameters for compositional 
# exercises of a type I invented in late 2012. Integral to their 
# nature is the randomness of the parameters generated for 
# each new exercise: the intention is that the composer be forced to
# confront novel compositional situations outside of his or her 
# "typical" experience, and thereby be stimulated to develop a 
# larger compositional vocabulary and experience creative growth.

require 'set'

class EnsembleError < StandardError
  
end

def score_order(ensemble, convention)  
    indices = ensemble.map {|instrument| convention.index(instrument)}
    if indices.include?(nil)
      raise EnsembleError, "You have un-convention-al instruments!"
    end  
    ordered_ensemble = indices.select{|index| ensemble.include?(
                                       convention[index])}.
                                       map{|index| convention[index]}
    if ensemble.to_set == ordered_ensemble.to_set
      return ordered_ensemble        
    else
      raise EnsembleError,
        "Instrument set somehow got changed during reordering."    
    end
end
    
def generate_ensemble(number, instrument_list)
  ensemble = []
  for instrument_number in (0...number)
    instrument = instrument_list.sample
    ensemble.push(instrument)
  end
  return ensemble
end    


pcs = {0 => ["B#", "C"], 1 => ["C#", "Db"], 2 => ["D"], 3 => ["D#", "Eb"],
           4 => ["E", "Fb"] , 5 => ["E#, F"] , 6 => ["F#", "Gb"] , 7 => ["G"], 
           8 => ["G#", "Ab"] , 9 => ["A"] , 
           10 => ["A#", "Bb"] , 11 => ["B", "Cb"] }  
modes = ["major", "minor"]
span_types = ["open", "closed"]
instrument_list = ["Piccolo", "Flute", "Alto Flute", "Oboe", "English Horn", 
                  "Eb Clarinet", "Bb (or A) Clarinet", "Alto Clarinet",
                  "Bass Clarinet",
                  "Bassoon", "Contrabassoon", "Horn", "Trumpet", "Trombone",
                  "Euphonium", "Tuba", "Glockenspiel", "Xylophone", "Marimba",
                  "Celesta", "Harp", "Piano (R.H.)", "Piano (L.H.)",
                  "Guitar",
                  "Soprano Voice", "Alto Voice", "Tenor Voice", "Bass Voice",
                  "Violin", "Viola", "Violoncello", "Double Bass"]
#events = rand(10...100).to_s
tempo = rand(40...150).to_s
beats = rand(10...30).to_s
textural_lines = rand(1...10).to_s
instruments = rand(1...10)
ensemble = score_order(generate_ensemble(instruments, instrument_list),
                        instrument_list
                        ).to_s
tonic = pcs[rand(0...12)].sample
mode = modes.sample

now = Time.now.strftime("%Y-%m-%d %H:%M:%S")

output = "Composition Exercise Parameters (v. 2.0), generated #{now} 
         
         Tempo: #{tempo}
         Beats: #{beats}
         Textural Lines: #{textural_lines}
         Instruments in Ensemble: #{ensemble}
         Key: #{tonic} #{mode}"
         
File.open('exercise_parameters.txt', 'a') { |file| file.write("\n \n" + output) }

puts output

