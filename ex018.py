import math
ang = float(input('Digite um angulo: '))
angr = math.radians(ang)
sen = math.sin(angr)
cos = math.cos(angr)
tan = math.tan(angr)
print(f'Esse ângulo esses valores aproximados:'
      f'\nsen: {sen:.2f}'
      f'\ncos: {cos:.2f}'
      f'\ntan: {tan:.2f}.')