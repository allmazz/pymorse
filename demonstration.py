import pymorze # Подключение библиотеки pymorze

inp = input("Вы хотите прочитать из файла(R) или записать(W)? ") # Пользовательский ввод
if inp == "W": # Если пользователь ввёл "W"
    try: # Обработка исключения, вдрг пользователь ведёт символ, которого нет среди допустимых
        mText = pymorze.to_morse(input('Введите текст для кодировки(русские символы, цифры, "., :; ()\'"-/?!@=" ) : '), pymorze.ruMorseAlphabet) # Получение пользовательского текста, который надо кодировать, и кодировка его в Морзе
    except: # Если пользователь ввёл недопустимый символ
        print("Недопустимый символ")
        exit() # Выход
    pymorze.gen_sound(mText, input("Введите имя выходного фалйа: ")) # Получение имя файла от пользователя, и генерация звукового файла
    print("Готово!")
elif inp == "R": # Если пользователь ввёл "R"
    print(pymorze.from_morse(pymorze.read_sound(input("Введите имя входного фалйа: ")), pymorze.ruMorseAlphabet)) # Получение имя файла от пользователя, чтение звукового файла, и кодировка в текст из морзе
else: # Если пользователь ввёл некоретный ответ(не "W" и не "R")
    print("Прочитать - 'R'; Записать - 'W'")