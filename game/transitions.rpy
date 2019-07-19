## Анимация плавного исчезновения
## Стырено из официальных рецептов

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

## Анимация моргания
## Стырено из Бесконечного лета, работает

## Использование (для перехода между сценами) :
## scene сцена 1
## window hide
## show blink
## pause(3)
## scene сцена 2
## hide blink
## show unblink
## pause(2)
## window show

## Использование (для появления спрайтов, например, после пробуждения): 
## window hide
## show blink
## pause(1)
## show uv normal behind blink at center with dissolve
## hide blink
## show unblink
## pause(1)
## window show


image unblink:
    contains:
        "anim blink_up"
        xalign 0 yalign 0
        ease 1.5 pos (0,-1080)
    contains:
        "anim blink_down"
        xalign 0 yalign 0
        ease 1.5 pos (0,1080)

image blink:
    contains:
        "anim blink_up"
        pos (0,-1080)
        ease 1.5 xalign 0 yalign 0
    contains:
        "anim blink_down"
        pos (0,1080)
        ease 1.5 xalign 0 yalign 0


image blinking:
    contains:
        "anim blink_up"
        pos (0,-1080)
        ease 1.5 xalign 0 yalign 0
    contains:
        "anim blink_down"
        pos (0,1080)
        ease 1.5 xalign 0 yalign 0
    pause 2.0
    contains:
        "anim blink_up"
        xalign 0 yalign 0
        ease 1.5 pos (0,-1080)
    contains:
        "anim blink_down"
        xalign 0 yalign 0
        ease 1.5 pos (0,1080)
