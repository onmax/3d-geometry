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

name = 'Own implementation of lookAt'


def own_lookAt():

def display():
    global rotating
    global translate

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
