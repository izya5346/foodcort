from collections import Counter
from pprint import pprint
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

        if len(i) <= 4 and max(i) <= 3:
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
            elif n < 13:
                try:
                    if dict(Counter(i))[3] + dict(Counter(i))[2] >= mn:
                        mn = dict(Counter(i))[3] + dict(Counter(i))[2]
                        tmp = i.copy()
                except:
                    pass
    return sorted(tmp, reverse = True)

def combine_menu(ls):
    comb = combine(len(ls))
    new = []
    cnt = 0
    for c in comb:
        tmp = []
        for i in range(cnt, cnt + c):
            tmp.append(ls[i])
        cnt+= c
        new.append(tmp)
    return new


def generate_keyboard(ls):
    new = []
    for i in ls:
        try:
            new.append({'label': i['name'], 'type': 'text'})
        except KeyError:
            new.append({'label': i['name'], 'type': 'text'})
    new.append({'label': 'Назад', 'type': 'text'})
    return combine_menu(new)
# pprint(combine_menu([{'label': f'btn{i}', 'type': 'text'} for i in range(11)]))