init python:
    proguli = 0
    pr = 0
    zn = 0
    para = 0

#gg ""

label ycheba:
    
    scene vuz_menu
    
    gg "Вот и настала пора моей учебы"
    gg "Первая пара уже скоро начаться"
    gg "Но как-то я не очень хочу идти на русский"

    menu idti_na_pary_1:
        "Идти на пару?"

        "Да":
            gg "Конечно же мне нужно идти на занятие!"
            gg "Нельзя просто взять и пропустить пару!"
            jump para_1

        "Нет":
            $ proguli =+1
            "Не так страшно, если не пойду сейчас"
            "В конце концов можно одну пару можно и пропустить"
            jump progul_1


    
    
label para_1:
    
    gg "Нужно поспешить на занятие, пока я не опоздал!"
    play music zvonok
    

    scene kabinet
    
    menu izvineniya:
        "Вы опоздали на пару. Извиниться и войти?"

        "Извиниться":
            show prepod_dva at left with dissolve
            show screen friendmeter_prep_dva
            $ fr_prep_dva += 10
            prepod_dva "Ничего страшного. Заходи и садись"

        "Просто зайти внутрь":
            show prepod_dva at left with dissolve
            show screen friendmeter_prep_dva
            $ fr_prep_dva -= 10
            prepod_dva "Молодой человек, когда опаздываете на занятия хотя бы извиняйтесь при входе"
            prepod_dva "Садитесь поближе, мы начинаем занятие"
    hide prepod_dva at left with dissolve
    hide screen friendmeter_prep_dva        
    stop music
    menu pr:
        "Пропустить текст лекции?"
        "Да":
            $ pr +=1
        
        "Нет":
            $ pr = 0

    

    if pr > 0:
        scene blek
        "Сев за парту твои глаза закрылись и ты уснул"
        
    else:
        show prepod_dva at left with dissolve
        show screen friendmeter_prep_dva
        $ zn =+1    
        prepod_dva "Меня зовут Лариса Анатольевна, я учитель русского языка"
        prepod_dva "Начнем нашу первую лекцию. РЕЧЕВЫЕ КОММУНИКАЦИИ"
        prepod_dva "Коммуникация (лат. communico – делаю общим) – в широком смысле –
        обмен информацией между индивидами через посредство общей системы
        символов."
        prepod_dva " Коммуникация может осуществляться вербальными и
        невербальными средствами."
        prepod_dva "Общение – взаимодействие индивидов или социальных групп,
        заключающееся в непосредственном обмене деятельностью, навыками,
        умениями, опытом, информацией и удовлетворяющее потребности человека
        в контактах с другими людьми."
        prepod_dva "Общение многогранно и может выполнять весьма разнообразные
        функции. Основными являются следующие"
        prepod_dva "- коммуникативная (состоит в обмене необходимой информацией);"
        prepod_dva "- интерактивная (функция организации взаимодействия, т. е.
        определение вида деятельности, распределение обязанностей и контроль за
        их выполнением, влияние на настроение, поведение, убеждение партнера по
        общению);"
        prepod_dva "- перцептивная (установление взаимопонимания в процессе
        деятельности)."
        prepod_dva "Общение становится возможным, если налицо все его единицы и каждая
        четко выполняет отведенную ей роль. Компонентами общения являются: 1)
        его участники; 2) предмет общения и 3) средства общения (словесные и
        несловесные)."
        prepod_dva "В основу классификации берут"
        prepod_dva "- вид деятельности человека (общение деловое и бытовое);"
        prepod_dva "- положение коммуникантов в пространстве (общение контактное и
        дистантное);"
        prepod_dva "- наличие или отсутствие опосредующего аппарата (общение
        непосредственное и опосредованное);"
        prepod_dva "- используемая форма языка (общение устное и письменное);"
        prepod_dva "- постоянство или изменчивость позиций «я говорящий» - «ты
        слушающий» (общение диалогическое и монологическое);"
        prepod_dva "- количество коммуникантов (общение межличностное и массовое);"
        prepod_dva "- степень общности (общение манипулятивное, примитивное,
        формально-ролевое, светское, деловое, духовное)."
        prepod_dva "Виды речевой деятельности – это различные виды речевых навыков
        и речевых умений."
        prepod_dva " Обычно выделяют четыре основных вида речевой
        деятельности: чтение, аудирование (слушание)"
        prepod_dva "Они объединяются под названием рецептивных видов речевой деятельности; говорение и письмо"

    play music zvonok
    
    scene kabinet
    prepod_dva "На следующей паре будем общаться по теме занятия"
    hide prepod_dva
    hide screen friendmeter_prep_dva
    stop music
    gg "Ох, наконец-то пара закончилась. Было ужасно"
    menu otziv:
        "Скучно":
            $ fr_prep_dva -= 10
            gg "Я и так все это знаю"

        "Интересно":
            $ fr_prep_dva += 10
            gg "Люблю уроки русского"

    gg "Пока не прозвенел звонок нужно решить что делать дальше"

    menu vibor:
        "Остаться в кабинете":
            gg "Перемена короткая, нет смысла куда-то идти"

        "Прогулять пару":
            gg "Не особо хочу оставаться на паре"
            gg "Тем более на спз с разговорами "
            $ proguli += 4
            jump konc

    gg "Чем же заняться?"

    "В кабинете осталось пару студентов"

    "Твой взгляд остановился на сидевшей перед тобой девушке"

    menu dev:
        "Окликнуть ее?"

        "Да":
            gg "Почему бы не пообщаться с одногруппницей?"

            show yn

            show screen friendmeter_yn

            gg "Эй, девушка!"

            "Ты толкнул ее в плечо"

            $ fr_yn -= 10
            xz "Чего?"

            gg "Хочу познакомиться с одногруппниками"

            $ fr_yn -= 10
            "Лицо девушки немного скривилось"

            gg "И прекрасными одногруппницами"

            $ fr_yn += 10
            "Она еле заметно улыбнулась"

            xz "Ну иди и знакомься. Я то тут при чем?"

            gg "Ну зачем же куда то идти, когда рядом есть такая красивая девушка!"
            $ fr_yn += 10

            "Девушка слегка закатила глаза"

            xz "Ну раз так, то давай знакомиться. Яна"

            gg "А меня зовут"
            menu name:
                "Василий":
                    $ fr_yn += 5
                    "Но можешь звать меня просто Васек"
                "Васек":
                    $ fr_yn -= 5

            yn "Чтож, приятно познакомиться Васек"

            jump para_2

            hide yn
            hide screen friendmeter_yn

        "Нет":
            gg "Зачем трогать человека?"
            jump para_2
    $ para +=1

