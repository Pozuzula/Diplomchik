
default max_fr = 100
default friend = 0
default fr_fan = 50
default fr_stryp = 50
default fr_prep_dva = 50
default fr_xul = 50
default fr_yn = 50
default fr_ves = 50

#screen timemeter:




#screen powermeter:




screen friendmeter_fan:
    vbar:
        xsize 220
        ysize 500
        xalign 0.95
        yalign 0.3
        value AnimatedValue(value=fr_fan, range=max_fr, delay=0.5)
        bottom_bar Frame("gui/bar/top.png",10,10)
        top_bar Frame("gui/bar/bot.png",10,10)


screen friendmeter_stryp:
    vbar:
        xsize 220
        ysize 500
        xalign 0.95
        yalign 0.3
        value AnimatedValue(value=fr_stryp, range=max_fr, delay=1.0)
        bottom_bar Frame("gui/bar/top.png",10,10)
        top_bar Frame("gui/bar/bot.png",10,10)

screen friendmeter_prep_dva:
    vbar:
        xsize 220
        ysize 500
        xalign 0.95
        yalign 0.3
        value AnimatedValue(value=fr_prep_dva, range=max_fr, delay=1.0)
        bottom_bar Frame("gui/bar/top.png",10,10)
        top_bar Frame("gui/bar/bot.png",10,10)

screen friendmeter_xul:
    vbar:
        xsize 220
        ysize 500
        xalign 0.95
        yalign 0.3
        value AnimatedValue(value=fr_xul, range=max_fr, delay=1.0)
        bottom_bar Frame("gui/bar/top.png",10,10)
        top_bar Frame("gui/bar/bot.png",10,10)

screen friendmeter_yn:
    vbar:
        xsize 220
        ysize 500
        xalign 0.95
        yalign 0.3
        value AnimatedValue(value=fr_yn, range=max_fr, delay=1.0)
        bottom_bar Frame("gui/bar/top.png",10,10)
        top_bar Frame("gui/bar/bot.png",10,10)


screen friendmeter_ves:
    vbar:
        xsize 220
        ysize 500
        xalign 0.95
        yalign 0.3
        value AnimatedValue(value=fr_ves, range=max_fr, delay=1.0)
        bottom_bar Frame("gui/bar/top.png",10,10)
        top_bar Frame("gui/bar/bot.png",10,10)

