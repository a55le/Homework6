#Задание 1
string = 'AAABBB'
string = list(string)
RLE = ''
while len(string) > 0:
    RLE_coeff = 1
    item = string.pop(0)
    while len(string) > 0:
        if item == string[0]:
            string.pop(0)
            RLE_coeff += 1
        else:
            break
    RLE = RLE + f'{item}*{RLE_coeff}'
print(RLE)
#Задание 2
plus_minus = ['+', '-']
print('Добро пожаловать в игру Крестики-Нолики. Вместо крестиков на панели будут отображаться еденички. Первыми ходят крестики')
import re
end = False
table_element = '0'
repeated_elements = []
nule_or_one_numerate = 1
nule_or_one = ''
A1 = ' '
A2 = ' '
A3 = ' '
B1 = ' '
B2 = ' '
B3 = ' '
C1 = ' '
C2 = ' '
C3 = ' '
ones = '111'
zeroes = '000'
while end is not True:
    table = f'      |      |      \n   {A1}  |   {B1}  |   {C1}   \n      |      |     \n‾‾‾‾‾‾|‾‾‾‾‾‾|‾‾‾‾‾‾‾\n   {A2}  |   {B2}  |   {C2}   \n      |      |      \n‾‾‾‾‾‾|‾‾‾‾‾‾|‾‾‾‾‾‾‾\n   {A3}  |   {B3}  |   {C3}  \n      |      |      '
    print(table)
    input_element = input('Введите номер ячейки\n')
    if re.match(r'^[A-C]?[1-3]?$', input_element) and input_element not in repeated_elements :
        repeated_elements.append(input_element)
        if nule_or_one_numerate % 2 == 0:
            nule_or_one = '0'
        else:
            nule_or_one = '1'
        if input_element == 'A1':
            A1 = nule_or_one
        if input_element == 'A2':
            A2 = nule_or_one
        if input_element == 'A3':
            A3 = nule_or_one
        if input_element == 'B1':
            B1 = nule_or_one
        if input_element == 'B2':
            B2 = nule_or_one
        if input_element == 'B3':
            B3 = nule_or_one
        if input_element == 'C1':
            C1 = nule_or_one
        if input_element == 'C2':
            C2 = nule_or_one
        if input_element == 'C3':
            C3 = nule_or_one
        nule_or_one_numerate += 1
    else:
        print('Ошибка')
    if (A1 + B1 + C1) == '111' or (A1 + B1 + C1) == '000':
        print(A1 + B1 + C1)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (A2 + B2 + C2) == '111' or (A2 + B2 + C2) == '000':
        print(A2 + B2 + C2)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (A3 + B3 + C3) == '111' or (A3 + B3 + C3) == '000':
        print(A3 + B3 + C3)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (A1 + A2 + A3) == '111' or (A1 + A2 + C3) == '000':
        print(A1 + B2 + C3)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (A3 + B2 + C1) == '111' or (A3 + B2 + C1) == '000':
        print(A3 + B2 + C1)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (A1 + A2 + A3) == '111' or (A1 + A2 + A3) == '000':
        print(A1 + A2 + A3)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (B1 + B2 + B3) == '111' or (B1 + B2 + B3) == '000':
        print(B1 + B2 + B3)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')
    if (C1 + C2 + C3) == '111' or (C1 + C2 + C3) == '000':
        print(C1 + C2 + C3)
        if nule_or_one == '0':
            print('Победили нолики')
        else:
            print('Победили крестики')