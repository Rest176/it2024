def check_numbers(massive : list) -> bool: # Проверяет состоят ли все элементы массива только из букв
    for element in massive:
        if element.isdigit():
            return True
    return False

def check_human(massive : list) -> bool: # Проверяет являются ли все рост человеческими
    for element in massive:
        element = int(element)
        if element < 50 or element > 250:
            return True
    return False

s = input()
seperated_str = s.split()

if s.count(' ') != len(seperated_str) - 1 or s == '' or len(seperated_str) % 2 != 0: # Проверяют если ввод - пустая строка, много пробелов или неправильность строки
    print('ERROR')
else:
    d = {seperated_str[i + 1] : seperated_str[i] for i in range(0, len(seperated_str), 2)} # Преобразует массив в строки вида: рост:имя
    if check_numbers(d.values()) or not check_numbers(d.keys()) or check_human(d.keys()): # Проверяет человеческий ли рост, есть ли среди имен числа или среди чисел имена
        print('ERROR')
    else:
        sorted_list_of_weights = sorted(d.keys(), reverse=True) # сортирует рост людей
        print(*[f'{d[i]} {i}' for i in sorted_list_of_weights], sep='\n') # выводит ответ вида: имя рост, в порядке убывания роста