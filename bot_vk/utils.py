from collections import Counter
from pprint import pprint
from config import *
def break_into_terms(n, k = None):
    if k is None:
        k = n

    if n == 0:
        return []

    result = []
    if n <= k:
        result.append([n])
    for i in range(1, 1+min(n, k)):
        for l in break_into_terms(n-i, i):
            result.append(l + [i])

    return result
def combine(n):
    tmp = []
    mn = 0
    for i in break_into_terms(n):

        if len(i) <= 6 and max(i) <= 3:
            if n < 4:
                try:
                    if dict(Counter(i))[1] >= mn:
                        mn = dict(Counter(i))[1]
                        tmp = i.copy()
                except:
                    pass
            elif n < 9:
                try:
                    if dict(Counter(i))[2] >= mn:
                        mn = dict(Counter(i))[2]
                        tmp = i.copy()
                except:
                    pass
            else:
                try:
                    if dict(Counter(i))[3] + dict(Counter(i))[2] >= mn:
                        mn = dict(Counter(i))[3] + dict(Counter(i))[2]
                        tmp = i.copy()
                except:
                    pass
    return sorted(tmp, reverse = True)

def combine_menu(ls, command:str):
    comb = combine(len(ls))
    keyboard = Keyboard(one_time = True, inline = False)
    cnt = 0
    for c in comb:
        keyboard.row()
        for i in range(cnt, cnt + c):
            match command:
                case 'get_restaurants':
                    keyboard.add(Text(label = ls[i]['name'], payload = {'command': command, 'id': ls[i]['restaurant_id']}))
                case _:
                    keyboard.add(Text(label = ls[i]['name'], payload = {'command': command, 'id': ls[i]['id']}))
        cnt+= c
    match command:
        case 'get_cities':
            ...
        case 'get_tags':    
            keyboard.row()
            keyboard.add(Text(label = 'Любую', payload = {'command': 'get_tags', 'id': ''}))
            keyboard.add(Text(label = 'Назад', payload = {'command': 'back', 'to': 'get_cities'}))
        case 'get_restaurants':
            keyboard.row()
            keyboard.add(Text(label = 'Назад', payload = {'command': 'back', 'to': 'get_tags'}))
    return keyboard


generate_keyboard = combine_menu
# pprint(combine_menu([{'label': f'btn{i}', 'type': 'text'} for i in range(11)]))