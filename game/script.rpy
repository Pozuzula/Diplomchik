init python:
    res = False
    start_game = 0
    kurs = 0
    name_gg = ""


label start:
         
    scene vuz_menu

    window hide

    a '''Наконец-то прошли 11 лет учебы в школе!

    Сданы экзамены и получен аттестат!

    И вот я стою перед зданием Московского университета
        
    Сегодня я пройдусь по его коридорам
        
    А уже завтра начну тут учиться '''

    nvl clear
    nvl hide
        
    jump nachalo_vuz
         


label kor_game:
    scene kol_kor_per
    show fan at left with dissolve
    fan "У тебя есть свободная минутка? Можешь мне помочь?"

    menu kor_game_menu:
        "Согласиться?"

        "Да":
            "Конечно!"
            jump poick_predmetov

        "Нет":
            "У меня нет на это времени"
            jump kol_holl


