 # drumRythm3.py
 # Double Kick Offset Drum Pattern
 
from music import *

repetitions = 4

score = Score("One Two Drum Pattern", 180.0)

drumsPart = Part("Drums", 0, 9)
 
bassDrumPhrase = Phrase(0.0)
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)

##### create musical data
 
# Kick
bassPitches   = [BDR] + [REST] + [BDR] + [REST] * 4 + [BDR] * 2 + [REST] + [BDR] + [REST] * 5
bassDurations = [EN] * 16
bassDrumPhrase.addNoteList(bassPitches, bassDurations)
 
# Snare
snarePitches   = [REST] * 4 + [SNR] + [REST] * 7 + [SNR] + [REST] * 3
snareDurations = [EN] * 16
snareDrumPhrase.addNoteList(snarePitches, snareDurations)
 
# hi-hat
hiHatPitches   = [CHH, REST] * 8
hiHatDurations = [EN, EN] * 8
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)
 
##### repeat material as needed
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(snareDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions)
 
##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(snareDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)
score.addPart(drumsPart)
 
##### view and play
View.sketch(score)
Play.midi(score)
Write.midi(score, "drumRythm3.mid")