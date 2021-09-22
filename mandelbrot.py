import pyxel
from random import choice, randint, seed, random
from functools import lru_cache

# ...
pixels = [[False] * 256 for _ in range(256)]
NUM_ITER = 42

def update():
    ...
    

def draw():
    # Itera sobre todos os pixels da tela, pintando de cores
    # aleatórias
    for i in range(0, 256):
        for j in range(pyxel.frame_count % 32, 256, 32):
            z = get_complex(i, j)
            pyxel.pset(i, j, mandelbrot_color(z))


@lru_cache(512 * 512)
def mandelbrot_color(z):
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


pyxel.init(256, 256, fps=30)
pyxel.run(update, draw)