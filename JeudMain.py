import random
from pygame.math import Vector2
import core
from pygame import Rect
import time

drops = []
gravity = 1


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1000, 800]

    core.memory("texture", core.Texture("W:\s3\info\\tpp5\exemple\\texture\\fon.jpg", Vector2(0, 0), scaleSize=core.WINDOW_SIZE))

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


    if not core.memory("texture").ready:
        core.memory("texture").load()

    core.memory("texture").show()

    show()
    update()

    # triangle

    core.cleanScreen()

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

    # deplacement

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

    # Tore

    if core.memory("position").x < 0:
        core.memory("position").x = core.WINDOW_SIZE[0]
    if core.memory("position").x > core.WINDOW_SIZE[0]:
        core.memory("position").x = 0
    if core.memory("position").y < 0:
        core.memory("position").y = core.WINDOW_SIZE[1]
    if core.memory("position").y > core.WINDOW_SIZE[1]:
        core.memory("position").y = 0

    # Tir

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
        core.Draw.line((255, 255, 255, 100), (drop.x, drop.y), (drop.x + 3, drop.y + 3), 3)

    core.Draw.rect((255, 250, 0), core.memory("target"))


core.main(setup, run)

