init python:

    def set_countdown_timer(tm, tmr, tj):

        """
        Функция set_countdown_timer нужна для инициализации и запуска таймера обратного отсчета, необходимого для важных выборов в сюжете
        Параметры:
            @param tm (int, float) — Время, через которое таймер скроется с экрана и произойдет переход по метке, указанной в timer_jump
            @param tmr (int, float) - Время, в течении которого работает анимация на счетчике (Если $time < $timer_range анимация на счетчике пойдет не от самого края, если $time > $timer_range, то анимация на счетчике пойдет не сразу)
            @param tj (string) - Имя метки, на которую произойдет переход, если игрок ничего не выберет в течении времени, указанного в timer_time
        Источник: рецепты из документации движка
        Использование: <Максимально подробно описать использование функции в скрипте>
            $set_countdown_timer(параметры)
            window hide
            show screen countdown
            menu:
                "Вариант 1":
                    hide screen countdown
                    window show
                    действия
                другие варианты аналогично 

        """
        
        timer_time = tm
        timer_range = tmr
        timer_jump = tj

        _window_hide()
        renpy.call_screen(countdown)

    def init_timeskip_transition(t):

        """
        Функция init_timeskip_transition используется для инициализации анимации пропуска времени (не использовать отдельно)

        Параметры:
        @param t (int, float) - продолжительность анимации 

        """

        return ImageDissolve("images/transitions/timeskip.png", t, reverse=False)

    def timeskip_transition(t, sc, snd):

        """
        Функция timeskip_transition нужна для запуска анимации пропуска времени
        Параметры:
            @param t (int, float) — Полное время анимации
            @param sc (string) - Имя сцены, которую нужно показать после завершения анимации
            @param snd (bool) - Флаг, указывающий на необходимость воспроизведения звука тиканья часов при проигравании анимации
        Источник: БКРР (мод на Бесконечное Лето)
        Использование:
            $ timeskip_trs(3, 'walls_day', False)

        """

        _window_hide()
        if snd: renpy.music.play("music/sfx/clock_transition_sound.ogg", channel="sound", fadein=1, fadeout=1)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(timeskip_transition(t/2))
        renpy.scene()
        renpy.show(sc)
        renpy.with_statement(timeskip_transition(t/2))
        if snd: renpy.music.stop("sound")
        _window_show()

  ## Переключает новеллу в режим adv (стандартные реплики внизу экрана)
  ## Стырено из Бесконечного лета, нужно проверить работоспособность

    def set_mode_adv():

        """
        Функция set_mode_adv нужна для переключения новеллы в режим adv (стандартные реплики внизу экрана)
        Параметры:
            —
        Источник: Бесконечное Лето

        """        
        nvl_clear()
        global menu
        menu = renpy.display_menu

    def set_mode_nvl():

        """
        Функция set_mode_nvl нужна для переключения новеллы в режим nvl (реплики на полный экран)
        Параметры:
            —
        Источник: Бесконечное Лето

        """  
        nvl_clear()
        global menu
        menu = nvl_menu
