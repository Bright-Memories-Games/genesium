## Первое правило кодера: работает – не трогай!


## Как писать комментарии:
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.

## Как документировать функции:


## Краткое и понятное описание, того что должна делать функция
## Указание источника, откуда взята функция
## Работает ли функция, как должна
## Описание каждого параметра, который принимает функция:
## @param имя_параметра (тип) – описание параметра
## Использование: (как функция должна использоваться в новелле)


init python:

  ## Инициализация таймера обратного отсчета и его отображение перед важным выбором.
  ## Стырено из официальных рецептов, работает

  ## @param tm (целое или дробное число) - Время, через которое таймер скроется с экрана и произойдет переход по метке, указанной в timer_jump
  ## @param tmr (целое или дробное число) - Время, в течении которого работает анимация на счетчике (Если $time < $timer_range анимация на счетчике пойдет не от самого края, если $time > $timer_range, то анимация на счетчике пойдет не сразу)
  ## @param tj (строка) - Имя метки, на которую произойдет переход, если игрок ничего не выберет в течении времени, указанного в timer_time

  ## Использование:
  ## $set_countdown_timer(параметры)
  ## window hide
  ## show screen countdown
  ## menu:
  ##   "Вариант 1":
  ##      hide screen countdown
  ##      window show
  ##      действия
  ##    другие варианты аналогично 

  def set_countdown_timer(tm, tmr, tj):

    timer_time = tm
    timer_range = tmr
    timer_jump = tj
    _window_hide()
    renpy.call_screen(countdown)


  ## Описание анимации таймскипа (пропуск времени)
  ## Стырено из БКРР (мод на Бесконечное лето), работает

  ## Рисует переход со сцены на сцену при помощи стандартной функции и картинки (время берется из родительской функции – timeskip_trs)
  ## Не использовать отдельно!

  def timeskip_transition(t):
        return ImageDissolve("images/transitions/timeskip.png", t, reverse=False)


  ## Управляет отрисовкой анимации таймскипа (пропуск времени)
  ## Стырено из БКРР (мод на Бесконечное лето), работает

  ## @param t (целое или дробное число) - полное время выполнения анимации
  ## @param sc (строка) - название сцены, которую нужно показать после окончания анимации
  ## @param snd - (булево значение) - запуск анимации со звуком тиканья

  ## Использование:
  ## $timeskip_trs(3, 'walls_day', False)

  def timeskip_trs(t, sc, snd):
        _window_hide()
        if snd:
            renpy.music.play("music/sfx/clock_transition_sound.ogg", channel="sound", fadein=1, fadeout=1)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(timeskip_transition(t/2))
        renpy.scene()
        renpy.show(sc)
        renpy.with_statement(timeskip_transition(t/2))
        if snd:
            renpy.music.stop("sound")
        _window_show()

  ## Переключает новеллу в режим adv (стандартные реплики внизу экрана)
  ## Стырено из Бесконечного лета, нужно проверить работоспособность

  def set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu

        ## Переопределяет определения Character для соответствующих режимов новеллы
        
        ## global store
        ## for x in store.names_list:
        ##     char_define(x)

  ## Переключает новеллу в режим nvl (реплики на полный экран)
  ## Стырено из Бесконечного лета, нужно проверить работоспособность

  def set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global narrator
        global th
        narrator_nvl = narrator
        th_nvl = th

        ## Переопределяет определения Character для соответствующих режимов новеллы
        
        ## global store
        ## for x in store.names_list:
        ##     char_define(x,True)
