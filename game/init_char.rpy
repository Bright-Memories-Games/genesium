init python:
    class Gameplay:

        ## TODO: (@dadyarri) Добавить создание персонажа Ren'Py в класс Trait
        ## (Добавить аргументы name, what_color, what_prefix, what_suffix, who_color)
        ## Пример:
        ## bh = Character(self.name, who_color=self.who_color, what_color=self.what_color, what_prefix=self.what_prefix, what_suffix=self.what_suffix)
        ## Документация: https://www.renpy.org/doc/html/python.html#define-statement

        class Trait:
            def __init__(self, min_value, max_value, init_value):
                self.min_value = min_value
                self.max_value = max_value
                self.this_value = init_value
                self.default_value = init_value

            def increase(self,value):
                if (value > 0):
                    if self.this_value + value > self.max_value:
                        self.this_value = self.max_value
                    else:
                        self.this_value += value
                else:
                    pass

            def decrease(self,value):
                if value > 0:
                    if self.this_value - value < self.max_value:
                        self.this_value = self.min_value
                    else:
                        self.this_value -= value
                else:
                    pass

            def reset(self):
                self.this_value = self.default_value

            def get(self):
                return self.this_value

            def more_than(self, value):
                if self.this_value >= value:
                    return True
                else:
                    return False

            def less_then(self, value):
                if self.this_value <= value:
                    return True
                else:
                    return False

            def is_over(self):
                if self.this_value == self.min_value:
                    return True
                else:
                    return False

        class Geo:
            def __init__(self, init_geo):
                self.locations = ['Albis', 'Hestir', 'Nox', 'Willaldan', 'Hostalikon', 'Galerenon', 'Fernlander', 'Lafetar']
                self.current_geo = init_geo
                self.default_geo = init_geo

            def current(self):
                return self.current_geo

            def reset(self):
                self.current_geo = self.default_geo

            def jump_to(self, new_geo):
                if new_geo in self.locations:
                    self.current_geo = new_geo
                else:
                    return 1
