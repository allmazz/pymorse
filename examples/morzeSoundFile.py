import pymorze

"""Generate sound(.wav) file"""

text = pymorze.to_morse("Привет, мир!", pymorze.ruMorseAlphabet)  # Encode text to Morze
# ['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--']

pymorze.gen_sound(text, "morze.wav")  # Generate file. text - Morze array; "morze.wav" - file name

"""Read sound(.wav) file"""

text2 = pymorze.read_sound("morze.wav")  # Read Morze from file
# ['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--']

print(pymorze.from_morse(text2, pymorze.ruMorseAlphabet))  # Encode Morze to text and print text
# Will be print "ПРИВЕТ, МИР!". Not "Привет, мир!" because not caps in Morze
