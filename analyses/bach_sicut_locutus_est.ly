


\score{  
  
  << \set Score.timing = ##f
  
   \new StaffGroup<<
 %\set PianoStaff.followVoice = ##t
  
  
  
  \new Staff{ 
	\override Staff.TimeSignature.stencil = ##f	 
	 \override Staff.Rest.style = #'classical	  
	 \override Stem #'transparent = ##t
	  \override Stem #'length = #0
	  
	  \key d \major 
	  
	    r4\( ( <gis' b' d''>)
		<a' cis''>( << d''a' fis') \)>> \bar "|." 
		
		\break
		
		a' b' c''
	}
   \new Staff{
     \override Staff.TimeSignature.stencil = ##f     
     \override Stem #'transparent = ##t
     \override Stem #'length = #0
     \clef bass
     \key d \major
		 d e <a a,> << d, d a >>
		 \break 
		 
		 a b c
   }  
   
   >>
   
   \new Staff {
                \override Stem #'transparent = ##t
                \override Stem #'length = #0                
                \override Staff.TimeSignature.stencil = ##f
                \key d \major
   <d' fis' a'> <d' e' gis' b'> <cis' e' a'> <d' fis' a'>
   }
  >>
   
  
	\layout{}
	\midi{}
}

\score{
  << \set Score.timing = ##f
  
  
  \new StaffGroup <<
  
  \new Staff{
    \override Stem #'transparent = ##t
    \override Stem #'length = #0
    \override Staff.TimeSignature.stencil = ##f a'b' c''
    \override Staff.Rest.style = #'classical
} 
\new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  a' b' c''}
  >>
  
  \new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  a' b' c''}
  >>
} 