label sam_prologue:
    scene bg samuel house night

    show screen healthbar with dissolve

    ## Эксперименты с Traits
    sam.char "Начальное значение здоровья [sam.health.current_value]"
    $ sam.health.decrease(30)
    play music rain
    play sound father_cough fadeout 1.0 fadein 0.5 
    bh.char "Здоровье: [sam.health.current_value]"
    $ sam.health.increase(20)
    "Здоровье: [sam.health.current_value]"
    $ sam.health.increase(20)
    "Здоровье: [sam.health.current_value]"
    $ sam.health.decrease(50)
    "Здоровье: [sam.health.current_value]"
    stop sound
  
    ## Интересный баг (или фича?) при перемотке сценария назад (через колесико мыши), 
    ## срабатывает повторное изменение здоровья.

    ## Переход между сценами с использованием эффекта моргания (более быстрый)
    window hide
    hide screen healthbar with dissolve
    show blink with dissolve
    pause(1)
    scene bg column path day behind blink
    hide blink
    show unblink
    pause(1.25)
    show screen healthbar with dissolve
    window show
    "idhjsdih"
