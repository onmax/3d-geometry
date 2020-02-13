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


name = 'Testing'


def display():
    glClearColor(0.5, 0.5, 0.5, 0.)  # color del fondo

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, 1, 1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutWireTeapot(3)
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
