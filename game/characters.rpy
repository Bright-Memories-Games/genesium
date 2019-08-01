## Файл для описания персонажей.
## Пример:
## define dev = Character ('Чокнутный разработчик', color='#016361')
## Документация по функции Character: https://renpy.org/doc/html/dialogue.html?highlight=character#Character

## Использование:
## dev "Какая-то реплика"

## Мысли главного героя
define th = Character(None, what_prefix='~', what_suffix='~')

## Джеймс Черношляп, главный герой основной арки
init 1 python:
  bh = Hero('Джеймс Черношляп', 'цвет_имени', 'цвет_текста', '', '', 'Nox')

  bh.health = bh.Trait(0, 200, 180)
  bh.trust = bh.Trait(-50, 50, 0)

  bh.strength = bh.Trait(1, 10, 3)
  bh.perception = bh.Trait(1, 10, 8)
  bh.charisma = bh.Trait(1, 10, 6)
  bh.luck = bh.Trait(1, 10, 4)


## Сэмюэль, главный герой демо-версии

  sam = Hero('Сэмюэль', 'цвет_имени', 'цвет_текста', '', '', 'Hostalikon')

  sam.health = sam.Trait(0, 200, 100)
  sam.trust = sam.Trait(-50, 50, 0)

  sam.strength = sam.Trait(1, 10, 7)
  sam.perception = sam.Trait(1, 10, 5)
  sam.charisma = sam.Trait(1, 10, 4)  
  sam.luck = sam.Trait(1, 10, 4)
