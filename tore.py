import core


def tore() :

    if core.memory("position").x < 0:
        core.memory("position").x = core.WINDOW_SIZE[0]
    if core.memory("position").x > core.WINDOW_SIZE[0]:
        core.memory("position").x = 0
    if core.memory("position").y < 0:
        core.memory("position").y = core.WINDOW_SIZE[1]
    if core.memory("position").y > core.WINDOW_SIZE[1]:
        core.memory("position").y = 0