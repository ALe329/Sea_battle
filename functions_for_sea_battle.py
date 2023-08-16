'''Определяем тип корабля'''
def ship_type(ship):
    '''Первый вариант через словарь'''
    # t= {1:"Подводная лодка",2:"Эсминец",3:"Крейсер",4:"Линкор"}
    # print(t[sheep[3]])
    '''Второй вариант через if'''
    # if sheep[3]==1:
    #     print("Подводная лодка")
    # elif sheep[3]==2:
    #     print("Эсминец")
    # elif sheep[3] == 3:
    #     print("Крейсер")
    # elif sheep[3] == 4:
    #     print("Линкор")
    '''Третий вариант через список'''
    names_ship=["Подводная лодка","Эсминец","Крейсер","Линкор"]
    return (names_ship[ship[3]-1])

'''определяем потоплен корабль или нет'''
def is_sunk(ship):
    '''Первый вариант'''
    # if sheep[3]==len(sheep[4]):
    #    return True
    # else:
    #     return False
    '''Второй вариант'''
    # print (True if sheep[3]==len(sheep[4]) else False)
    '''Третий вариант'''
    return ship[3]==len(ship[4])
# print(is_sunk(ship_3))

def is_open_sea(x, y, fleet):
    koord = []
    koord_sheep = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            koord.append([i, j])
    for ship in fleet:
        if ship[2] == True:
            for n in range(ship[3]):
                koord_sheep.append([ship[0], ship[1] + n])
        else:
            for h in range(ship[3]):
                koord_sheep.append([ship[0] + h, ship[1]])
    false_true = []
    for c in koord_sheep:
        if c in koord:
            false_true.append(False)
        else:
            false_true.append(True)
    if False in false_true:
        return False
    else:
        return True

'''Проверяет можно ли расположить корабль, нет ли рядом других кораблей '''
def ok_to_place_ship_at(ship, fleet):
    true_false = []
    for i in range(ship[3]):
        if ship[2]:
            true_false.append(is_open_sea(ship[0], ship[1]+i, fleet))
        else:
            true_false.append(is_open_sea(ship[0]+i, ship[1], fleet))

    if False in true_false:
        return False
    else:
        return True

''' Функция возвращает флот с новым кораблем если можно его добавить в существующий флот'''
def place_ship_at(ship, fleet):
    if ok_to_place_ship_at(ship, fleet) == True:
        fleet.append(ship)
    return fleet

def randomly_place_all_ships():
    fleet=[]
    import random
    from random import randrange
    while len(fleet)<1:
        place_ship_at((randrange(0,6),randrange(0,6), random.choice([False, True]),4,set()),fleet)
    while len(fleet)<3:
        place_ship_at((randrange(0, 7), randrange(0, 7), random.choice([False, True]), 3, set()), fleet)
    while len(fleet)<6:
        place_ship_at((randrange(0, 8), randrange(0, 8), random.choice([False, True]), 2, set()), fleet)
    while len(fleet)<10:
        place_ship_at((randrange(0, 9), randrange(0, 9), random.choice([False, True]), 1, set()), fleet)
    return fleet

'''Функция говорит было ли попадание в корабль'''
def chek_if_hitts(x,y,fleet):
    list_of_ships_coord=[]
    for ship in fleet:
        if ship[2]:
            for i in range(ship[3]):
                list_of_ships_coord.append([ship[0], ship[1]+i])
        else:
            for j in range(ship[3]):
                list_of_ships_coord.append([ship[0]+j, ship[1]])
    koord=[x,y]
    if koord in list_of_ships_coord:
        return True
    else:
        return False
'''Функция которая если корабль подбит-выдает флот и этот корабль'''
def hit(x,y,fleet):
    koord_ships = []
    x_y=[x,y]
    for ship in fleet:
        if ship[2]:
            for i in range(ship[3]):
                koord_ships.append([ship[0], ship[1] + i])
            if x_y in koord_ships:
                ship[4].add((x,y))
                # ship[4].add(y)
                return fleet, ship
        else:
            for j in range(ship[3]):
                koord_ships.append([ship[0] + j, ship[1]])
            if x_y in koord_ships:
                ship[4].add((x,y))
                # ship[4].add(y)
                return fleet, ship

'''Функция которая принимает флот и возвращает True если есть еще непотопленные корабли'''
def are_unsink_ships_left(fleet):
    tr_fls=[]
    for ship in fleet:
        if len(ship[4])==ship[3]:
            tr_fls.append(1)
        else:
            tr_fls.append(0)
    if 0 in tr_fls:
        return True
    else:
        return False

def zapros():
    a = input("Введите две цифры через пробел или esc(для выхода из игры): ").split()
    if a[0] == 'esc':
        return 'End of Game'
    elif len(a) == 2 and a[0].isdigit() and a[1].isdigit() and 0 <= int(a[0]) < 10 and 0 <= int(a[1]) <10:
        a =(list(map(int,a)))
        return a
    else:
        return "Вы ввели неправильный запрос, необходимо ввести два простых числа через пробел или esc"

def color(ship):

    symbol=ship_type(ship)[0]
    if is_sunk(ship):
        return symbol

