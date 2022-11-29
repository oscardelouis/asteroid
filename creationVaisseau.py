from pygame import Vector2

import core


def creatVais():

    P1bis = Vector2(core.memory("vitesse"))
    P3bis = P1bis.rotate(-90)
    P3bis.scale_to_length(10)
    P1bis = P1bis.rotate(90)
    P1bis.scale_to_length(10)
    P2bis = Vector2(core.memory("vitesse"))
    P2bis.scale_to_length(30)
    P1 = core.memory("position") + P1bis + core.memory("accel")
    P2 = core.memory("position") + P2bis + core.memory("accel")
    P3 = core.memory("position") + P3bis + core.memory("accel")

    core.Draw.polygon((255, 0, 0), (P1, P2, P3), 3)