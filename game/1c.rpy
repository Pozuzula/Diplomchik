init:        
    $ les1 = 0              # Пермееные прохождения лекций
    $ les2 = 0
    $ les3 = 0
    $ les4 = 0
    $ les5 = 0
    $ les = les1 + les2 + les3 + les4 + les5
    $ task1 = 0              # Пермееные прохождения тестов
    $ task2= 0
    $ task3 = 0
    $ task4 = 0
    $ task5 = 0
    $ task = task1 + task2 + task3 + task4 + task5
    $ prov = 0
    $ popitka_1 = 0
    $ popitka_2 = 0
    $ popitka_3 = 0
    $ popitka_4 = 0
    $ popitka_5 = 0

    



label lekciy:
    scene kabinet_komp
    show stryp at left with dissolve
    show screen friendmeter_stryp
    stryp "Добро пожаловать!"
    stryp "Меня зовут Стряпунина Нэли Ильинична, я преподователь 1С"
    stryp "Давайте начнем занятие!"
    stryp "Первая лекция курса 1С"
    stryp "Для начала разберемся что такое 1С. Это фирма, разработавшая 1С:Предприятие. Основана она была в 1991 году Борисом и Сергеем Нуралиевым."
    stryp "На данный момент она занимает лидирующие позиции в российском софтверном бизнесе благодаря своему суперпродукту 1С:Предприятие"
    stryp "Система 1С:Предприятие предоставляет в распоряжение разработчику широкий набор объектов:  справочники, документы, регистры и т.д., и инструментов: встроенный язык программирования, механизм запросов, различные визуальные редакторы и конструкторы. "
    stryp "Сама по себе 1С:Предприятие — это специализированная объектно-ориентированная система управления базами данных (СУБД), предназначенная для автоматизации деятельности предприятия."
    stryp "Рассмотрим 1С:Предприятие подробнее. Как уже говорилось ранее, это система управления базами данных. К ним относятся Microsoft SQL Server, PostgreSQL, Oracle Database, IBM DB2 и файловой базой данных. "
    stryp "Состоит «1С:Предприятие» из двух частей: технологической платформы и конфигурации. "
    stryp "Технологическая платформа – это и среда разработки, и среда выполнения. Она содержит все инструменты разработки, а так же осуществляет работу уже готовых продуктов. Разработкой платформы занимается сама компания «1С»."
    stryp "Конфигурация – это прикладные решения, которые работать сами по себе не смогут, для этого им необходима платформа. Фирмой 1С были разработаны типовые конфигурации: бухгалтерия, кадровый учет, управление торговлей и т.д.."
    play music zvonok
    
    stryp "На этом закончим нашу лекцию"
    stryp "На втором нашем занятии я дам вам пройти небольшой тест по лекции. На оценки это не повляет!"
    stop music
    hide stryp
    hide screen friendmeter_stryp

    "Началась короткая перемена"
    menu ne_posl:
        "Что делать?"

        "Пойти домой" if proguli==0:
            "Я и так долго сидел. Пора отдыхать"
            $ proguli =+1
            jump konec
        "Досидеть до конца":
            "Не падать духом. Не отходить ни на шаг!"
            jump para_4


    

label lecture_1c: 
    scene kabinet_komp
    menu list_lecture:
        "Начать лекцию"

        "Первая":
            jump professional_1c_lectures_one

        #"Вторая":
        #    jump professional_1c_lectures_two

        #"Третья":
        #    jump professional_1c_training_start

        #"Четвертая":
        #    jump professional_1c_training_start

        #"Пятая":
        #   jump professional_1c_training_start


label tasks_1c:
    scene kabinet_komp
    
    menu list_tasks:
        "Начать тест"

        "Первый":
            jump para_4

        #"Второй":
        #    jump professional_1c_task_two

        #"Третий":
        #    jump professional_1c_training_start

        #"Четвертый":
        #    jump professional_1c_training_start

        #"Экзамен":
        #   jump professional_1c_training_start

label menu_1c:
    scene kabinet_komp
    menu menu_for_1c:
        "Что дальше?"

        "Лекции":
            jump lecture_1c

        "Тесты":
            jump tasks_1c
                
        "Прогресс курса":
            jump  professional_1c_progress

        "Результаты тестов":
            jump res





