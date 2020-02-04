# -*- coding: utf-8 -*-
"""
This file try to recreate the following exercise:

1- A teapot rotating around an axis placed 3 units above like:
    1. The tap pointing to the axis
    2. A ferris wheel
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math


name = 'Teapots rotating'
rotating_tap = 0
translate_tap = 0
radius = 3


def display():
    global rotating_tap
    global translate_tap

    # ****************   INIT   *****************
    glClearColor(0.5, 0.5, 0.5, 0.)  # color del fondo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(80, 1, 1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(7, 7, 7, 0, radius, 2, 0, 1, 0)
    # ***********************************

    # Print axis
    glPushMatrix()
    glBegin(GL_LINES)

    glColor3f(0, 1, 0)  # y=3 axis
    glVertex3f(0, radius, -100)
    glVertex3f(0, radius, 100)

    glEnd()
    glPopMatrix()

    # Place first teapot
    glPushMatrix()
    glColor3f(0.5, 0, 1)  # purple teapot
    x = 0 + (radius * math.cos((translate_tap - 90) * math.pi / 180))
    y = radius + (radius * math.sin((translate_tap - 90) * math.pi / 180))
    glTranslatef(x, y, 0)
    glRotatef(rotating_tap, 0, 0, 1)
    rotating_tap += 1
    translate_tap += 1

    glutWireTeapot(1.0)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 0)  # yellow teapot
    glTranslatef(x, y, 4)
    glutWireTeapot(1.0)
    glPopMatrix()

    # **********************************
    glutSwapBuffers()  # Ordena el dibujado


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(600, 100)
    glutInitWindowSize(600, 600)
    glutCreateWindow(name)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()


main()
