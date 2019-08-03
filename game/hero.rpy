init python:
    class Hero:

        ## Инициализация персонажа (Ренпаевский Character, начальное местоположение, описание характеристик)
        def __init__(self, name, who_color, what_color, what_prefix, what_suffix, init_loc, traits):
            self.char = Character(name, who_color=who_color, what_color=what_color, what_prefix=what_prefix, what_suffix=what_suffix)

            self.health = self.Trait(traits.get("health")[0], traits.get("health")[1], traits.get("health")[2])
            self.trust = self.Trait(traits.get("trust")[0], traits.get("trust")[1], traits.get("trust")[2])
            self.strength = self.Trait(traits.get("strength")[0], traits.get("strength")[1], traits.get("strength")[2])
            self.perception = self.Trait(traits.get("perception")[0], traits.get("perception")[1], traits.get("perception")[2])
            self.charisma = self.Trait(traits.get("charisma")[0], traits.get("perception")[1], traits.get("perception")[2])
            self.luck = self.Trait(traits.get("luck")[0], traits.get("luck")[1], traits.get("luck")[2])

            self.loc = self.Geo(init_loc)

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
                ## Использование:
                ## $ sam.health.increase(30)
                ## Увеличит здоровье Сэмюэля на 30 единиц, или установит максимум (100)
                if (value > 0):
                    if self.current_value + value > self.max_value:
                        self.current_value = self.max_value
                    else:
                        self.current_value += value
                else:
                    pass

            def decrease(self,value):

                ## Уменьшает текущее значение на указанное (передаваемое число должно быть положительным)
                ## Использование:
                ## $ sam.health.decrease(30)
                ## Уменьшит здоровье Сэмюэля на 30 единиц, или установит минимум (0)
                if value > 0:
                    if self.current_value - value < self.min_value:
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

                ## Сравнивает выбранное значение с переданным (Если значение характеристики строго больше переданного, то возвращает True)
                ## Использование:
                ## if sam.health.more_than(30):
                ##  действия
                if self.current_value > value:
                    return True
                else:
                    return False

            def more_than_or_equal(self, value):
                ## Сравнивает выбранное значение с переданным (Если значение характеристики не меньше переданного, то возвращает True)
                ## Использование:
                ## if sam.health.more_than_or_equal(30):
                ##  действия
                if self.current_value >= value:
                    return True
                else:
                    return False

            def less_then(self, value):

                ## Сравнивает выбранное значение с переданным (Если значение характеристики строго меньше переданного, то возвращает True)
                ## Использование:
                ## if sam.health.less_than(30):
                ##  действия
                if self.current_value < value:
                    return True
                else:
                    return False

            def less_then_or_equal(self, value):
                ## Сравнивает выбранное значение с переданным (Если значение характеристики не больше переданного, то возвращает True)
                ## Использование:
                ## if sam.health.less_than_or_equal(30):
                ##  действия
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
            def __init__(self, init_loc):

                ## locations хранит список доступных локаций. Не должен изменяться
                ## current_loc хранит информацию о текущем местоположении
                ## default_loc хранит информацию о изначально заданном местоположении. Не должен изменяться
                self.locations = ['Albis', 'Hestir', 'Nox', 'Willaldan', 'Hostalikon', 'Galerenon', 'Fernlander', 'Lafetar']
                self.current_loc = init_loc
                self.default_loc = init_loc

            def is_in(self):

                ## Возвращает текущее местоположение персонажа
                ## Использование:
                ##  if sam.is_in() == 'Hostalikon':
                ##      Действия
                return self.current_loc

            def reset_loc(self):

                ## Сбрасывает текущее местоположение до начального
                self.current_loc = self.default_loc

            def jump_to(self, new_loc):

                ## Изменяет текущее местоположение
                if new_loc in self.locations:
                    self.current_loc = new_loc
                else:
                    pass
