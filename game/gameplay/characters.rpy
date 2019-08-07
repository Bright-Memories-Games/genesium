init 1 python:
    ## Файл для описания персонажей.
    ## Пример (для неигровых персонажей):
    dev = Character ('Чокнутный разработчик', color='#016361')
    ## Документация по функции Character: https://renpy.org/doc/html/dialogue.html?highlight=character#Character

    ## Использование:
    ## dev "Какая-то реплика"

    ## Мысли главного героя (текст реплики окружен тильдами)
    th = Character(None, what_prefix='~', what_suffix='~')

    ## Рассказчик (текст реплики курсивом)
    narrator = Character(None, what_prefix='{i}', what_suffix='{/i}')

    ## NPC (неигровые персонажи):
    fath = Character('Отец', who_color='#FCCB2C', what_color='#fff')

    ## Джеймс Черношляп, главный герой основной арки
    ## Использование:
    ## bh.char "Реплика"
    bh = Hero(name='Джеймс Черношляп', who_color='#0414B4', what_color='#fff', what_prefix='', what_suffix='', init_loc='Nox', traits={"health": [0, 100, 100], "trust": [-50, 50, 0], "strength": [1, 10, 3], "perception": [1, 10, 8], "charisma": [1, 10, 6], "luck": [1, 10, 4]})


    ## Сэмюэль, главный герой демо-версии
    sam = Hero(name='Сэмюэль', who_color='#043424', what_color='#fff', what_prefix='', what_suffix='', init_loc='Hostalikon', traits={"health": [0, 100, 100], "trust": [-50, 50, 0], "strength": [1, 10, 7], "perception": [1, 10, 5], "charisma": [1, 10, 4], "luck": [1, 10, 4]})
