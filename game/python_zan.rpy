

label lec_python:
    scene kabinet_komp
    play music zvonok
    show preob at left
    preob "Добрый день, студенты"
    stop music

    preob "Меня зовут Преображенский Максим Владимирович, я ваш преподователь по Python"

    preob "Если вы до этого момента не занимались программированием - это не страшно!"
    preob "Мы начнем обучение с основ, так что проблем ни у кого не будет"
    preob "Начнем нашу лекцию"

    preob "Python - высокоуровневый язык программирования. Он достаточно прост в изучение и отлично подойдет для первого языка программирования"
    preob "Стоит сразу отметить, что в программах важны отступы! Все операторы должны иметь один и тот же отсуп, если только они не входят в другую последовательность действий"
    preob "Может казаться сложно, но это пока что"
    preob """На примере:
    \na = 1
    \nb = 2
    \na = a + b
    \nb = a - b
    \na = a - b
    \nprint a, b"""

    preob "Имеют одинаковое количество отсупов, так как идут сразу друг за другом в работе кода"
    preob """А вот рассмотрим простой оператор выбора
    \nif a < 0:
    \n      s = -1
    \nelif a == 0:
    \n      s = 0
    \nelse:
    \n      s = 1
    """
    preob "Уже заметны отличия в отступах. Потому что тут код будет выполняться только после проверки условии. И если оно соблюдено - выполниться код идущий после него"
    preob "Разберем оператор выбора: есть if, elif и else"
    preob "С if начинается любой оператор выбора. После него идет условие и заканчиваетяс двоеточием "
    preob "Elif же проверяется в случае если условия до него не прошли. После него так же пишутся условия, ставиться двоиточие"
    preob "Else же в отличие от предыдущих ключевых строк не дает нам поставить условия проверки. Код идущий за else будет выполняться в любом случае, если все предыдущие условия не прошли"
    preob "Для вывода данных нам потребуетмя оператор print()"
    preob "В скобочках указывается что именно должно выводиться программой"
    preob "Разберем что такое циклы"
    preob "С помощью циклов можно описать повторяющиеся действия"
    preob "Циклы деляться на несколько типов: выполняя некоторое условие и выполняя код для всех значений последовательности"
    preob """s = "abcdefghijklmnop"
    \nwhile s != "":
    \n      print s
    \n      s = s[1:-1]
        """
    preob "Это первый тип"
    preob """while 1:
    \n      l = f.readline()
    \nif not l:
    \n      break
    \nif len(l) > 5:
    \n      print l,
    \nf.close()
    """
    preob "Это второй тип"

    play music zvonok
    preob "Закончим на этом нашу лекцию"
    stop music
    preob "На семинаре закрепим занния"

    "Перемена перед последней парой была слишокм короткой, что бы ты ее вообще мог заметить"
    play music zvonok
    preob "Ну и быстро приступим к занятию!"
    stop music

    preob "Какое ключевое слово выводит данные на экран?"
    menu otv_7:
        "Что ответить?"

        "Print()":
            fedya "Правильно"

        "Conclusion":
            fedya "Не верно"

    preob "Важны ли отступы в коде?"
    menu otv_8:
        "Что ответить?"

        "Да":
            fedya "Правильно"

        "Нет":
            fedya "Не верно"
    preob "Сколько ключевых слов в условиях?"
    menu otv_9:
        "Что ответить?"

        "Три":
            fedya "Правильно"

        "Два":
            fedya "Тоже верно. Технически elif это соединение else и if"

    preob "Какие виды циклов мы изучили?"
    menu otv_10:
        "Что ответить?"

        "Выполеннеи условия и прохождение по всей последовтаельности":
            fedya "Правильно"

        "Выполнение условий последовтаельности и условий":
            fedya "Ну, можно сказать и так"

    play music zvonok
    preob "Вот и закончилось наше семинарское занятие!"
    stop music        
    preob "До встречи!"

    jump konc

