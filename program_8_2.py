def check_numbers(massive : list) -> bool:
    for element in massive:
        if element.isdigit():
            return True
    return False

def check_human(massive : list) -> bool:
    for element in massive:
        element = int(element)
        if element < 50 or element > 250:
            return True
    return False

s = input()
seperated_str = s.split()

if s.count(' ') != len(seperated_str) - 1 or s == '':
    print('ERROR')
else:
    d = {seperated_str[i + 1] : seperated_str[i] for i in range(0, len(seperated_str), 2)}
    if check_numbers(d.values()) or check_numbers(d.keys()):
        print('ERROR')
    else:
        sorted_list_of_weights = sorted(d.keys(), reverse=True)
        print(*[f'{d[i]} {i}' for i in sorted_list_of_weights], sep='\n')