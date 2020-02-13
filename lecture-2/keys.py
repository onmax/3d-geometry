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
angle_x = 0
angle_y = 0
angle_z = 0


def keys(key, x, y):
    global angle_y, angle_z, angle_x

    if key == 'd':
        angle_y += 10
    elif key == 'a':
        angle_y -= 10
    elif key == 'e':
        angle_z += 10
    elif key == 'q':
        angle_z -= 10
    elif key == 'w':
        angle_x += 10
    elif key == 's':
        angle_x -= 10
    else:
        return

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


def display():
    # ****************   INIT   *****************
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)
    # ***********************************

    glColor3f(1, 1, 1)
    drawAxis(2, 2, 2)
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_z, 0, 0, 1)
    drawAxis(2, 2, 2)

    glutWireTeapot(1.0)

    # **********************************
    glutSwapBuffers()  # Ordena el dibujado


def main():
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
