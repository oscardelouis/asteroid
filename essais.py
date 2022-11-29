import random
from pygame.math import Vector2
import core
from pygame import Rect
import time

from exemple.creationVaisseau import creatVais
from exemple.deplacement import deplacement
from exemple.tore import tore

drops = []
gravity = 1


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1000, 800]

    # core.memory("texture", core.Texture("W:\s3\info\\tpp5\exemple\\texture\\fon.jpg", Vector2(0, 0), scaleSize=core.WINDOW_SIZE))

    for i in range(0, 100):
        drops.append(Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(-400, 800)))

    core.fps = 60
    core.WINDOW_SIZE = [1000, 800]

    core.memory("vitesse", Vector2(0, -1))
    core.memory("position", Vector2(500, 400))
    core.memory("accel", Vector2(0, 0))
    core.memory("projectile", [])

    # target
    x = random.randint(0, 850)
    y = random.randint(0, 750)
    l = 50
    h = 50

    core.memory("target", Rect(x, y, l, h))

    # def menu() :
    #
    #
    # def jeu():
    #
    #
    # def go():
    #
    #

    core.memory("etat", 0)
    print("Setup END-----------")


def run():
    #
    # core.cleanScreen()
    # if core.memory("etat")==0 :
    #     menu()
    # if core.memory("etat")==1 :
    #     jeu()
    # if core.memory("etat")==2 :
    #     go()

    #
    # if not core.memory("texture").ready:
    #     core.memory("texture").load()
    #
    # core.memory("texture").show()

    show()
    update()


    core.cleanScreen()

    creatVais()
    deplacement()
    tore()

    tir()

    # projectile

    for proj in core.memory("projectile"):
        core.Draw.circle(proj["couleur"], proj["position"], proj["rayon"])

    for proj in core.memory("projectile"):
        proj["position"] = proj["position"] + proj["vitesse"]

    # clean proj

    for proj in core.memory("projectile"):
        if time.time() - proj["startTime"] > 0.75:
            core.memory("projectile").remove(proj)

    # collision

    for proj in core.memory("projectile"):
        if core.memory("target").collidepoint((proj["position"].x, proj["position"].y)):
            x = random.randint(0, 850)
            y = random.randint(0, 750)
            l = 50
            h = 50

            core.memory("target", Rect(x, y, l, h))
            core.memory("projectile").remove(proj)

    if core.memory("target").collidepoint((core.memory("position").x, core.memory("position").y)):
        x = random.randint(0, 850)
        y = random.randint(0, 750)
        l = 50
        h = 50

        core.memory("target", Rect(x, y, l, h))

        # core.memory("target").remove(core.memory("target"))


# core.printMemory()

def update():
    # print(core.keyPressValue)
    for drop in drops:
        drop.y += gravity
        if drop.y > core.WINDOW_SIZE[1]:
            drop.x = random.randint(0, core.WINDOW_SIZE[0])
            drop.y = random.randint(-900, 0)


def show():
    core.cleanScreen()
    for drop in drops:
        core.Draw.line((255, 255, 255), (drop.x, drop.y), (drop.x + 3, drop.y + 3), 3)

    core.Draw.rect((255, 250, 0), core.memory("target"))


core.main(setup, run)

