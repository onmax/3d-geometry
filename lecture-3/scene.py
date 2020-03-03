# -*- coding: utf-8 -*-
"""
This file try to recreate the following exercise:

1- A teapot rotating around an axis placed 3 units above like:
    1. The tap pointing to the axis
    2. A ferris wheel
"""

import math
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

name = 'Testing'
camera = {"x": 3, "y": 1, "z": 0}
pointing_at = {"x": 0, "y": 1, "z": 0}
angle = 180


def update_angle():
    global pointing_at
    rad = math.radians(angle)
    pointing_at["x"] = camera["x"] + math.sin(rad)
    pointing_at["z"] = camera["z"] - math.cos(rad)


def keys(key, x, y):
    global camera, pointing_at, angle

    step = 0.1

    if key == 'd':
        angle += 5
    elif key == 'a':
        angle -= 5
    elif key == 'z':
        camera["y"] -= 1
        pointing_at["y"] -= 1
    elif key == 'q':
        camera["y"] += 1
        pointing_at["y"] += 1
    elif key == 'w':
        rad = math.radians(angle)
        camera["x"] += math.sin(rad)
        camera["z"] -= math.cos(rad)
    elif key == 's':
        rad = math.radians(angle)
        camera["x"] -= math.sin(rad)
        camera["z"] += math.cos(rad)

    update_angle()
    print(camera, pointing_at)

    glutPostRedisplay()


def drawAxis(x, y, z):
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(x, 0, 0)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, y, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, z)
    glColor3f(1, 1, 1)
    glEnd()


def draw_floor():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-100, 0, -100)
    glVertex3f(-100, 0, 100)
    glVertex3f(100, 0, 100)
    glVertex3f(100, 0, -100)
    glEnd()


def display():
    # ****************   INIT   *****************
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(camera["x"], camera["y"], camera["z"],
              pointing_at["x"], pointing_at["y"], pointing_at["z"], 0, 1, 0)
    # ***********************************
    glEnable(GL_DEPTH_TEST)

    draw_floor()
    drawAxis(2, 2, 2)
    glColor3f(1, 0, 0)

    for i in range(-2, 3):
        for j in range(-2, 3):
            glPushMatrix()
            glTranslatef(i * 10, 1, j * 10)
            glutWireTeapot(0.5)
            glPopMatrix()

    # **********************************
    glutSwapBuffers()  # Ordena el dibujado


def main():
    update_angle()

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(600, 100)
    glutInitWindowSize(600, 600)
    glutCreateWindow(name)
    glutKeyboardFunc(keys)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()


main()