label para_2:
    hide yn
    hide screen friendmeter_yn
    play music zvonok
    
    scene kabinet

    "Время перемены пролетело быстро"
    stop music

    "В кабинет вошла преподовательница"
    show prepod_dva at left with dissolve

    prepod_dva "Рада видеть тех, кто остался с нами"

    prepod_dva "Ну что готовы к занятию?"

    menu otv:
        "Промолчать":
            "Ты не видешь смысла отвечать на такое"

            xz "Да капитан!"

            prepod_dva "Что? Кто-то что-то смказал? Я не услышала?"

            xz '''Я сказал "так точно капитан"'''

            prepod_dva "А, это ваши шутки"

            prepod_dva "Ну значит к разговорам вы готовы"
            $ para +=1   
            $ fr_yn += 5

        "Ответить":
            gg "Будь готов!"

            xz "Всегда готов!"

            "Ты невольно улыбнулся"

            "Преподователь с улыбкой хмыкнула на твою выходку"
            $ fr_prep_dva += 5
            $ fr_ves += 5
            $ para +=1   


    prepod_dva "Ну хватит болтать. Пора заниматься"
    menu par_2:
        "Пропустить семинарское занятие?"
        "Да":
            $ pr +=1
        
        "Нет":
            $ pr = 0

    scene kabinet

    if pr > 0:
        scene blek
        "Тебя не сильно интересовало занятие"
        "В мире снов у тебя еще остались недосмротренные сюжеты"
        "Ты закрыл глаза и уснул"
        "Опять"

    elif pr == 0:
        scene kabinet
        prepod_dva "Что вы успели запомнить из сказаного мною ранее?"

        yn "Мы слушали про общение и коммуникацию"

        xz "Что-то про поболтушки и писанину"

        menu otv_2:
            "Промолчать":
                "А смысл что-то говорить?"
                

            "Ответить":
                $ zn =+1
                gg "Рассмотрели функции общения, виды речевой деятельности"
                gg "Что-то такое"
                $ fr_prep_dva += 5
                $ fr_yn -= 5
                prepod_dva "Ну хорошо, что-то в голове осталось. Молодцы!"
    
    scene kabinet
    

    "Оставшееся время пролетело незаметно"

    play music zvonok
    
    
    hide prepod_dva

    "Первые пары прошли быстро"
    stop music

    "Настало время большой перемны"

    menu bol_per:
        "Что делать на большой перемене?"

        "Пойти погулять по вузу":
            gg "Хочу размять ноги"
            jump kor_prog

        "Пойти на цокольный этаж":
            gg "Там вроде можно сыграть в пинг-понг"
            jump cok_prog

        "Пойти домой":
            gg "Уже и так много отсидел"
            $ proguli += 4
            jump konc
        
        "Пойти в библиотеку":
            gg "Хочу посидеть там"
            jump biblio_prog



label progul_1:

    gg "Теперь нужно придумать чем заняться"

    menu zan_na_prog:
        "Чем заняться в свободное время"

        "Пойти в библиотеку":
            jump biblio_prog

        "Пойти на цокольный этаж":
            jump cok_prog

        "Прогуляться по вузу":
            jump kor_prog

        "Пойти домой":
            "Пропустил одно занятие, можно и другие пропустить"
            $ proguli += 4
            jump konc


