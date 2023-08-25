lst_mro = [# список введённых строк
    'A', 'B : A', 'C : A', 'D : B C', 'E : D', 'F : D','G : F', 'X', 'Y : X A',  'Z : X', 'V : Z Y', 'W : V',
]
lst_q = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]
n = int(input())
lst_in = []
lst_qq = []
for i in range(n):
    lst_in.append(input())
q = int(input())
for i in range(q):
    lst_qq.append(input())
def split_and_insert(element):
    items = element.split(':')  # Разделение элемента на две части
    prefix = items[0]  # Часть элемента перед символом ":"
    suffix = items[1].strip()  # Часть элемента после символа ":", очищенная от лишних пробелов
    # Создание новых элементов списка
    new_elements = [f"{prefix}: {item}" for item in suffix.split()]
    return new_elements
def check(lst_mro, lst_q):
    ans = False
    query = lst_q.split(" ")
    j = 0
    while j < len(lst_mro):
        child = lst_mro[j].split(" : ")[0]
        if (query[0] == query[1] and (query[0] in [i[0] for i in lst_mro] or query[0] in [i[-1] for i in lst_mro])):
            return True
        if query[1] == child and len(lst_mro[j]) > 1:
            query[1] = lst_mro[j][-1]
            if j != lst_mro.index(lst_mro[-1]) and child[0] == lst_mro[j + 1][0]:
                pos = lst_mro[j + 1].rpartition(" ")
                ans = check(lst_mro, query[0] + ' ' + pos[2])
            j = 0
        j = j + 1
    if ans:
        return True
    return ans
def graph(lst_mro, lst_q):
    for i in lst_mro:
        if i.count(" ") > 2:
            pos = split_and_insert(i)
            for j in pos:
                lst_mro.insert(lst_mro.index(i),  j)
            lst_mro.remove(i)
    for i in lst_q:
        if check(lst_mro, i):
            print("Yes")
        else:
            print("No")

graph(lst_in, lst_qq)





