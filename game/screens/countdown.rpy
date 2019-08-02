init offset = -1

## Экран таймера ################################################################
##
## Этот экран используется, чтобы показывать таймер обратного отсчета в выборах на время (time-to-action)
##

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0 yalign 0.03 xmaximum 300 at alpha_dissolve # This is the timer bar.
