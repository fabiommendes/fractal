import pyxel
from random import choice, randint, seed, random

# ...
pixels = [[False] * 256 for _ in range(256)]
NUM_ITER = 42

def update():
    ...
    

def draw():
    pyxel.cls(pyxel.COLOR_WHITE)
    # seed(0)

    # Itera sobre todos os pixels da tela, pintando de cores
    # aleatórias
    r = 32
    for i in range(pyxel.mouse_x - r, pyxel.mouse_x + r + 1):
       for j in range(pyxel.mouse_y - r, pyxel.mouse_y + r + 1):
           pyxel.pset(i, j, mandelbrot_color(i, j))

    # for i in range(0, 256):
    #     for j in range(256):
    #         pyxel.pset(i, j, mandelbrot_color(i, j))


def mandelbrot_color(i, j):
    z = get_complex(i, j)
    
    # iteração de mandelbrot
    erro = 1
    tol = 1e-6
    x = 0
    n = 0

    while erro > tol:
        x_novo = x**2 + z
        erro = abs(x - x_novo)
        x = x_novo
        n += 1

        if abs(x) > 2:
            return pyxel.COLOR_WHITE
        if n > NUM_ITER:
            return pyxel.COLOR_BLACK

    return pyxel.COLOR_BLACK

def get_complex(i, j):
    re = +i / 64 - 2
    im = -j / 64 + 2
    return complex(re, im)


pyxel.init(256, 256)
pyxel.mouse(True)
pyxel.run(update, draw)