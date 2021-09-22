import pyxel
from random import choice, randint, seed, random
from functools import lru_cache

# ...
pixels = [[False] * 256 for _ in range(256)]
NUM_ITER = 42
N_FRAMES = 16
ZOOM = 1.0
X0 = 0.0
Y0 = 0.0
delta = 0.25

def update():
    global X0, Y0, ZOOM
    
    # Desloca o fractal de um lado para o outro
    if pyxel.btnp(pyxel.KEY_UP):
        Y0 -= delta
    if pyxel.btnp(pyxel.KEY_DOWN):
        Y0 += delta
    if pyxel.btnp(pyxel.KEY_LEFT):
        X0 -= delta
    if pyxel.btnp(pyxel.KEY_RIGHT):
        X0 += delta

    # Controla o zoom 
    if pyxel.mouse_wheel < 0:
        new_zoom = ZOOM * 1.25
        ZOOM = new_zoom
    if pyxel.mouse_wheel > 0:
        new_zoom = ZOOM / 1.25
        ZOOM = new_zoom
    

def draw():
    # Itera sobre todos os pixels da tela, pintando de cores
    # aleatórias
    for i in range(0, 256):
        for j in range(pyxel.frame_count % N_FRAMES, 256, N_FRAMES):
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
            return (n // 2) % 8 + 8
        if n > NUM_ITER:
            return pyxel.COLOR_BLACK

    return pyxel.COLOR_BLACK

def get_complex(i, j):
    re = +(i - 128) / 64
    im = -(j - 128) / 64
    return ZOOM * complex(re - X0, im - Y0)


pyxel.init(256, 256, fps=30)
pyxel.run(update, draw)