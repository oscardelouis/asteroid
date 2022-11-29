from datetime import time

from pygame import Vector2

import core


def tir() :

if core.getKeyPressList("SPACE"):
    if len(core.memory("projectile")) > 0:
        if time.time() - core.memory("projectile")[-1]["startTime"] > 1:
            p = Vector2(core.memory("position"))
            v = Vector2(core.memory("vitesse"))
            v.scale_to_length(core.memory("vitesse").length() + 10)
            r = 3
            c = (255, 0, 100)
            st = time.time()

            d = {"position": p, "vitesse": v, "rayon": r, "couleur": c, "startTime": st}
            core.memory("projectile").append(d)
    else:
        p = Vector2(core.memory("position"))
        v = Vector2(core.memory("vitesse"))
        v.scale_to_length(core.memory("vitesse").length() + 20)
        r = 3
        c = (255, 0, 50)
        st = time.time()

        d = {"position": p, "vitesse": v, "rayon": r, "couleur": c, "startTime": st}
        core.memory("projectile").append(d)