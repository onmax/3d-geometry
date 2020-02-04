# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:45:23 2018

@author: lola
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'PLANTILLA openGL 3D'
    

def display():
    
    #****************   INIT   *****************
    glClearColor(0.5,0.5,0.5,0.)  # color del fondo
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective ( 60, 1, 1, 1000 )
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5,5,5,0,0,0,0,1,0)
    #*********************************** 
    
    glColor3f(1,1,1) #color de la tetera
    glutWireTeapot(1.0)
    
    #**********************************
    glutSwapBuffers()  #Ordena el dibujado
       
       
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(600,100)
    glutInitWindowSize(600,600)
    glutCreateWindow(name)
    glutDisplayFunc(display)
    glutMainLoop()

main()