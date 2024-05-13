
label nachalo_vuz:
    scene holl
    show fan at left with dissolve
    fan "Привет, меня зовут Аня, я расскажу и покажу тебе про Московский университет имени Витте!"
    fan "Рада приветствовать тебя в стенах нашего вуза!"
    # сделать фон чб
    fan "Он был основан в 1993 году! В прошлом году нашему вузу исполнилось 30 лет."
    # (вернуть нормальный фон)
    fan "В 2011 году было получено звание Университета и делается все, чтобы соответствовать этому высокому статусу!"
    fan "В 2020 году вуз в очередной раз успешно прошел аккредитацию, поэтому можно не переживать. Диплом будет выдаваться государственного образца. "
    fan "Помимо этого, вуз стабильно занимает высокие места в рейтингах частных ВУЗов страны!"
    fan "Наше знакомство начинается в холле университета. Здесь находится зона отдыха для студентов. А так же ставится сцена на мероприятия, которые организовывает студенческий совет." 
    fan "Университет вед активную студенческую жизнь как в учебной части, так и во вне учебном плане. Мы отмечаем такие праздники как 23 февраля и 8 марта. Новый год, Хэллоуин."
    fan "Одним из самых масштабных мероприятий является посвящение в студенты. Скучно точно не будет!"
    fan "Ты можешь сам решать куда пойти."
    menu holl_menu:
        
        "Куда пойти?"
        "Влево":
            jump kab_107

        "Вправо":
            jump stend_kyb



label kab_107:
    scene kab_107
    "Так же на первом этаже находится студенческий офис. Или 107 кабинет. Это Многофункциональный центр нашего Университета."
    "Здесь Вы сможете задать любой вопрос и Вам окажут консультационную помощь, выдадут документ, справку, помогут решить проблему."
    menu kab_17_menu:
        "Куда идти?"

        "Вперед":
            jump nagradi

        "Назад":
            jump nachalo_vuz



label nagradi:
    scene vuz_nagradi
    "Наш вуз неоднакратно принимал участие в различных форумах и получал высокие награды." # посмотерть награды на стенде для примеров
    "Помимо этого, наш вуз занимает высокие позиции в рейтингах негосударсвенных вузов России!"

    menu nagradi_menu:
        "Куда идти?"

        "Вперед":
            jump stend_sted_life

        "Назад":
            jump kab_107



label stend_sted_life:
    scene stud_jizn
    "Так же тут есть стенд “Студенческая жизнь”, на котором вы можете увидеть насколько яркая и насыщенная жизнь у наших студентов."
    
    menu stend_sted_life_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_1

        "Назад":
            jump nagradi


label stend_kyb:
    scene stend_kubki
    "Так же тут можно увидеть стенд с кубками и наградами, которые получают студенты нашего вуза на мероприятиях."
    "Наши студенты неоднократно учавствуют в футбольных сореванованиях и занимают первые места."
    
    menu stend_kyb_menu:
        "Куда идти?"

        "Вперед":
            jump kassa  

        "Назад":
            jump nachalo_vuz


label kassa:
    scene krasn_kor
    "При поступлении, после заключения договора, студент может сразу оплатить обучение как на пол года, так и на всеь учебный год."
    "Делается это в кассе внутри университета! Она рабоатет каждый день. Так что любой студент может приехать и оплатить обучение в вузе в удобное для него время"

    menu kassa_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_2

        "Назад":
            jump stend_kyb

label kr_kor:
    scene krasn_kor

    "На первом этаже располагается кабинет медицинского персонала, где дежурит квалифицированный сотрудник, готовый оказать первую помощь всем нуждающимся. "
    "Так же в 111 кабинете располагается центр карьеры, практики и трудоустройства.  Университет ведет активную деятельность по организации практики студентов и трудоустройству выпускников. "
    "Главная красота первого этажа – коридор «Аллея славы Витте». Здесь представлены ключевые моменты жизни и деятельности великого Сергея Юльевича Витте."
    "На стене вывешены картины с интерсеными фактами о великом деятеле."

    menu  kr_kor_menu:
        "Куда идти?"

        "Дальше":
            jump kab_1_itazh

        "Назад":
            jump lectnica_2



label kab_1_itazh:
    scene krasn_kor_vtor
    "На первом этаже распологаются небольшие аудитории для семинарских занятий. Чаще всего ими пользуются студенты заочной формы образования."
    "Так же тут стоит кулер с водой, которым могут пользоваться все студенты."

    menu kab_1_itazh_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_3

        "Назад":
            jump kr_kor

label cok_itazh:
    scene cokol_kor
    "Это цокольный этаж. Здесь стоять столы для пинг-понга, которыми могут пользоваться все студенты вуза. Так же тут находится книгохранилище."

    menu cok_itazh_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_16

        "Подойти к столу для пинг-понга":
            jump  ping_pong_mini_game

        "Назад":
            jump lectnica_1

