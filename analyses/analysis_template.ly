\score{
  << \set Score.timing = ##f
  
  
  \new StaffGroup <<
  
  \new Staff{
    \override Stem #'transparent = ##t
    \override Stem #'length = #0
    \override Staff.TimeSignature.stencil = ##f 
    \override Staff.Rest.style = #'classical
    
    a'\( (b')
    \mark \markup { \box "29" }
    c''\) r4 \bar "|."
} 
\new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  \clef bass
  
  a, b, c r4 }
  >>
  
  \new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  
  a'\( (b') c''\) r4}
  >>
} 