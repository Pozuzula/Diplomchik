init:

    image bg pong field = "images/pin_pong/pong_field.png"

    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)
                
                # Некоторые таблицы отображения, которые мы используем.
                self.veslo = Image("images/pin_pong/pong.png")
                self.mych = Image("images/pin_pong/pong_ball.png")
                self.player = Text(_("Игрок"), size=36)
                self.fanya = Text(_("Анна Фандей"), size=36)
                self.ctb = Text(_("Игра началась"), size=36)

                # Размеры некоторых изображений
                self.veslo_WIDTH = 30
                self.veslo_HEIGHT = 79
                self.mych_WIDTH = 15
                self.mych_HEIGHT = 15
                self.ctol_TOP = 300
                self.ctol_BOTTOM = 930

                # Если мяч застрял в весло.
                self.stuck = True

                # Позиции двух затворов.
                self.playery = (self.ctol_BOTTOM - self.ctol_TOP) / 2
                self.computery = self.playery

                # Скорость компьютера.
                self.computerspeed = 350.0

            # Положение, дентал-положение и скорость
            # мяч.
                self.bx = 155
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 400.0

                # Время прошлого рендера кадра.
                self.oldst = None

                #победитель.
                self.winner = None

            def visit(self):
                return [ self.veslo, self.mych, self.player, self.fanya, self.ctb ]

        # Пересчитывает положение мяча, ручками отбивается, и
# рисует на экране.
            def render(self, width, height, st, at):

                # Объект отображения, мы будем рисовать в.
                r = renpy.Render(width, height)

                # Выяснить время, прошедшее с предыдущего кадра.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                #Выяснить, где мы хотим, чтобы переместить мяч.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Переместить весло компьютера. Он хочет пойти в self.by но
                # может быть ограничена ограничить его скорость.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                # Ручка отскакивает.

                # Отскакивают от верхней.
                mych_top = self.ctol_TOP + self.mych_HEIGHT / 2 - 50
                if self.by < mych_top:
                    self.by = mych_top + (mych_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("images/pin_pong/pong_beep.wav", channel=0)

                # Отскакивают от дна.
                mych_bot = self.ctol_BOTTOM - self.mych_HEIGHT / 2 + 50
                if self.by > mych_bot:
                    self.by = mych_bot - (self.by - mych_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("images/pin_pong/pong_beep.wav", channel=0)

                # Это берет весло, и проверяет отскакивает.
                def veslo(px, py, hotside):

                # Отображение весло изображения
# чтобы представить, зная, что изображения будут меньше.
# (Это не в случае со всеми displayables. Твердый, Рамка,
# Исправлена и будет расширяться, чтобы заполнить выделенное пространство.)
# Проходим в ST и at.
                    pi = renpy.render(self.veslo, 1980, 1020, st, at)

                # renpy.оказывать возвращает объект визуализации, который мы можем
# блитировать на визуализации мы делаем.
                    r.blit(pi, (int(px), int(py - self.veslo_HEIGHT / 2)))

                    if py - self.veslo_HEIGHT / 2 <= self.by <= py + self.veslo_HEIGHT / 2:

                        hit = False

                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True

                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True

                        if hit:
                            renpy.sound.play("images/pin_pong/pong_boop.wav", channel=1)
                            self.bspeed *= 1.10

                # Нарисуйте два весла.
                veslo(130, self.playery, 120 + self.veslo_WIDTH)
                veslo(1780, self.computery, 1780)

            # Розыгрыш мяча.
                mych = renpy.render(self.mych, 1980, 1020, st, at)
                r.blit(mych, (int(self.bx - self.mych_WIDTH / 2),
                            int(self.by - self.mych_HEIGHT / 2)))

                # Показать имена игроков.
                player = renpy.render(self.player,1980, 1020, st, at)
                r.blit(player, (100, 70))

                # Имя.
                fanya = renpy.render(self.fanya,1980, 1020, st, at)
                ew, eh = fanya.get_size()
                r.blit(fanya, (1800 - ew, 70))

                # Показать "Нажмите, чтобы начать" метки.
                if self.stuck:
                    ctb = renpy.render(self.ctb, 1980, 1020, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (1000 - cw / 2, 70))


            # Проверка на победителя.
                if self.bx < 120:
                    self.winner = "Анна Фандей"

                # Необходима, чтобы гарантировать, что событие вызывается, заметив
                # победитель.
                    renpy.timeout(0)

                elif self.bx > 1900:
                    self.winner = "player"
                    renpy.timeout(0)

            # Прошу, чтобы нам быть повторно вынесено как можно скорее, так мы можем показать на следующей
            # рамы.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Обрабатывает события.
            def event(self, ev, x, y, st):

                import pygame

                # # Выбирете вниз == начать игру, установив застрял
# ложные.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                # Установить положение ракетки игрока
                y = max(y, self.ctol_TOP)
                y = min(y, self.ctol_BOTTOM)
                self.playery = y

            # Если у нас есть победитель, вернуть его или ее. В противном случае, игнорировать
# текущее событие
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()

label demo_minigame:

    fan "Да победит сильнейший!"

label minigame_pong:

    window hide None

    # Put up the pong background, in the usual fashion.
    scene bg pong field

    # Run the pong minigame, and determine the winner.
    python:

        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene cokol_ping
    show fan

    window show None


    if winner == "Анна Фандей":
        fan "Я выиграла!"

    else:


        fan "Ты победил! Поздравляю."


    menu:
        fan "Давай еще раз сыграем?"

        "Конечно.":
            jump minigame_pong
        "Не спасибо.":
            jump cok_itazh