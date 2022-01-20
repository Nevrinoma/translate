from Module import*
eng = []
rus = []
failist_lugemine("eng.txt",eng)
failist_lugemine("rus.txt",rus)
vastus = True
while vastus:
    print("""
    1 >>> Все слова
    2 >>> Перевести
    3 >>> Новое слово
    4 >>> Исправление ошибок
    5 >>> Тест
    6 >>> Выход""")
    vastus = input(">>> ")
    if vastus == "1":
        print(eng)
        print(rus)
        continue
    elif vastus == "2":
        slovo = input("Введите слово для перевода >>> ")
        if slovo not in eng and slovo not in rus:
            print(f"Этого слова {slovo} еще нет в нашем словаре, но вы можете добавить его")
            continue
        else:
            if slovo in eng:
                indeks = eng.index(slovo)
                print(f"{slovo} - {rus[indeks]}")
            elif slovo in rus:
                indeks = rus.index(slovo)
                print(f"{slovo} - {est[indeks]}")
                
    elif vastus == "3":
        print()
    elif vastus == "4":
        print()
    elif vastus == "5":
        print()
    elif vastus == "6":
        break
    else:
        print("Неправильный тип данных!")

