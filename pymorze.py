# pymorze, library for Morze alphabet in Python. by allmaZz https://github.com/allmazz/
# Thanks luck20yan https://github.com/luck20yan for help with library. Special for read .wav file(ReadSound)
# Библиотека написанна для первого тура ЗПШ 2020

#FIXME learn PEP8
import wave
from math import pi, sin
from struct import pack
from numpy import std

# За русский алфавит Морзе я балогвдрен автору этой статьи: https://habr.com/ru/post/349776/

# Russian Morze alphabet, author: https://habr.com/ru/post/349776/

ruMorseAlphabet = {"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
                   "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
                   "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
                   "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--",
                   "Я": ".-.-", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                   "7": "--...", "8": "---..", "9": "----.", ".": "......", "0": "-----", ",": ".-.-.-", ":": "---...",
                   ";": "-.-.-.", "(": "-.--.-", ")": "-.--.-", "'": ".----.", "\"": ".-..-.", "-": "-....-",
                   "/": "-..-.", "?": "..--..", "!": "--..--", "@": ".--.-.", "=": "-...-", " ": " "}

#FIXME rename
def ToMorze(text, alphabet):  # From string to morze(array)
    morzeText = []  # Array for symbols
    for symbol in text.upper():
        if symbol not in alphabet:  # If symbol not in Morze dictionary
            raise Exception("Symbol '" + symbol + "' not in Morze alphabet")
        morzeText.append(alphabet[symbol])  # Append symbol
    return morzeText


#FIXME rename
def FromMorze(morzeText, alphabet):  # From morze(array) to string
    text = ""  # String for symbols
    for symbol in morzeText:
        for k, v in alphabet.items():
            if v == symbol:
                text += k  # Append symbol
    return text


#FIXME rename
def GenSound(morzeText, morzeFilename, volume=1.0, sample=44100, dotTime=150, frequency=700):  # Generate sound file(.wav)
    nowSymble = 0  # Counter
    morzeSound = []  # Sound frames
    samp = sample / 1000  # Sample / 1000
    syn = 2 * pi * frequency
    synPack0 = pack('h', 0)
    times = {"dot": [], "dash": [], "space": [], "delay1": [], "delay3": []}  # Dictionary for times
    for x in range(int(dotTime * samp)):  # Calculation (dotTime * 1)(for dot)
        times["dot"].append(pack('h', int(volume * sin(syn * (x / sample)) * 32767.0)))
    for x in range(int(dotTime * samp)):  # Calculation delay (dotTime * 1)(for separate symbols)
        times["delay1"].append(synPack0)
    times["dash"] = times["dot"] * 3  # Calculate dash (dotTime * 3)
    times["delay3"] = times["delay1"] * 3  # Calculate delay (dotTime * 3)(for separate character)
    times["space"] = times["delay1"] * 7  # Calculate delay (dotTime * 7)(for space)
    while nowSymble < len(morzeText):  # Every character
        nowMorzeSymbol = 0
        if morzeText[nowSymble] == " ":  # If space append times["space"] (delay dor space)
            morzeSound += times["space"]
        else:
            while nowMorzeSymbol < len(morzeText[nowSymble]):  # Every symbol
                if morzeText[nowSymble][nowMorzeSymbol] == ".":  # If dot append times["dot"] (delay dor dot)
                    morzeSound += times["dot"]
                elif morzeText[nowSymble][nowMorzeSymbol] == "-":  # If dash append times["dash"] (delay dor dash)
                    morzeSound += times["dash"]
                nowMorzeSymbol += 1
                if nowMorzeSymbol < len(morzeText[nowSymble]):  # If no last morzeSymbol in character append times["delay1"] (delay for morzeSymbol)
                    morzeSound += times["delay1"]
        nowSymble += 1
        if nowSymble < len(morzeText) and morzeText[nowSymble - 1] != " " and morzeText[nowSymble] != " ":  # If no last symbol in word append delay(for separate character)
            morzeSound += times["delay3"]
    morzeFile = wave.open(morzeFilename, "w")  # Open file
    morzeFile.setparams((1, 2, sample, 0, "NONE", "not compressed"))  # Set WAV parameters
    morzeFile.writeframes(b"".join(morzeSound)) # Write frames
    morzeFile.close()  # Close file


#FIXME rename
def ReadSound(morzeFilename, dotTime=150):  # Read from sound file(.wav)
    frames = []
    buf_frame = []
    w = wave.open(morzeFilename, "rb")
    # read .wav and create 0,1 array
    for i in range(0, w.getnframes()):
        s = w.readframes(1)
        f = int.from_bytes(s[:2], "big", signed=True)
        buf_frame.append(f)
        if len(buf_frame) == dotTime:
            if std(buf_frame) > 5000:
                frames.append(1)
            else:
                frames.append(0)
            buf_frame = []
    w.close()

    # get time beeps
    zero_or_one = frames[0]
    num = 0
    timeframe = []
    out = []
    for i in range(0, len(frames)):
        if zero_or_one != frames[i]:
            timeframe.append([num, zero_or_one])
            zero_or_one = frames[i]
            num = 0
        else:
            num += 1
    timeframe.append([num, zero_or_one])

    # create array array with morse charts
    print(timeframe)
    char = ""
    for i in timeframe:
        if i[1] == 0:
            if i[0] > 275:
                out.append(char)
                char = ""
                out.append(" ")
            elif i[0] > 50:
                out.append(char)
                char = ""
        else:
            if i[0] > 50:
                char += "-"
            elif i[0] > 15:
                char += "."
    return out.append(char)
