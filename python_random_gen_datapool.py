from random import randint
import os


os.system(r'nul>c:/Users/admin/Documents/Git/random_datapool/temp/out_datapool.txt') #Удаление значений в файле

path = 'c:/Users/admin/Documents/Git/random_datapool/temp/out_datapool.txt'
 
out_file = open(path,'a')

process = input("Какие значения генерировать: \n1. числовой: 1000-9999(написать 1)\n2. дата: YYYY-MM-DD(написать 2)\n3. дата: DD-MM-YYYY(написать 3)\nНомер процесса: ")
valueRand = input("\nСколько значений генирировать: ")


class Switch:
    def __init__(self, value):
        self.value = value

    def case(self, value, code):
        if self.value == value:
            code()
        return self

#Маска (числовой: ХХХХ)
def process_1(params):
    for i in range(0, int(params)):
        out_file.write(f'{randint(1000, 9999)}')
        out_file.write("\n")

#Маска (дата: YYYY-MM-DD)
def process_2(params):
    for i in range(0, int(params)):
        out_file.write(f'{randint(1900, 2020)}')
        out_file.write("-")
        out_file.write(f'{randint(1, 12)}'.zfill(2))
        out_file.write("-")
        out_file.write(f'{randint(1, 28)}'.zfill(2))
        out_file.write("\n")

#Маска (дата: DD-MM-YYYY)
def process_3(params):
    for i in range(0, int(params)):
        out_file.write(f'{randint(1, 28)}'.zfill(2))
        out_file.write("-")
        out_file.write(f'{randint(1, 12)}'.zfill(2))
        out_file.write("-")
        out_file.write(f'{randint(1900, 2020)}')
        out_file.write("\n")


Switch(int(process)) \
    .case(1, lambda: process_1(valueRand)) \
    .case(2, lambda: process_2(valueRand)) \
    .case(3, lambda: process_3(valueRand))


out_file.close()    #Закрытие файла