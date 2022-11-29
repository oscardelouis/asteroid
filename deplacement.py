from pygame import Vector2

import core


def deplacement() :


    core.memory("position", core.memory("position") + core.memory("accel"))

    if core.getKeyPressList("z"):
        if core.memory("vitesse").length() < 1.2:
            core.memory("vitesse", core.memory("vitesse").scale_to_length(core.memory("vitesse").length() + 0.1))

        if core.memory("accel").length() < 5:

            if core.memory("accel") != Vector2(0, 0):

                core.memory("accel", core.memory("accel").scale_to_length(core.memory("accel").length() + 0.08))
                core.memory("accel", core.memory("accel") + core.memory("vitesse"))
            else:
                core.memory("accel", core.memory("vitesse"))

    if not core.getkeyPressValue():

        if core.memory("accel").length() > 1:
            core.memory("accel", core.memory("accel").scale_to_length(core.memory("accel").length() - 0.08))
        else:
            core.memory("accel", Vector2(0, 0))

    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(5))
    if core.getKeyPressList("q"):
        core.memory("vitesse", core.memory("vitesse").rotate(-5))