label ping_pong_mini_game:
    scene cokol_ping
# Здесь должан быть мини игра пинг понг. 
    jump ping_pong
    

label kol_holl:

    scene kol_itazh

    "Это холл колледжа. Он светлый и просторный. Выйти из здания колледжа можно через турникету, однако войти можно только через здание вуза"

    menu kol_holl_menu:
        "Куда идти?"

        "Вперед":
            jump kol_kor

        "Назад":
            jump lectnica_16

label kol_kor:
    scene kol_kor_per

    "Не так давно колледж был отремонтирован и выполнин в одной стилистике - лофт. "

    menu kol_kor_menu:
        "Куда идти?"

        "Вперед":
            jump kol_kab

        "Назад":
            jump kol_holl

label kol_kab:
    scene kol_kab

    "А так выглядят кабинеты колледжа"

    menu kol_kab_menu:

        "Вернуться в коридор":
            jump kor_game


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

        


label biblioteca:
    scene bibl

    "Это библиотека вуза. В ней каждый студент и преподователь может подготовится к своим предметам, позаниматься в свободнео время или прсотовзять книгу почитать. Доступны как учебники, так и другая литература"
    "Тут размещены компьютеры, на которых студенты могут заниматься и готовится к занятиям. "

    menu biblioteca_menu:
        "Куда идти?"

        "Остаться":
            jump biblioteca

        "Уйти":
            jump lectnica_17

label biblioteca_vnt:
    scene bibliotk_vnt

    menu biblioteca_vnt_menu:
        "Вернуться"

        "Уйти":
            jump lectnica_17


label vtoroy_itazh:
    scene kor_vtor_vtor
    "Второй этаж полностью отдан юридическому факультету. На нем расположены как большие кабинеты для лекций, так и небольшие для семинарских занятий.  "

    menu vtoroy_itazh_menu:
        "Куда идти?"

        "Вперед":
            jump stud_sovet

        "Назад":
            jump lectnica_4

label stud_sovet:
    scene stud_sovet
    "Здесь распологается студенческий совет. Это самые активные студенты вуза! Они организовывают мероприятия вуза для студентов, помогают с официальными мероприятиями, а так же классно проводят время."
    "Если захочешь, ты сможешь к ним попасть и быть частью этого классного коллектива!"

    menu stud_sovet_menu:
        "Куда идти?"

        "Вперед":
            jump yr_klinica

        "Назад":
            jump vtoroy_itazh

label yr_klinica:
    scene kor_vtor_vtor
    "На базе Юридического факультета работает Юридическая клиника, которая помогает в решение правовых вопросов."

    menu yr_klinica_menu:
        "Куда идти?"

        "Вперед":
            jump yr_decanat

        "Назад":
            jump stud_sovet

label auditorii_2itazh:
    scene kor_vtor_vtor
    "На втором этаже в основном распологаются большие аудитории для лекций у всего потока."
    "Аудитория для лекций оснащена всей медиа техникой. В нем есть и проектор, экран, ноутбук и микрофон, что бы было слышно везде."

    menu auditorii_2itazh_menu:
        "Куда идти?"

        "Вперед":
            jump yr_decanat

        "Назад":
            jump yr_klinica

label yr_decanat:
    scene kor_vtor_vtor
    "На втором этаже распологается деканат Юридического факультета"

    menu yr_decanat_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_5

        "Назад":
            jump stud_sovet

label yr_facultet:
    scene kor_vtor_vtor
    "На втором этаже располагаются кайфедра уголовного права и процесса и кафедра Гражданского права и процесса."

    menu yr_facultet_menu:
        "Куда идти?"

        "Вперед":
            jump zal_zac

        "Назад":
            jump lectnica_5

label zal_zac:
    scene kor_vtor_vtor
    "Рядом со столовой располагается зал судебных заседаний. Оно предназначен для семинарских занятий студентов по правовым дисциплинам."

    menu zal_zac_menu:
        "Куда идти?"

        "Вперед":
            jump cafe

        "Назад":
            jump yr_facultet

label cafe:
    scene stol_stoli
    "А это любое место всех студентов – Студенческое кафе «»."
    "Студенческое кафе достаточно большое и вместительное. Много столов вмещают множество студентов. "
    "Внутри столовой стоят несколько микроволновых печей, в которых можно разогреть еду. Можно купить хот-дог, молочный коктейль, покушать в столовой или купить воды, булочки, и мелкие снеки."

    menu cafe_menu:

        "Назад":
            jump zal_zac

