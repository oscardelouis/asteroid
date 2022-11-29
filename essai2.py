import random
from pygame.math import Vector2
import core

def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1000, 800]
    core.memory("vitesse", Vector2(0, -1))
    core.memory("position", Vector2(500, 400))
    core.memory("accel", Vector2())
    core.memory("maxSpeed", 1)
    core.memory("maxAccel", 4)

def run():
    core.cleanScreen()


    #acceleration
    if core.memory("accel").length() > core.memory("maxAccel"):
        core.memory("accel").scale_to_length("maxAccel")

    core.memory("vitesse", core.memory("vitesse")+ core.memory("accel"))
    if core.memory("vitesse").length() > core.memory("maxSpeed"):
        core.memory("vitesse").scale_to_length(core.memory("maxSpeed"))
    core.memory("accel", Vector2(0,0))
    core.memory("position", core.memory("position") + core.memory("vitesse")


    # self.vel += self.acc
    # if self.vel.length() > self.maxSpeed:
    #     self.vel.scale_to_length(self.maxSpeed)
    # self.acc = Vector2(0, 0)
    # self.pos += self.vel

    # deplacement

    if core.getKeyPressList("z"):
        core.memory("position", core.memory("position") + core.memory("vitesse") * 0.15)

    # core.memory("vitesse").scale_to_length(core.memory("position").length() + 2)
    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(5))
    if core.getKeyPressList("q"):
        core.memory("vitesse", core.memory("vitesse").rotate(-5))

core.main(setup, run)
