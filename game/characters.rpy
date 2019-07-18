## Файл для описания персонажей.
## Пример:
## define dev = Character ('Чокнутный разработчик', color='#016361')
## Документация по функции Character: https://renpy.org/doc/html/dialogue.html?highlight=character#Character

## Использование:
## dev "Какая-то реплика"

## Мысли главного героя
define th = Character(None, what_prefix='~', what_suffix='~')

## Джеймс Черношляп, главный герой первой, более значимой ветки
define bh = Character('Джеймс Черношляп', color='#034634')

## Сэмюель, главный герой второй ветки (меньшей по значимости и объему)
define sam = Character('Сэмюэль', color='#034634')
