label sam_prologue:
  scene bg abandoned_church

  ## Эксперименты с Traits
  "Начальное значение здоровья [sam.health.current_value]"
  $ sam.health.decrease(30)
  "Здоровье: [sam.health.current_value]"
  $ sam.health.increase(20)
  "Здоровье: [sam.health.current_value]"

  ## Переход между сценами с использованием эффекта моргания
  window hide
  show blink with dissolve
  pause(3)
  scene bg column_path_day
  hide blink
  show unblink
  pause(2)
  window show
  "idhjsdih"
