# londonBridge.py
 
from music import *

# Section 1
# Bar 1 / 5
pitch1 = [G4,  A4, G4, F4]
dur1 =   [DQN, EN, QN, QN]

# Bar 2 / 4 / 6
pitch2 = [E4, F4, G4]
dur2 =   [QN, QN, HN]

# Bar 3
pitch3 = [D4, E4, F4]
dur3 =   [QN, QN, HN]

# Bar 7
pitch4 = [D4, G4]
dur4 =   [HN, HN]

# Bar 8
pitch5 = [E4, C4]
dur5 =   [QN, DHN]

# Phrase
theme = Phrase()
theme.setTempo(120)
theme.addNoteList(pitch1, dur1)
theme.addNoteList(pitch2, dur2)
theme.addNoteList(pitch3, dur3)
theme.addNoteList(pitch2, dur2)
theme.addNoteList(pitch1, dur1)
theme.addNoteList(pitch2, dur2)
theme.addNoteList(pitch4, dur4)
theme.addNoteList(pitch5, dur4)

Play.midi(theme)