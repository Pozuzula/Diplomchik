

# Определение персонажей игры.
define fan = Character('Анна Фандей', color="#c8ffc8")
image fan = "images/pin_pong/fandei(1).png"



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
    pass



label poick_predmetov:
    pass


label ping_pong:
    hide say

    #play music "menu.mp3"
    scene black
    "Мини игра пин понг"

    jump minigame_pong #Переход на игру
