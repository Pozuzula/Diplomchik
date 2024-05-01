init python:
    res = False

# Определение персонажей игры.
define fan = Character('Анна Фандей', color="#c8ffc8")
image fan = "images/pin_pong/fandei.png"



# Игра начинается здесь:
label start:
    show fan at left with dissolve

    fan "Привет. Давай поиграем?"

    fan "Во что хочешь поиграть?"

    menu igri:
        "Выбери игру"

        "Пин-понг":
            jump ping_pong

        "3 в ряд":
            jump tri_v_ryd

        "Поиск предметов":
            jump poick_predmetov


label konec:
    show fan at left with dissolve

    "Хорошо поиграли"
    "Хочешь еще?"

    menu echo:
        "Poigraem?"

        "Да":
            jump igri

        "Нет":
            pass

label tri_v_ryd:
    "А тут ничего("
    jump konec



label poick_predmetov:

    scene black
    # заполняем экран игры объектами
    #$ InitGame("poisk_fon", 5.0, (1675, 600), "lampa", (1420, 445), "cvetok", (10, 10), "telefon", (1480, 810), "rychka", (1040, 780), "tetradka")
    $ InitGame("poisk_fon", 5.0, (0, 0), "cvetok", (0, 0), "lampa", (0, 0), "telefon", (0, 0), "rychka", (0, 0), "tetradka" )
    # показываем экран игры в качестве простого фона
    $ GameAsBG()
    with dissolve

    # запускаем игру и играем
    $ res = StartGame()

    # снова показываем в качестве фона
    # (но уже без найденных во время игры предметов)
    $ GameAsBG()

    # проверяем результаты игры и обыгрываем их в сценарии
    if oRes:
        "Фух... Вовремя"
    else:
        "Не успел("
        
    jump konec



label ping_pong:
    hide say

    #play music "menu.mp3"
    scene black
    "Мини игра пин понг"

    jump minigame_pong #Переход на игру