label biblio_prog:
    scene bibliotk_vnt_2
    "Библиотека была полу-пустой"
    "Ты сел за свободный стол"
    "Перед тобой стоит компьютер"

    menu komp:
        "Что делать?"

        "Включить компьютер":
            "Ты включил компьютер"
            "Все началось с просмотратра рандомных сайтов"
            "А закончилось играми в Яндексе"
            "Ты потерял счет времени и пропустил целую пару"
            $ proguli += 1
            $ para +=1
            menu ystala:
                "Что делать?"

                "Пойти на пару":
                    "Никогда не поздно учиться"
                    jump lekciy
                        
                "Пойти домой":
                    $ proguli += 1
                    gg "Ну а чего. Могy же"
                    jump konc


        "Не включать компьютер":
            if para >=1:
                "Ты не захотел включать компьютер"
                "И начал смотреть по сторонам"
                "И увидел знакомое лицо"

                gg "И снова привет"
                show yn 

                show screen friendmeter_yn

                "Яна ухмыльнулась"

                yn "Привет. Давно не виделись"
                $ fr_yn += 5

                yn "Не ожидала тебя тут увидеть"

                gg "Да и я тебя тоже"

                "Вы болтали всю перемену, пока не прозвенел звонок"
                play music zvonok
                

                yn "Пошли на пару, пока не опоздали"
                hide yn
                hide screen friendmeter_yn
                
                jump lekciy
                
                stop music
            
            else:
                "Ты не стал включать компьюетр"
                "И ничего в блиблиотеке не зацепило твой взор"
                "И ты пошел на пару"
            
                jump lekciy
                



label cok_prog:
    scene cokol_kor

    "Ты увидел стол для пинг-понга"
    "А рядом с ним сидел парень"
    
    show igor
    show screen friendmeter_xul

    xz "Здарова"

    gg "Ну здарова"

    xz "Игорь"

    menu names:
                "Василий":
                    $ fr_xul -= 5
                    "Но можешь звать меня просто Васек"
                "Васек":
                    $ fr_xul += 5

    igor "Ну приятно."
    igor "Чего, может сыграем в теннис?"

    menu igrylka:
        "Сыгарть в пинг-понг?"

        "Да":
            "Ну давай"
            $ fr_xul += 10
            hide igor
            hide screen friendmeter_xul
            jump ping_pong

        "Нет":
            gg "Сорянба, не игрок"
            $ fr_xul -= 20
            igor "Ну че тогда, вали отсюда"
            hide igor
            hide screen friendmeter_xul
            play music zvonok
            
           
            jump lekciy
            



label kor_prog:
    scene kol_kor_vt
    "Ты ходил по вузу без особой цели"
    "Как заметил знакомое лицо"
    show fan at left with dissolve
    show screen friendmeter_fan
    fan "Привет. Смотрю понравилось гулять по вузу"
    gg "Привет. Да вот решил походить на переменке"
    fan "Это ты мне удачно папался"
    fan "Если ты сейчас не сильно занят можешь помочь мне?"
    gg "А что нужно делать?"
    fan "Да помочь принести пару вещей из аудитории. А то рук не хватает"
    menu nus_sigraem:
        "Что ответить?"
        "Ну давай":
            fan "Спасибо!"
            $ fr_fan =+10
            hide fanR
            hide screen friendmeter_fan
            jump poick_predmetov

        "Сорянба, не могу":
            fan "Ну ладно. Беги тогда по делам"
            $ fr_fan =-10
            hide fan
            hide screen friendmeter_fan
            jump lekciy
            


    
label konc:
    scene vuz_menu
    if proguli >= 4:
        play music capog
        "У вас накопилось много прогулов"
        "Теперь ты свободный человек без каких-либо обязательств"
        show priz at left with dissolve
        
        priz "Добрый день, гражданин!"
        priz "До нас дошли вести, что вы молодой человек без отсрочки"
        priz "Разрешите пройти с нами!"
        window hide
        scene prizivnik
        pause
        $ proguli = 0
        "Концовка №1: Юность в сапогах"
        stop music
        return
    
    elif proguli == 0 and zn >= 4:
        scene vipusk
        play music vip
        "Ты ходил на все пары"
        "Ты показывал свои знания"
        "И смог закончить вуз с красным дипломом!"
        window hide
        pause
        $ proguli = 0
        "Концовка №2: Идеальный студент"
        stop music
        return
            

    elif proguli < 4 and zn <= 3:
        scene vipusk
        play music vip
        "Ты ходил на пары, но не особо проявлял интерес к учебе"
        "Однако ты все еще молодец!"
        window hide
        pause
        $ proguli = 0
        "Концовка №3: Студентик "
        stop music
        return

    else:
        scene vipusk
        play music vip
        "Как ты смог выпуститься?"
        "Тебе очень повезло"
        window hide
        pause
        $ proguli = 0
        "Концовка №4: Чертов везунчик"
        stop music
        return

    




