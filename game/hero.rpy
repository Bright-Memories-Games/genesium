init python:
    class Hero:

        ## Инициализация персонажа (Ренпаевский Character, начальное местоположение)
        def __init__(self, name, who_color, what_color, what_prefix, what_suffix, init_geo):
            self.char = Character(name, who_color=who_color, what_color=what_color, what_prefix=what_prefix, what_suffix=what_suffix)
            self.geo = self.Geo(init_geo)

        ## Описание свойств персонажа и работа с ними
        class Trait:
            def __init__(self, min_value, max_value, init_value):

                ## min_value и max_value описывают допустимые границы характеристики
                ## current_value хранит текущее значение характеристики
                ## default_value хранит значение, заданное в начале игры и не должно изменяться
                self.min_value = min_value
                self.max_value = max_value
                self.current_value = init_value
                self.default_value = init_value

            def increase(self, value):
                
                ## Увеличивает текущее значение на указанное (передаваемое число должно быть положительным)
                if (value > 0):
                    if self.current_value + value > self.max_value:
                        self.current_value = self.max_value
                    else:
                        self.current_value += value
                else:
                    pass

            def decrease(self,value):

                ## Уменьшает текущее значение на указанное (передаваемое число должно быть положительным)
                if value > 0:
                    if self.current_value - value < self.max_value:
                        self.current_value = self.min_value
                    else:
                        self.current_value -= value
                else:
                    pass

            def reset(self):

                ## Сбрасывает текущее значение до значения по умолчанию
                self.current_value = self.default_value

            def get(self):

                ## Возвращает текущее значение параметра
                return self.current_value

            def more_than(self, value):

                ## Сравнивает выбранное значение с переданным (Если значение характеристики не меньше, то возвращает True)
                if self.current_value >= value:
                    return True
                else:
                    return False

            def less_then(self, value):

                ## Сравнивает выбранное значение с переданным (Если значение характеристики не больше, то возвращает True)
                if self.current_value <= value:
                    return True
                else:
                    return False

            def is_over(self):

                ## Сравнивает значение характеристики с её минимумом. Если равно, возвращает True.
                if self.current_value == self.min_value:
                    return True
                else:
                    return False

        class Geo:

            ## Описывает местоположение персонажа и управляет им.
            def __init__(self, init_geo):

                ## locations хранит список доступных локаций. Не должен изменяться
                ## current_geo хранит информацию о текущем местоположении
                ## default_geo хранит информацию о изначально заданном местоположении. Не должен изменяться
                self.locations = ['Albis', 'Hestir', 'Nox', 'Willaldan', 'Hostalikon', 'Galerenon', 'Fernlander', 'Lafetar']
                self.current_geo = init_geo
                self.default_geo = init_geo

            def current(self):

                ## Возвращает текущее местоположение персонажа
                return self.current_geo

            def reset(self):

                ## Сбрасывает текущее местоположение до начального
                self.current_geo = self.default_geo

            def jump_to(self, new_geo):

                ## Изменяет текущее местоположение
                if new_geo in self.locations:
                    self.current_geo = new_geo
                else:
                    pass
