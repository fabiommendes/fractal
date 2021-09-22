import pyxel


def update():
    ...
    

def draw():
    pyxel.cls(pyxel.COLOR_WHITE)


def get_complex(i, j):
    return i + 1j * j


pyxel.init(256, 256)
pyxel.mouse(True)
pyxel.run(update, draw)