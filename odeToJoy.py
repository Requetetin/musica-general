# odeToJoy.py

from music import *

# Section 1
# Bar 1 / 5 / 13
pitch1 = [E4, E4, F4, G4]
dur1 =   [QN, QN, QN, QN]

# Bar 2 / 6 / 14
pitch2 = [G4, F4, E4, D4]
dur2 =   [QN, QN, QN, QN]

# Bar 3 / 7 / 15
pitch3 = [C4, C4, D4, E4]
dur3 =   [QN, QN, QN, QN]

# Bar 4
pitch4 = [E4,  D4, D4]
dur4 =   [DQN, EN, HN]

# Bar 8 / 16
pitch5 = [D4,  C4, C4]
dur5 =   [DQN, EN, HN]

# Bar 9
pitch6 = [D4, D4, E4, C4]
dur6 =   [QN, QN, QN, QN]

# Bar 10
pitch7 = [D4, E4, F4, E4, C4]
dur7 =   [QN, EN, EN, QN, QN]

# Bar 11
pitch8 = [D4, E4, F4, E4, D4]
dur8 =   [QN, EN, EN, QN, QN]

# Bar 12
pitch9 = [C4, D4, G3]
dur9 =   [QN, QN, HN]

# Phrase
theme = Phrase()
theme.setTempo(120)
theme.addNoteList(pitch1, dur1)
theme.addNoteList(pitch2, dur2)
theme.addNoteList(pitch3, dur3)
theme.addNoteList(pitch4, dur4)
theme.addNoteList(pitch1, dur1)
theme.addNoteList(pitch2, dur2)
theme.addNoteList(pitch3, dur3)
theme.addNoteList(pitch5, dur5)
theme.addNoteList(pitch6, dur6)
theme.addNoteList(pitch7, dur7)
theme.addNoteList(pitch8, dur8)
theme.addNoteList(pitch9, dur9)
theme.addNoteList(pitch1, dur1)
theme.addNoteList(pitch2, dur2)
theme.addNoteList(pitch3, dur3)
theme.addNoteList(pitch5, dur5)

Play.midi(theme)