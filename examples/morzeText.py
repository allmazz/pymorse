import pymorze  # Import library pymorze

"""Encoding to Morze"""
# Encode from Russian text to Morze(with an internal dictionary)
text = "Привет, мир!"
print(pymorze.ToMorze(text,
                      pymorze.ruMorseAlphabet))  # Text - text to encode; pymorze.ruMorseAlphabet - Morze alphabet. Can be custom(must be dictionary: {"symbol": ".-."}
# Will be print ['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--']
# Every array element - one symbol. " " - is space :)

# Encode from any language(not default in pymorze)
text2 = "Hola mundo!"  # Hello world in Spanish
myDictionary = {"H": ".",
                "O": "-"}  # ... P.S it,s not correct Morze code in this example. Correct Morze codes for any language you can fine in internet
print(pymorze.ToMorze(text2, myDictionary))  # Exception: Symbol 'L' not in Morze alphabet
# Because symbol 'L' nt in our example Spanish alphabet

"""Decoding from Morze"""
# Decode "Привет, мир!" encoded in first example to Russian text to Morze(with an internal dictionary)
print(pymorze.FromMorze(['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--'],
                      pymorze.ruMorseAlphabet))  # Text - text to encode; pymorze.ruMorseAlphabet - Morze alphabet. Can be custom(must be dictionary: {"symbol": ".-."}
# Will be print "ПРИВЕТ, МИР!". Not "Привет, мир!" because not caps in Morze

# Decode from Morze to any language(not default in pymorze)
myDictionary = {"H": ".",
                "O": "-"}  # ... P.S it,s not correct Morze code in this example. Correct Morze codes for any language you can fine in internet
print(pymorze.ToMorze([".-.", ".-"], myDictionary))  # Exception: Symbol '.-.' not in Morze alphabet
# Because symbol 'L' nt in our example Spanish alphabet