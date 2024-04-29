
# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Eileen', color="#c8ffc8")
image eileen = "eileen.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    hide say
    # play music "menu.mp3"
    scene black
    "Мини игра пин понг"

    jump demo_minigame_pong #Переход на игру
    

    return