label tretiy_itazh:
    scene tret_dal_kor
    "Третий этаж – два факультета: факультет экономики и финансов и факультет управления. Сейчас мы находимся в крыле факультета экономики и финансов.  "
    "Здесь расположены преимущественно маленькие аудитории для семинарских занятий. В этих аудиториях преподаватели проводят практические занятия с группами."

    menu tretiy_itazh_menu:
        "Куда идти?"

        "Вперед":
            jump koridor_tretiy

        "Назад":
            jump lectnica_6

label koridor_tretiy:
    scene tret_dal_kor
    "Здесь рапологаются Кафедра экономики городского хозяйства и сферы обслуживания, а так же Кафедра финансового учета"

    menu koridor_tretiy_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_7

        "Назад":
            jump tretiy_itazh

label ypr_facultet:
    scene tret_dal_kor
    "Здесь распологаются Кафедры менедмента, реклами и человеческих ресурсов, психологии и педагогике. А так же Деканат факультета управления."

    menu ypr_facultet_menu:
        "Куда идти?"

        "Вперед":
            jump dal_kor_tretiy

        "Назад":
            jump lectnica_7

label dal_kor_tretiy:
    scene tret_dal_kor
    "Так же в вузе работает центр дополнительного профессионального образования. Благодаря ему вы модете пройти куросы повышения квалификации или переподготовки."
    "Помимо этого на третьем этаже располоается Научно-Образовательный центр Устойчевого развития."
    "И вот уже более 5 лет в Университета развиваетяс анправление магистратуры Менеджер усойчевого развития"

    menu dal_kor_tretiy_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_8

        "Назад":
            jump ypr_facultet

label adminictraciya:
    scene adminictraciya
    "Здесь распологаетяс Администрация вуза. Студентом сюда заходить без необходимости запрещено."
    "Лучше идти дальше"

    menu adminictraciya_menu:
        "Куда идти?":
            jump lectnica_9


label kab_chetv:
    scene kor_tret
    "На четвертом этаже распалагаются достаточно просторные кабинеты. Они подходят как для лекций, так и для практический занятий."

    menu kab_chetv_menu:
        "Куда идти?"

        "Вперед":
            jump dovuz_podgot

        "Назад":
            jump lectnica_10

label dovuz_podgot:

    "Так же на четвертом эnаже распологается отдел довузовской подготовки"

    menu dovuz_podgot_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_11

        "Назад":
            jump kab_chetv

label decan_fit:
    scene pyt_kor_od
    "На пятом этаже распологается Факультет Информационных технологий."
    

    menu decan_fit_menu:
        "Куда идти?"

        "Вперед":
            jump kab_pyt

        "Назад":
            jump lectnica_12

label kab_pyt:
    scene pyt_kor_vt
    "Практически сразу же нас встречает Деканат Факультета, а так же Кафедры информационных систем и математический и естесвеннонаучных дисциплин."

    menu kab_pyt_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_13

        "Назад":
            jump decan_fit

label dal_kab_pyt:
    scene pyt_kor_vt
    "Преимущесвенно здесь распологаются небольшие кабинеты оснащенные техникой для работы за песрональными компьюетарми на семинарских занятиях."
    "Рабоат преподователя транслируется на больших экранах в кабинете. А студенты выполняют ее индивидуально на компьютере."

    menu dal_kab_pyt_menu:
        "Куда идти?"

        "Вперед":
            jump lectnica_14

        "Назад":
            jump kab_pyt




