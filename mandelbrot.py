import pyxel
from random import choice, randint, seed, random

# ...
pixels = [[False] * 256 for _ in range(256)]


def update():
    ...
    

def draw():
    pyxel.cls(pyxel.COLOR_WHITE)
    # seed(0)

    # Itera sobre todos os pixels da tela, pintando de cores
    # aleatórias
    for i in range(pyxel.mouse_x, pyxel.mouse_x + 1):
       for j in range(pyxel.mouse_y, pyxel.mouse_y + 1):
           pyxel.pset(i, j, mandelbrot_color(i, j))

    # for i in range(0, 256):
    #     for j in range(256):
    #         pyxel.pset(i, j, mandelbrot_color(i, j))


def mandelbrot_color(i, j):
    z = get_complex(i, j)
    if pyxel.btnp(pyxel.KEY_SPACE):
        print(z, abs(z))
    ... # iteração de mandelbrot
    ... # decide a cor a ser utilizada 
    return randint(0, 15)

def get_complex(i, j):
    re = +i / 64 - 2
    im = -j / 64 + 2
    return complex(re, im)


pyxel.init(256, 256)
pyxel.mouse(True)
pyxel.run(update, draw)