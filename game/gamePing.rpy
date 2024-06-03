init:

    image bg pong field = "images/pin_pong/pong_field.png"

    python:
        import msvcrt, sys
        

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)
                
                
                self.veslo = Image("images/pin_pong/pong.png")
                self.mych = Image("images/pin_pong/pong_ball.png")
                self.player = Text(_("Игрок"), size=36)
                self.fanya = Text(_("Игорь"), size=36)
                self.ctb = Text(_("Игра началась"), size=36)

              
                self.veslo_WIDTH = 30
                self.veslo_HEIGHT = 79
                self.mych_WIDTH = 15
                self.mych_HEIGHT = 15
                self.ctol_TOP = 300
                self.ctol_BOTTOM = 930

                
                self.stuck = True

               
                self.playery = (self.ctol_BOTTOM - self.ctol_TOP) / 2
                self.computery = self.playery

                
                self.computerspeed = 350.0

            
                self.bx = 155
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5   
                self.bspeed = 400.0

              
                self.oldst = None

              
                self.winner = None

             
            def visit(self):
                return [ self.veslo, self.mych, self.player, self.fanya, self.ctb ]


            def render(self, width, height, st, at):

           
                r = renpy.Render(width, height)


                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

               
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed


                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)



                mych_top = self.ctol_TOP + self.mych_HEIGHT / 2 - 50
                if self.by < mych_top:
                    self.by = mych_top + (mych_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("images/pin_pong/pong_beep.wav", channel=0)


                mych_bot = self.ctol_BOTTOM - self.mych_HEIGHT / 2 + 50
                if self.by > mych_bot:
                    self.by = mych_bot - (self.by - mych_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("images/pin_pong/pong_beep.wav", channel=0)

  
                def veslo(px, py, hotside):


                    pi = renpy.render(self.veslo, 1980, 1020, st, at)


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


                veslo(130, self.playery, 120 + self.veslo_WIDTH)
                veslo(1780, self.computery, 1780)


                mych = renpy.render(self.mych, 1980, 1020, st, at)
                r.blit(mych, (int(self.bx - self.mych_WIDTH / 2),
                            int(self.by - self.mych_HEIGHT / 2)))


                player = renpy.render(self.player,1980, 1020, st, at)
                r.blit(player, (100, 70))

       
                fanya = renpy.render(self.fanya,1980, 1020, st, at)
                ew, eh = fanya.get_size()
                r.blit(fanya, (1800 - ew, 70))

        
                if self.stuck:
                    ctb = renpy.render(self.ctb, 1980, 1020, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (1000 - cw / 2, 70))


         
                if self.bx < 120:
                    self.winner = "Анна Фандей"


                    renpy.timeout(0)

                elif self.bx > 1900:
                    self.winner = "player"
                    renpy.timeout(0)

                

                

                renpy.redraw(self, 0)

               
                return r



          
            def event(self, ev, x, y, st):

                import pygame


                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                
                y = max(y, self.ctol_TOP)
                y = min(y, self.ctol_BOTTOM)
                self.playery = y



                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()
                
                



label ping_pong:
    hide say

    jump minigame_pong #Переход на игру


label minigame_pong:

    window hide None

    
    scene bg pong field

   
    python:

        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    

    window show None

    scene cokol_ping
    show igor
    show screen friendmeter_xul
    if winner == "Игорь":
        $ fr_xul += 10
        igor "Cюда!"
        igor "Ну не грусти, малыш, в следующий раз повезет"

    else:

        $ fr_xul += 30
        igor "Ты победил! Поздравляю. Ну в следующий раз не повезет."

    hide screen friendmeter_xul
    menu:
        igor "Давай еще раз сыграем?"

        "Конечно":
            jump minigame_pong

        "Не спасибо":
            hide igor
            "За игрой ты не заметил как прошло много времени и ты пропустил аж две пары!"
            $ proguli += 2
            $ para += 2
            if proguli >= 3:
                jump konc
            else:
 
                menu omgs:
                    "Что делать дальше?"

                    "Идти на пару":
                        gg "Ну не все же пропускать"
                        jump para_4
                    "Не идти на пару":
                        gg "Ну че уже пытаться-то"
                        jump konec
                    
