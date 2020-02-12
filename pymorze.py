# pymorze, library for Morze alphabet in Python. by allmaZz https://github.com/allmazz/
# Библиотека написанна для первого тура ЗПШ 2020

import wave
import math
import struct

# За русский алфавит Морзе я балогвдрен автору этой статьи: https://habr.com/ru/post/349776/

# Russian Morze alphabet, author: https://habr.com/ru/post/349776/
import numpy

ruMorseAlphabet = {"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
                   "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
                   "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
                   "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--",
                   "Я": ".-.-", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                   "7": "--...", "8": "---..", "9": "----.", ".": "......", "0": "-----", ",": ".-.-.-", ":": "---...",
                   ";": "-.-.-.", "(": "-.--.-", ")": "-.--.-", "'": ".----.", "\"": ".-..-.", "-": "-....-",
                   "/": "-..-.", "?": "..--..", "!": "--..--", "@": ".--.-.", "=": "-...-", " ": " "}


def ToMorze(text, alphabet):  # From string to morze(array)
    morzeText = [] # Array for symbols
    for symbol in text.upper():
        if symbol not in alphabet: # If symbol not in Morze dictionary
            raise Exception("Symbol '" + symbol + "' not in Morze alphabet")
        morzeText.append(alphabet[symbol]) # Append symbol
    return morzeText


def FromMorze(morzeText, alphabet):  # From morze(array) to string
    text = "" # String for symbols
    for symbol in morzeText:
        for k, v in alphabet.items():
            if v == symbol:
                text += k # Append symbol
    return text


def GenSound(morzeText, morzeFilename, volume=1.0, sample=44100, time=300, frequency=700):  # Generate sound file(.wav)
    nowSymble = 0 # Counter
    morzeSound = [] # Sound frames
    time3 = time * 3 # Time * 3(for delay, and long signal(dash))
    time7 = time * 7 # Time * 7(for space)
    while nowSymble < len(morzeText):
        nowMorzeSymbol = 0
        if morzeText[nowSymble] == " ": # If space append time7
            for x in range(int(time7 * (sample / 1000.0))):
                morzeSound.append(0.0)
        else:
            while nowMorzeSymbol < len(morzeText[nowSymble]):
                print(morzeText[nowSymble][nowMorzeSymbol])
                if morzeText[nowSymble][nowMorzeSymbol] == ".":  # If point append time
                    for x in range(int(time * (sample / 1000.0))):
                        morzeSound.append(volume * math.sin(2 * math.pi * frequency * (x / sample)))
                elif morzeText[nowSymble][nowMorzeSymbol] == "-":  # If dash append time3
                    for x in range(int(time3 * (sample / 1000.0))):
                        morzeSound.append(volume * math.sin(2 * math.pi * frequency * (x / sample)))
                nowMorzeSymbol += 1
                if nowMorzeSymbol < len(morzeText[nowSymble]): # If no last morzeSymbol in symbol append delay(time * 1)
                    for x in range(int(time * (sample / 1000.0))):
                        morzeSound.append(0.0)
        nowSymble += 1
        if nowSymble < len(morzeText): # If no last symbol in word append delay(time3)
            for x in range(int(time3 * (sample / 1000.0))):
                morzeSound.append(0.0)
    morzeFile = wave.open(morzeFilename, "w") # Write to file. Open file
    morzeFile.setparams((1, 2, sample, 0, "NONE", "not compressed")) # Set WAV parameters
    for frame in morzeSound: # Append frames
        morzeFile.writeframes(struct.pack('h', int(frame * 32767.0)))
    morzeFile.close() # Close file


def ReadSound(morzeFilename, time=300): # Read from sound file(.wav)
    w = wave.open(morzeFilename, "rb")
    frames = []
    for i in range(0, w.getnframes()):
        s = w.readframes(1)
        f = int.from_bytes(s[:2], "big", signed=True)
        if f > 10000 or i < -10000:
            frames.append(1)
        else:
            frames.append(0)
    w.close()
    print(frames)