label sam_prologue:
    scene black

    $ set_mode_nvl()

    "Здравствуй, Сэмюэль."
    "Извини, что так долго тебе не писал. Я был очень занят, и не мог отвечать на письма"
    "Не знаю, как, но я подцепил какую-то болячку. Ко мне приходили люди в масках. Они называли себя врачами и просто разводили руками, когда я спрашивал про возможное лечение."
    "Боюсь, мне осталось не так много..."
    "С каждым днем мне все хуже и сейчас я не способен встать с постели"
    "Пожалуйста, приедь к своему старику, чтобы попрощаться."
    "Твой отец, Патрик."

    window hide

    scene bg samuel house night

    $ renpy.music.set_volume(0.3, delay=0, channel='ambient')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')

    play ambient rain

    window show

    "Я залетаю в дом и вижу отца, лежащего в постели"
    "Его лицо бледного цвета, а в глазах читается вся его боль."
    "Он слабо улыбается, видя меня"

    fath "Спасибо тебе. Прости, что заставил приехать"
    play sound father_cough_silent
    pause 1
    sam.char "Н-ничего, пап. Все нормально."
    sam.char "Сколько... тебе осталось?"
    play sound father_cough_loud
    pause 3

    fath "Эти гады в белых масках всё молчат, пытаясь скрыть правду."
    play sound father_cough_silent
    pause 2
    extend " Думают так легче..."
    pause 2
    extend " По правде говоря есть еще одна причина, по которой я тебя позвал."

    play sound father_cough_silent
    pause 2

    fath " В Альбисе живет мой брат, которому я так и не вернул долг. Прошу, выполни последнюю просьбу отца и отдай за меня долг. В моем столе лежит вся та сумма, которую я задолжал. Просто отвези ее."

    play sound father_cough_loud
    pause 3

    sam.char "Папа..."
    window hide
    pause 2
    sam.char "Отец... Нет.."

    dev "Пусть пока будет так, вроде норм :)"
    ## Интересный баг (или фича?) при перемотке сценария назад (через колесико мыши), 
    ## срабатывает повторное изменение здоровья.

    ## Переход между сценами с использованием эффекта моргания (более быстрый)


    # window hide
    # hide screen healthbar with dissolve
    # show blink with dissolve
    # pause(1)
    # scene bg column path day behind blink
    # hide blink
    # show unblink
    # pause(1.25)
    # show screen healthbar with dissolve
    # window show
    # "idhjsdih"
