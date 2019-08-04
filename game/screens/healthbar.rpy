screen healthbar:
    if main_char=='sam':
        vbar value StaticValue(sam.health.current_value, sam.health.max_value): # максимум - 100 hp
            xalign 0.01 yalign 0.01 # положение на экране
            xmaximum 200 # размеры
            ymaximum 200
            left_bar "../assets/images/gui/healthbar/heartempty.png" # пустое сердце
            right_bar "../assets/images/gui/healthbar/heartfull.png" # полное сердце
            thumb None # тут можно поставить разделитель
            thumb_shadow None # и тень
    if main_char == 'jbh':
       vbar value StaticValue(bh.health.current_value, bh.health.max_value): # максимум - 100 hp
            xalign 0.01 yalign 0.01 # положение на экране
            xmaximum 200 # размеры
            ymaximum 200
            left_bar "../assets/images/gui/healthbar/heartempty.png" # пустое сердце
            right_bar "../assets/images/gui/healthbar/heartfull.png" # полное сердце
            thumb None # тут можно поставить разделитель
            thumb_shadow None # и тень 
