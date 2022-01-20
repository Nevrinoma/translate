import os
from gtts import gTTS

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel;slow=False).save("heli.mp3")
    os.system("heli.mp3")





def failist_lugemine(f:str,l:list)->list:
    """Информация из файла f в список l
    :param str f: файл с информацией
    :param list l: список, в который добавляется информация
    :rtype: list
    """
    fail = open(f,"r",encoding="utf-8-sig")
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def failisse_salvestamine(f:str,l:list):
    """Сохраняем списки в файл
    :param str f: файл, куда сохраняем
    :param list l: список, в который добавляется информация
    """
    fail = open(f,"w")
    for el in l:
        fail.write(el + "\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Сохранение слова или фразы (строки) в файл
    :param str f: файл, куда сохраняем
    :param str rida: слово, которое нужно сохранить
    """
    fail = open(f,"a")
    fail.write(rida + "\n")
    fail.close()

def uus_sona(f:str,rida:str)->list:
    """
    :param str f:
    :param str rida:
    :rtype: list
    """
    l = []
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida + "\n")
    l = failist_lugemine(f)
    return l

def translate(slovo:str)->str:
    """
    :param str slovo:
    :rtype:
    """
