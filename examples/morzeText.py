import pymorze  # Import library pymorze
from timeit import default_timer as timer
# Encode from Russian text to Morze(with internal dictionary)
# text = ""
# start = timer()
# print(pymorze.ToMorze(text,
#                       pymorze.ruMorseAlphabet))  # Text - text to encode; pymorze.ruMorseAlphabet - Morze alphabet. Can be custom(must be dictionary: {"symbol": ".-."}
# end = timer()
# print(end - start)
# # Will be print ['.--.', '.-.', '..', '.--', '.', '-', '.-.-.-', ' ', '--', '..', '.-.', '--..--']
# # Every array element - one symbol. " " - is space :)
#
# # Encode from any language(not default in pymorze)
text2 = "Hola mundo!"  # Hello world in Spanish
# myDictionary = {"H": ".",
#                 "O": "-"}  # ... P.S it,s not correct Morze code in this example. Correct Morze codes for any language you can fine in internet
# print(pymorze.ToMorze(text2, myDictionary))  # Exception: Symbol 'L' not in Morze alphabet
# # Because symbol 'L' nt in our example Spanish alphabet
#
# start = timer()
# text3 = "КУ КУ"
# pymorze.GenSound(pymorze.ToMorze(text3,
#                       pymorze.ruMorseAlphabet), "sound2.wav")
#
# end = timer()
# print(end - start)


start = timer()
print(pymorze.FromMorze(pymorze.read_sound("sound.wav"), pymorze.ruMorseAlphabet))
end = timer()
print(end - start)