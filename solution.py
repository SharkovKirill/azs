"""
Developers: Vladimir Ermolenko:


"""
import random

max_all_places = {}
types_of_gaz = {}
with open('azs.txt', encoding='utf-8') as azs:
    lst_azs = azs.readlines()

for num in range(len(lst_azs)):
    x = lst_azs[num].split()
    max_all_places[num + 1] = int(x[1])

    for i in range(2, len(x)):
        if x[i] not in types_of_gaz.keys():
            types_of_gaz[x[i]] = [num + 1]
        elif x[i] in types_of_gaz.keys():
            types_of_gaz.get(x[i]).append(num + 1)

current_places = {}
for i in range(len(max_all_places)):
    current_places[i + 1] = 0

with open('input.txt', encoding='utf-8') as clients:
    lst_clients = clients.readlines()

# print(current_places)
# print(max_all_places)
# print(types_of_gaz)
# print(list(types_of_gaz))
future_leaving = []
aazz = {}
cost = {}
allcost = 0
cost['АИ-92'] = 43.54
cost['АИ-80'] = 46.72
cost['АИ-95'] = 44.55
cost['АИ-98'] = 49.66


def table(current_places, max_all_places, types_of_gaz):
    for i in range(1, len(current_places) + 1):
        az = ''
        for key in types_of_gaz.keys():
            if i in types_of_gaz.get(key):
                az = az + ' ' + key
        print('Автомат №{}  максимальная очередь: {} Марки бензина: {} ->'.format(i, max_all_places.get(i), az),
              '*' * list(current_places.values())[i - 1], sep='')
    print()


k = 0
left_azs = 0
for client in range(len(lst_clients)):
    cl = lst_clients[client].split()
    if k == 0:
        time = int(cl[0][1:3]) * 60 + int(cl[0][4:6])
        k = 1
    else:
        time = int(cl[0][0:2]) * 60 + int(cl[0][3:5])

    if len(future_leaving) > 0:
        try:
            while future_leaving[0][0] <= time:
                ti = future_leaving[0][0] // 60
                tii = future_leaving[0][1] // 60
                current_places[future_leaving[0][5]] -= 1

                if ti < 10:
                    if (future_leaving[0][0] - ti * 60) < 10:
                        if tii < 10:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), str(future_leaving[0][1] - tii * 60))
                        else:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), str(future_leaving[0][1] - tii * 60))
                    else:
                        if tii < 10:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), str(future_leaving[0][1] - tii * 60))
                        else:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format('0' + str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), str(future_leaving[0][1] - tii * 60))

                else:
                    if (future_leaving[0][0] - ti * 60) < 10:
                        if tii < 10:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), str(future_leaving[0][1] - tii * 60))
                        else:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), '0' + str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), str(future_leaving[0][1] - tii * 60))
                    else:
                        if tii < 10:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   '0' + str(tii), str(future_leaving[0][1] - tii * 60))
                        else:
                            if (future_leaving[0][1] - tii * 60) < 10:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), '0' + str(future_leaving[0][1] - tii * 60))
                            else:
                                fp = 'В {}:{} клиент {}:{}'.format(str(ti), str(future_leaving[0][0] - ti * 60),
                                                                   str(tii), str(future_leaving[0][1] - tii * 60))

                print(fp + ' {} {} {} заправил свой автомобиль и покинул азс.'.format(future_leaving[0][2],
                                                                                      str(future_leaving[0][3]),
                                                                                      str(future_leaving[0][4])))

                table(current_places, max_all_places, types_of_gaz)
                future_leaving.pop(0)

        except:
            pass


    # для проверки прохождения for на первый раз
    mi = -1
    changed_azs = -1
    for i in range(len(types_of_gaz.get(cl[2]))):
        if current_places.get(types_of_gaz.get(cl[2])[i]) < max_all_places.get(types_of_gaz.get(cl[2])[i]):
            if mi == -1:

                mi = current_places.get(types_of_gaz.get(cl[2])[i])
                changed_azs = types_of_gaz.get(cl[2])[i]
            else:
                if current_places.get(types_of_gaz.get(cl[2])[i]) < mi:
                    mi = current_places.get(types_of_gaz.get(cl[2])[i])
                    changed_azs = types_of_gaz.get(cl[2])[i]

    if changed_azs > 0:
        current_places[changed_azs] += 1
    if changed_azs == -1:
        left_azs += 1
        print('Не нашел места В {}:{} '.format(str(time // 60), str(time - (time // 60) * 60), cl[2]),
              current_places.values())
        table(current_places, max_all_places, types_of_gaz)
        continue
    refill_time = int((int(cl[1]) - 1) // 10) + 1 + int(random.randint(-1, 1))
    if refill_time == 0:
        refill_time = 1
    future_time = 0
    for f in range(len(future_leaving)):
        if future_leaving[len(future_leaving) - f - 1][5] == changed_azs:
            future_time = future_leaving[len(future_leaving) - f - 1][0] + refill_time
            break
    if future_time == 0:
        future_time = time + refill_time

    if (time // 60) < 10:
        if time - ((time // 60) * 60) < 10:
            fp1 = 'В {}:{} новый клиент: {}:{}'.format('0' + str(time // 60), '0' + str(time - (time // 60) * 60),
                                                       '0' + str(time // 60), '0' + str(time - (time // 60) * 60))
        else:
            fp1 = 'В {}:{} новый клиент: {}:{}'.format('0' + str(time // 60), str(time - (time // 60) * 60),
                                                       '0' + str(time // 60), str(time - (time // 60) * 60))
    else:
        if time - ((time // 60) * 60) < 10:
            fp1 = 'В {}:{} новый клиент: {}:{}'.format(str(time // 60), '0' + str(time - (time // 60) * 60),
                                                       str(time // 60), '0' + str(time - (time // 60) * 60))
        else:
            fp1 = 'В {}:{} новый клиент: {}:{}'.format(str(time // 60), str(time - (time // 60) * 60),
                                                       str(time // 60), str(time - (time // 60) * 60))

    print(fp1 + ' встал в очередь к автомату №{}'.format(str(changed_azs)))

    table(current_places, max_all_places, types_of_gaz)
    if cl[2] not in aazz.keys():
        aazz[cl[2]] = int(cl[1])
    elif cl[2] in aazz.keys():
        aazz[cl[2]] += int(cl[1])

    if cl[2] == 'АИ-92':
        allcost += int(cl[1]) * cost.get(cl[2])
    if cl[2] == 'АИ-80':
        allcost += int(cl[1]) * cost.get(cl[2])
    if cl[2] == 'АИ-95':
        allcost += int(cl[1]) * cost.get(cl[2])
    if cl[2] == 'АИ-98':
        allcost += int(cl[1]) * cost.get(cl[2])

    future_leaving.append([future_time, time, cl[2], int(cl[1]), refill_time, changed_azs])


print('Количество литров АИ-80, проданного за сутки: ', aazz.get('АИ-80'), '\n'
                                                                           'Количество литров АИ-92, проданного за '
                                                                           'сутки: ',
      aazz.get('АИ-92'), '\n'
                         'Количество литров АИ-98, проданного за сутки: ', aazz.get('АИ-98'), '\n'
                                                                                              'Количество литров АИ-95,'
                                                                                              ' проданного за сутки: ',
      aazz.get('АИ-95'), '\n')
print('Общая сумма продаж за сутки: ', int(allcost))
print('Количество машин, покинувших АЗС: ', left_azs)
# Вся необходимая информация о клиенте добавляется(удаляется) через future_leaving,
# Время считается в минутах начиная с 00:00