label para_4:
    scene kabinet_komp
    show stryp at left with dissolve
    show screen friendmeter_stryp
    stryp "Рада, что хоть кто-то остался с нами"
    stryp "Давайте тогда начнем тест. Чем быстрее приступим, тем быстрее закончим!"
    hide stryp
    hide screen friendmeter_stryp
    if popitka_1 <= 2:

        if task1 > 0:
            $ prov = task1
            $ task1 = 0
        else:
            menu q1_1:
                "Это твоя [popitka_1] попытка решить тест"
                "В каком году была основана компания 1С?"

                "1991":
                    $ task1 += 1
                    jump q1_2
                
                "1990":
                    jump q1_2

                "1989":
                    jump q1_2

                "2000":
                    jump q1_2

            menu q1_2:
                "В чем преимущество компании 1С над конкурентами?"

                "В хорошей логистике":
                    jump q1_3
                
                "Монополизации рынка":
                    jump q1_3
                
                "Агресивной рекламе":
                    jump q1_3

                "В суперпродукте 1С:Предприятие":
                    $ task1 += 1
                    jump q1_3

            menu q1_3:
                "В чем заключается суть работы 1С:Предприятия?"

                "В управление баз данных":
                    $ task1 += 1
                    jump q1_4

                "В создание красивых интерфейсов":
                    jump q1_4

                "Страдании":
                    jump q1_4

                "Оптимизации работы компьютера":
                    jump q1_4

            menu q1_4:
                "Из каких частей состоит 1С:Предприятие?"


                "2":
                    jump q1_5

                
                "3":
                    $ task1 += 1
                    jump q1_5
                

                "4":
                    jump q1_5

                "1":
                    jump q1_5

            menu q1_5:
                "Из чего состоит 1С:Предпритие?"

                "Технологическая платформа, конфигуратор":
                    $ task1 += 1
                    jump q1_6
                
                "Конфигуратор, интерпретатор":
                    jump q1_6
                
                "Техническая платформа, коммутатор":
                    jump q1_6
                
                "Компьютер, монитор, мышь, по":
                    jump q1_6

            menu q1_6:
                "Что еще включает в себя 1с:Предприятие?"

                "База данных":
                    $ task1 += 1
                    jump q1_7
                
                "Конфигурация":
                    jump q1_7

                "Компетенция":
                    jump q1_7

                "Программирование":
                    jump q1_7

            menu q1_7:
                "Что представляет собой технологическая платофрма?"

                "Среда разработки и выполнения":
                    $ task1 += 1
                    jump q1_8
                
                "Среда разработки и отлаживания":
                    jump q1_8

                "Среда проработки и выполнения":
                    jump q1_8

                "Среда отработки и выслеживания":
                    jump q1_8

            menu q1_8:
                "Что предсталвяет собой конфигурация?"

                "Прикладное решение, которое не работает без платформы":
                    $ task1 += 1
                    jump q1_9
                
                "Прикладное решение, которое работает где угодно":
                    jump q1_9
                
                "Подколодное решение, для отработки ":
                    jump q1_9

                "Прикольное решение, для увеселенья":
                    jump q1_9

            menu q1_9:
                "Кто занимается разработкой платформы?"

                "Фирма 1С":
                    $ task1 += 1
                    jump q1_10
                
                "Программисты":
                    jump q1_10

                "Фирма ПервыйБит":
                    jump q1_10

                "Разработчики":
                    jump q1_10

            menu q1_10:
                "Какие есть типовые конфигурации?"

                "Бухгалтерия, Кадровый учет, Управление торгами":
                    $ task1 += 1
                    jump bals
                    
                
                "Подсчет, Учет, Отчет":
                    jump bals

                "Вычет, Бухгалтериия, Управление":
                    jump bals

                "Бухгалтерия, Учет, Управление":
                    jump bals

                    

    else:
        jump ban


label bals:
    if task1 > prov:
        jump end_task1
                    
    elif task1 < prov:
        $ task1 = prov
        jump end_task1
    else: 
        jump end_task1

label ends_tasks_1c:
    scene kabinet_komp
    menu end_task1:
        "Первый тест пройден на [task1]"

        "Перепройти тест (сохранится лучшая попытка)":  
            $ popitka_1 += 1
            jump para_4

        "Пойти домой":
            jump konc
        
label ban:
    scene kabinet_komp
    "Вы уже два раза проходили этот тест"
    "Возвращаемся обратно в меню"
    jump menu_1c


label res:
    scene kabinet_komp
    "Результаты пройденных тестов:"
    "Первый тест пройден на [task1]"
    if task1 >= 7:
        $ zn +=5
    elif task1 >=5 and <7:
        $ zn +=3
    else:
        jump konc
