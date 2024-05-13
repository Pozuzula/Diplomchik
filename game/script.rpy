init python:
    res = False



label start:
    jump nachalo_vuz


label poick_predmetov:

    show fan at left with dissolve
    fan "Помоги найти мне лампу, цветок, телефон, ручку и тетрадку пожалуйста. Они должны стоять в кабинете"

    scene black
    window hide
    show screen info   
    # заполняем экран игры объектами
    #$ InitGame("poisk_fon", 5.0, (1675, 600), "lampa", (1420, 445), "cvetok", (10, 10), "telefon", (1480, 810), "rychka", (1040, 780), "tetradka")
    $ InitGame("poisk_fon", 5.0, (0, 0), "cvetok", (0, 0), "lampa", (0, 0), "telefon", (0, 0), "rychka", (0, 0), "tetradka" )
    # показываем экран игры в качестве простого фона
    $ GameAsBG()
    with dissolve

    # запускаем игру и играем
    $ res = StartGame()
    hide screen info 
    # снова показываем в качестве фона
    # (но уже без найденных во время игры предметов)
    $ GameAsBG()

    # проверяем результаты игры и обыгрываем их в сценарии
    if oRes:
        "Спасибо за помощь!"
    else:
        "Мне уже надо идти. В следующий раз будь быстрее!"
        
    jump kol_holl



label ping_pong:
    hide say

    #play music "menu.mp3"
    scene black
    "Мини игра пин понг"

    jump minigame_pong #Переход на игру
