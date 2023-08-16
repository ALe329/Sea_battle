sea=[]
from functions_for_sea_battle import randomly_place_all_ships,zapros,chek_if_hitts,is_sunk,ship_type,color,hit,are_unsink_ships_left

fleet=randomly_place_all_ships()
print(fleet)
'''Делаем поле'''
print("   " + " ".join([str(x) for x in range(10)]))
for k in range(10):
    sea.append(['.']*10)
for j in range(10):
    print(str(j)+"  " + " ".join(sea[j]))
game_over = True
count_zapros = 0

while game_over:
    count_zapros+=1
    ochki = (1000/count_zapros)**2
    t=zapros()
    if t == 'End of Game':
        print(t)
        game_over=False
    elif t == 'Вы ввели неправильный запрос, необходимо ввести два простых числа через пробел или esc':
        print(t)
        game_over = True
    else:

        # q, w = hit(t[0], t[1], fleet)
        if chek_if_hitts(t[0], t[1], fleet) != True:
            print('Мимо')
            print("   " + " ".join([str(x) for x in range(10)]))
            sea[t[0]][t[1]] = "-"
            for j in range(10):
                print(str(j) + "  " + " ".join(sea[j]))


        elif chek_if_hitts(t[0],t[1],fleet) == True and is_sunk(hit(t[0], t[1], fleet)[1]):
            print(f'Потоплен {ship_type(hit(t[0], t[1], fleet)[1])}')
            print("   " + " ".join([str(x) for x in range(10)]))
            for j in hit(t[0], t[1], fleet)[1][4]:
                sea[j[0]][j[1]] = ship_type(hit(t[0], t[1], fleet)[1])[0]
            for j in range(10):
                print(str(j) + "  " + " ".join(sea[j]))

        elif chek_if_hitts(t[0],t[1],fleet) == True:
            print('Попал')
            print("   " + " ".join([str(x) for x in range(10)]))
            sea[t[0]][t[1]] = "x"
            for j in range(10):
                print(str(j) + "  " + " ".join(sea[j]))

    if are_unsink_ships_left(fleet)==False:
        print(f"Вы выиграли за {count_zapros} ударов и получили {ochki} очков")
        game_over=False