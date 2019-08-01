init python:
    class Gameplay:

        ## TODO: (@dadyarri) Добавить создание персонажа Ren'Py в класс Trait
        ## (Добавить аргументы name, what_color, what_prefix, what_suffix, who_color)
        ## Пример:
        ## bh = Character(self.name, who_color=self.who_color, what_color=self.what_color, what_prefix=self.what_prefix, what_suffix=self.what_suffix)
        ## Документация: https://www.renpy.org/doc/html/python.html#define-statement

        class Trait():
            def __init__(self, min_value, max_value, init_value):
                self.min_value = min_value
                self.max_value = max_value
                self.init_value = init_value
                
            def increase():
                return self.init_value+1
                
            def decrease():
                return self.init_value-1
                
            def reset():
                return self.min_value
                
            def get():
                pass
                
            def more_than():
                pass
                
            def less_then():
                pass
                
            def is_over():
                pass
                
            
                  
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
