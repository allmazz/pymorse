import pymorze

"""Generate sound(.wav) file"""

text = pymorze.ToMorze("Привет, мир!", pymorze.ruMorseAlphabet)  # Encode text to Morze
# ['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--']

pymorze.GenSound(text, "morze.wav")  # Generate file. text - Morze array; "morze.wav" - file name

"""Read sound(.wav) file"""

text2 = pymorze.ReadSound("morze.wav")  # Read Morze from file
# ['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--']

print(pymorze.FromMorze(text2, pymorze.ruMorseAlphabet))  # Encode Morze to text and print text
# Will be print "ПРИВЕТ, МИР!". Not "Привет, мир!" because not caps in Morze
