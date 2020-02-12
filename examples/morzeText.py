import pymorze  # Import library pymorze

# Encode from Russian text to Morze(with internal dictionary)
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

text3 = "Карл у Клары украл кораллы, а Клара у Карла украла кларнет. Если бы Карл у Клары не украл кораллы, то Клара у Карла не украла б кларнет "
pymorze.GenSound(pymorze.ToMorze(text3,
                      pymorze.ruMorseAlphabet), "test.wav")
print(pymorze.FromMorze(pymorze.ReadSound("test.wav"), pymorze.ruMorseAlphabet))
