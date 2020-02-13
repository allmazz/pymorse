# pymorse, library for morse alphabet in Python. by allmaZz https://github.com/allmazz/
# Thanks luck20yan https://github.com/luck20yan for help with library. Special for read .wav file(ReadSound)
# Библиотека написанна для первого тура ЗПШ 2020

import wave
from math import pi, sin
from struct import pack
from numpy import std

# За русский алфавит Морзе я балогвдрен автору этой статьи: https://habr.com/ru/post/349776/

# Russian Morse alphabet, author: https://habr.com/ru/post/349776/

ruMorseAlphabet = {"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
                   "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
                   "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
                   "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--",
                   "Я": ".-.-", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                   "7": "--...", "8": "---..", "9": "----.", ".": "......", "0": "-----", ",": ".-.-.-", ":": "---...",
                   ";": "-.-.-.", "(": "-.--.-", ")": "-.--.-", "'": ".----.", "\"": ".-..-.", "-": "-....-",
                   "/": "-..-.", "?": "..--..", "!": "--..--", "@": ".--.-.", "=": "-...-", " ": " "}


def to_morse(text, alphabet):  # From string to morse(array)
    morse_text = []  # Array for symbols
    for symbol in text.upper():
        if symbol not in alphabet:  # If symbol not in morse dictionary
            raise Exception("Symbol '" + symbol + "' not in morse alphabet")
        morse_text.append(alphabet[symbol])  # Append symbol
    return morse_text


def from_morse(morse_text, alphabet):  # From morse(array) to string
    text = ""  # String for symbols
    for symbol in morse_text:
        for k, v in alphabet.items():
            if v == symbol:
                text += k  # Append symbol
    return text


def gen_sound(morse_text, morse_filename, volume=1.0, sample=44100, dot_time=150, frequency=700):  # Generate sound file(.wav)
    now_symble = 0 # Counter
    morse_sound = []  # Sound frames
    samp = sample / 1000
    syn = 2 * pi * frequency
    syn_pack0 = pack('h', 0) # Prepare pach for delay
    times = {"dot": [], "dash": [], "space": [], "delay1": [], "delay3": []}  # Dictionary for times
    for x in range(int(dot_time * samp)):  # Calculation (dotTime * 1)(for dot)
        times["dot"].append(pack('h', int(volume * sin(syn * (x / sample)) * 32767.0)))
    for x in range(int(dot_time * samp)):  # Calculation delay (dotTime * 1)(for separate symbols)
        times["delay1"].append(syn_pack0)
    times["dash"] = times["dot"] * 3  # Calculate dash (dotTime * 3)
    times["delay3"] = times["delay1"] * 3  # Calculate delay (dotTime * 3)(for separate character)
    times["space"] = times["delay1"] * 7  # Calculate delay (dotTime * 7)(for space)
    while now_symble < len(morse_text):  # Every character
        nowmorse_symbol = 0 # Counter
        if morse_text[now_symble] == " ":  # If space append times["space"] (delay dor space)
            morse_sound += times["space"]
        else:
            while nowmorse_symbol < len(morse_text[now_symble]):  # Every symbol
                if morse_text[now_symble][nowmorse_symbol] == ".":  # If dot append times["dot"] (delay dor dot)
                    morse_sound += times["dot"]
                elif morse_text[now_symble][nowmorse_symbol] == "-":  # If dash append times["dash"] (delay dor dash)
                    morse_sound += times["dash"]
                nowmorse_symbol += 1
                if nowmorse_symbol < len(morse_text[now_symble]):  # If no last morseSymbol in character append times["delay1"] (delay for morseSymbol)
                    morse_sound += times["delay1"]
        now_symble += 1
        if now_symble < len(morse_text) and morse_text[now_symble - 1] != " " and morse_text[now_symble] != " ":  # If no last symbol in word append delay(for separate character)
            morse_sound += times["delay3"]
    morse_file = wave.open(morse_filename, "w")  # Open file
    morse_file.setparams((1, 2, sample, 0, "NONE", "not compressed"))  # Set WAV parameters
    morse_file.writeframes(b"".join(morse_sound)) # Write frames
    morse_file.close()  # Close file


def read_sound(morse_filename, dot_time=130, dash_time=430, space_time=1000, char_space_time=430):  # Read from sound file(.wav)
    frames = []
    buf_frame = []
    w = wave.open(morse_filename, "rb")
    frame_per_ms = w.getframerate()/1000
    # read .wav and create 0,1 array
    for i in range(0, w.getnframes()):

        s = w.readframes(1)
        f = int.from_bytes(s[:2], "big", signed=True)
        buf_frame.append(f)
        if len(buf_frame) == 300:
            if std(buf_frame) > 5000:
                frames.append(1)
            else:
                frames.append(0)
            buf_frame = []
    w.close()
    # get time beeps
    zero_or_one = frames[0]
    num = 0
    time_frame = []
    out = []
    for i in range(0, len(frames)):
        if zero_or_one != frames[i]:
            time_frame.append([num*300/frame_per_ms, zero_or_one])
            zero_or_one = frames[i]
            num = 0
        else:
            num += 1
    time_frame.append([num*300/frame_per_ms, zero_or_one])

    # create array array with morse charts
    print(time_frame)
    char = ""
    for i in time_frame:
        if i[1] == 0:
            if i[0] > space_time:
                out.append(char)
                char = ""
                out.append(" ")
            elif i[0] > char_space_time:
                out.append(char)
                char = ""
        else:
            if i[0] > dash_time:
                char += "-"
            elif i[0] > dot_time:
                char += "."
    out.append(char)
    print(out)

    return out
