
% A-level / Level 0

\score{
  << \set Score.timing = ##f
  
  
  \new StaffGroup << % textural lines
  
  \new Staff{
    \override Stem #'transparent = ##t
    \override Stem #'length = #0
    \override Staff.TimeSignature.stencil = ##f 
    \override Staff.Rest.style = #'classical
    \key d\major
    
      <fis' a' d''>
 \bar "|."
} 
\new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  \clef bass
  \key d\major
  
  <d, d a> }
  >>
  % pitch-class lines
  
  \new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  \key d\major
  
  <d' fis' a' > }
  >>
} 




% B-level / Level 11

\score{
  << \set Score.timing = ##f
  
  
  \new StaffGroup << % textural lines
  
  \new Staff{
    \override Stem #'transparent = ##t
    \override Stem #'length = #0
    \override Staff.TimeSignature.stencil = ##f 
    \override Staff.Rest.style = #'classical
    \key d\major
    
      r4( <fis' a' d''>)
 \bar "|."
} 
\new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  \clef bass
  \key d\major
  
  d( <d, d a>) }
  >>
  % pitch-class lines
  
  \new Staff {
  \override Stem #'transparent = ##t
  \override Stem #'length = #0
  \override Staff.TimeSignature.stencil = ##f
  \override Staff.Rest.style = #'classical
  \key d\major
  
  <d' \parenthesize fis' \parenthesize a'> <d' fis' a' > }
  >>
} 


% C-level/ Level 10 

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
	    \mark \markup { \box "29" }
		<a' cis''>( << d''a' fis') \)>> \bar "|." 
		

	}
   \new Staff{
     \override Staff.TimeSignature.stencil = ##f     
     \override Stem #'transparent = ##t
     \override Stem #'length = #0
     \clef bass
     \key d \major
		 d e <a a,> << d, d a >>

   }  
   
   >>
   
   \new Staff {
                \override Stem #'transparent = ##t
                \override Stem #'length = #0                
                \override Staff.TimeSignature.stencil = ##f
                \key d \major
   <d' \parenthesize fis' \parenthesize a'> <d' e' gis' b'>
   <cis' e' a'> <d' fis' a'>
   }
  >>
   
  
	\layout{}
	\midi{}
}

% D-level/Level 9

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
	  
	    r4 ( <gis' b' d''>)
	    \mark \markup { \box "29" }
		<a' cis''>\( ( <g'' b' b>) \slurUp 
		
		\mark \markup { \box "51" }
		
		<cis'' e' > (  < d''a' fis'> )\) \bar "|." 
		

	}
   \new Staff{
     \override Staff.TimeSignature.stencil = ##f     
     \override Stem #'transparent = ##t
     \override Stem #'length = #0
     \clef bass
     \key d \major
		 d e <a a,> <g e>
		 
		 <g a> << d, d a >>

   }  
   
   >>
   
   \new Staff {
                \override Stem #'transparent = ##t
                \override Stem #'length = #0                
                \override Staff.TimeSignature.stencil = ##f
                \key d \major
   <d' \parenthesize fis' \parenthesize a'> <d' e' gis' b'>
   
   <cis' e' a'> <e' g' b'> <cis' e' a'> <d' fis' a'>
   }
  >>
   
  
	\layout{}
	\midi{}
}
