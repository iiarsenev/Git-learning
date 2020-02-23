#coding: utf-8

import os
import psutil
import sys
import time
import shutil

print("Program13")
print("Привет")
name = input("Имя: ")
print(name, ", добро пожаловать в мир Python 441")
answer = ''
while answer != 'Q':
    answer = input("Поработаем? (Y/N/Q)")
    if answer == 'Y': 
        print(" Молодец бро")
        print("Вот что я могу:")
        print("[1]- Вывести список файлов")
        print("[2]- системная информация")
        print("[3]- Текущее время")
        print("[4]- Дублироване файлов")
        print("[5]- удаление дубликатов")
        

        do = int(input("Выберите действие:-"))
    
    
        if do == 1:
           print(os.listdir())
        elif do == 2:
           print("имя системы:-", os.name)
           print("Логин пользователя", os.getlogin())
           print("Количество процессоров", psutil.cpu_count)
        elif do == 3:
            print(time.asctime())
        elif do == 4:
            print("Дублирование файлов")
            fl = os.listdir()
            i = 0
            while i< len(fl):
                newfile = fl[i] + '.dub'
                shutil.copy(fl[i], newfile)
                i += 1
            print(os.getcwd())
        else:
            print("Допустимые значения -\n -1\n -2\n -3\n -4")

    elif answer == 'N':
	    print("Я был о тебе лучшего мнения.")	
    else:
	    print("Всего доброго")
        