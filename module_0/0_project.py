import numpy as np

begin_def = 1
end_def = 100

def game_core_v2(number):
    #чтобы не переписывать все значения в программе при изменении диапазона загаданного числа (для теста)
    #задаем диапозон числел (отрезок) из которых будет загадываться рандомное число
    #сначала находим середину диапозона из которорого нужно угадывать (точка по середине отрезка)
    #в зависимости от того больше или меньше загаданное число относительно этой точки продолжаем поиск в соответвующей половине диапозона
    count = 1
    begin = begin_def #задаем исходные значения
    end = end_def
    lookup = [x for x in range(begin, end+1)] #интервал в котором после каждой попытки будем искать середину
    predict = len(lookup)//2 #ищем середина отрезка

    while number != predict != begin != end:
        #если загаданное число = началу, найденной середине или концу отрезка - значит угадали и выходим из цикла
        count += 1
        if number > predict:
            begin = predict
        elif number < predict:
            end = predict
            # если предполагаемое число больше начала отрезка, то отрезок для поиска уменьшаем (предполагаемое число становится началом). Аналогично в обратную сторону
        #в итоге остается 2 соседних числа, которые являются началом и концом отрезка соответвенно
        elif end - begin == 1:
            #если последнее
            if number == end:
                break
            else:
                break
        predict = (begin + end) // 2

    return (count)  # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(begin_def, end_def+1, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)
score_game(game_core_v2)