label lectnici:
    scene lec_2_2
    menu lectnica_1:
        
        "Куда пойти?"

        "На 5 этаж":
            jump decan_fit

        "На 4 этаж":
            jump adminictraciya

        "На 3 этаж":
            jump tretiy_itazh

        "На 2 этаж":
            jump vtoroy_itazh

        "В библиотеку":
            jump biblioteca

        "Остаться на этаже":
            jump stend_sted_life_menu
        
        "Спуститься на цокольный этаж":
            jump cok_itazh
        
    
    menu lectnica_2:
        "Куда пойти?"

        "На 5 этаж":
            jump kab_pyt

        "На 4 этаж":
            jump kab_chetv

        "На 3 этаж":
            jump koridor_tretiy

        "На 2 этаж":
            jump yr_decanat

        "Идти дальше по этажу":
            jump kr_kor

        "Идти назад по коридору":
            jump kassa

    menu lectnica_3:
        "Куда пойти?"

        "На 5 этаж":
            jump dal_kab_pyt

        "На 4 этаж":
            jump dovuz_podgot

        "На 3 этаж":
            jump dal_kor_tretiy 

        "Остаться на этаже":
            jump kab_1_itazh_menu


    menu lectnica_4:
        "Куда пойти?"

        "На 5 этаж":
            jump decan_fit

        "На 4 этаж":
            jump adminictraciya

        "На 3 этаж":
            jump tretiy_itazh

        "Остаться на этаже":
            jump vtoroy_itazh
        
        "Спуститься на 1 этаж":
            jump stend_sted_life


    menu lectnica_5:
        "Куда пойти?"

        "На 5 этаж":
            jump kab_pyt

        "На 4 этаж":
            jump kab_chetv

        "На 3 этаж":
            jump koridor_tretiy
        
        "Спуститься на 1 этаж":
            jump kassa

        "Идти дальше по этажу":
            jump yr_facultet



    menu lectnica_6:
        "Куда пойти?"

        "На 5 этаж":
            jump decan_fit

        "На 4 этаж":
            jump adminictraciya

        "Остаться на этаже":
            jump tretiy_itazh

        "Спуститься на 2 этаж":
            jump vtoroy_itazh

        
        "Спуститься на 1 этаж":
            jump stend_sted_life

    menu lectnica_7:
        "Куда пойти?"

        "На 5 этаж":
            jump kab_pyt

        "На 4 этаж":
            jump kab_chetv

        "Идти дальше по этажу":
            jump ypr_facultet 

        "Спуститься на 2 этаж":
            jump yr_decanat

        
        "Спуститься на 1 этаж":
            jump kassa


    menu lectnica_8:
        "Куда пойти?"

        "На 5 этаж":
            jump dal_kab_pyt

        "На 4 этаж":
            jump dovuz_podgot

        "Остаться на этаже":
            jump dal_kor_tretiy
        
        "Спуститься на 1 этаж":
            jump kab_1_itazh

    menu lectnica_9:
        "Куда пойти?"

        "На 5 этаж":
            jump decan_fit

        "Спуститься на 3 этаж":
            jump tretiy_itazh

        "Спуститься на 2 этаж":
            jump vtoroy_itazh

        "Спуститься на 1 этаж":
            jump stend_sted_life

    menu lectnica_10:
        "Куда пойти?"

        "На 5 этаж":
            jump kab_pyt

        "Остаться на этаже":
            jump kab_chetv
        
        "Спуститься на 3 этаж":
            jump koridor_tretiy

        "Спуститься на 2 этаж":
            jump yr_decanat

        "Спуститься на 1 этаж":
            jump kassa

    menu lectnica_11:
        "Куда пойти?"

        "На 5 этаж":
            jump dal_kab_pyt

        "Остаться на этаже":
            jump dovuz_podgot
        
        "Спуститься на 3 этаж":
            jump dal_kor_tretiy

        "Спуститься на 1 этаж":
            jump kab_1_itazh


    menu lectnica_12:
        "Куда пойти?"

        "Остаться на этаже":
            jump decan_fit
        
        "Спуститься на 4 этаж":
            jump adminictraciya
        
        "Спуститься на 3 этаж":
            jump tretiy_itazh

        "Спуститься на 2 этаж":
            jump vtoroy_itazh

        "Спуститься на 1 этаж":
            jump stend_sted_life

    menu lectnica_13:
        "Куда пойти?"

        "Идти дальлше":
            jump dal_kab_pyt
        
        "Спуститься на 4 этаж":
            jump kab_chetv
        
        "Спуститься на 3 этаж":
            jump  koridor_tretiy

        "Спуститься на 2 этаж":
            jump yr_decanat

        "Спуститься на 1 этаж":
            jump kassa

    menu lectnica_14:
        "Куда пойти?"

        "Остаться на этаже":
            jump dal_kab_pyt
        
        "Спуститься на 4 этаж":
            jump dovuz_podgot
        
        "Спуститься на 3 этаж":
            jump dal_kor_tretiy

        "Спуститься на 1 этаж":
            jump kab_1_itazh

    menu lectnica_17:
        "Куда пойти?"
        
        "На 5 этаж":
            jump decan_fit

        "На 4 этаж":
            jump adminictraciya

        "На 3 этаж":
            jump tretiy_itazh

        "Подняться на 2 этаж":
            jump vtoroy_itazh

        "Остаться на этаже":
            jump biblioteca

        "Спуститься на 1 этаж":
            jump lectnica_1


label lectnici_kolledj:
    menu lectnica_15:
        "Куда пойти?"

        "Подняться на 3 этаж":
            pass

        "Подняться на 2 этаж":
            pass

        "Остаться на этаже":
            jump kol_holl
        
        "Спуститься на цокальный этаж":
            jump cok_itazh

    menu lectnica_16:
        "Куда пойти?"

        "Подняться на 3 этаж":
            pass

        "Подняться на 2 этаж":
            pass
        
        "Подняться на 1 этаж":
            jump kol_holl

        "Остаться на этаже":
            jump cok_itazh
        
        

