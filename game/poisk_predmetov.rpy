init python:
    # окно по центру экрана
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # автоматическое объявление спрайтов
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ["images"]
    oXY = []
    pred = []
    oLen = 0
    maxLen = 0
    oBg = ""
    oLast = -1
    oTime = 0.0
    oMaxTime = 5.0
    needTimer = False
    oActive = False
    oRes = False

    # Инициализация игры, размещение предметов на экране
    def InitGame(bg, time, *args):
        global oBg, oXY, pred, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
        oXY = []
        pred = []
        oLen = 0
        oBg = bg
        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        oActive = True
        oRes = False
        if oTime > 0.0:
            needTimer = True
        for xy, obj_name in zip(args[0::2], args[1::2]):
            oXY.append(xy)
            pred.append(obj_name)
            maxLen += 1

    # Запуск игры
    def StartGame():
        global oActive
        oActive = True
        need = True
        while need:
            renpy.call_screen("igra", _layer="master")
            need = oRes == False
            if needTimer and (oTime <= .0):
                need = False

    # Показать экран игры в виде неактивного фона
    # Уже найденные предметы не будут отображаться
    def GameAsBG():
        global oActive
        oActive = False
        renpy.show_screen("igra", _layer="master")

    # Обработчик клика по предмету
    def o_click(i):
        global oLen, oRes
        if i >= 0:
            if pred[i]:
                temp = pred[i]
                pred[i] = ""
                oLen += 1
                renpy.restart_interaction()
                if needTimer:
                    if oLen >= maxLen:
                        oRes = True
                else:
                    oRes = temp
    oClick = renpy.curry(o_click)

# Собственно экран игры, запускать из функции StartGame()
screen igra:

    modal True

    add oBg
    for i in range(0, len(pred)):
        if pred[i]:
            imagebutton:
                focus_mask True
                pos(oXY[i])
                idle pred[i]
                hover pred[i] + "_cvet"
                if oActive:
                    action [oClick(i), Return()]
                else:
                    action []




screen info:
    frame:
        padding(10, 10)


        vbox:
            text "Нужно найти:"
            text "Ручка"
            text "Тетрадка"
            text "Лампа"
            text "Телефон"
            text "Цветок"



