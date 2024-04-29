init:

    image bg pong field = "images/pin_pong/pong_field.png"

    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # Некоторые таблицы отображения, которые мы используем.
                self.paddle = Image("images/pin_pong/pong.png")
                self.ball = Image("images/pin_pong/pong_ball.png")
                self.player = Text(_("Игрок"), size=36)
                self.eileen = Text(_("Eileen"), size=36)
                self.ctb = Text(_("Игра началась"), size=36)

                # Размеры некоторых изображений
                self.PADDLE_WIDTH = 8
                self.PADDLE_HEIGHT = 79
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 98
                self.COURT_BOTTOM = 530

                # Если мяч застрял в весло.
                self.stuck = True

                # Позиции двух затворов.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # Скорость компьютера.
                self.computerspeed = 350.0

            # Положение, дентал-положение и скорость
            # мяч.
                self.bx = 88
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 300.0

                # Время прошлого рендера кадра.
                self.oldst = None

                #победитель.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.eileen, self.ctb ]

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
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("images/pin_pong/pong_beep.wav", channel=0)

                # Отскакивают от дна.
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("images/pin_pong/pong_beep.wav", channel=0)

                # Это берет весло, и проверяет отскакивает.
                def paddle(px, py, hotside):

                # Отображение весло изображения. Мы даем его площадь 800х600
# чтобы представить, зная, что изображения будут меньше.
# (Это не в случае со всеми displayables. Твердый, Рамка,
# Исправлена и будет расширяться, чтобы заполнить выделенное пространство.)
# Проходим в ST и at.
                    pi = renpy.render(self.paddle, 800, 600, st, at)

                # renpy.оказывать возвращает объект визуализации, который мы можем
# блитировать на визуализации мы делаем.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

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
                paddle(68, self.playery, 68 + self.PADDLE_WIDTH)
                paddle(724, self.computery, 724)

            # Розыгрыш мяча.
                ball = renpy.render(self.ball, 800, 600, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                            int(self.by - self.BALL_HEIGHT / 2)))

                # Показать имена игроков.
                player = renpy.render(self.player, 800, 600, st, at)
                r.blit(player, (20, 25))

                # Имя Айлин.
                eileen = renpy.render(self.eileen, 800, 600, st, at)
                ew, eh = eileen.get_size()
                r.blit(eileen, (790 - ew, 25))

                # Показать "Нажмите, чтобы начать" метки.
                if self.stuck:
                    ctb = renpy.render(self.ctb, 800, 600, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (400 - cw / 2, 30))


            # Проверка на победителя.
                if self.bx < -200:
                    self.winner = "eileen"

                # Необходима, чтобы гарантировать, что событие вызывается, заметив
                # победитель.
                    renpy.timeout(0)

                elif self.bx > 1000:
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
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y

            # Если у нас есть победитель, вернуть его или ее. В противном случае, игнорировать
# текущее событие
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()

label demo_minigame:

    e "Да победит сильнейший!"

label demo_minigame_pong:

    window hide None

    # Put up the pong background, in the usual fashion.
    scene bg pong field

    # Run the pong minigame, and determine the winner.
    python:

        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene black
    show eileen 

    window show None


    if winner == "eileen":
        e "Я выиграла!"

    else:


        e "Ты победил! Поздравляю."


    menu:
        e "Давай еще раз сыграем?"

        "Конечно.":
            jump demo_minigame_pong
        "Не спасибо.":
            pass