import matplotlib.pyplot as plt
import numpy as np
from math import pi,cos,sin 
from Config import *


class Camera:
    def __init__(self):
        self.M = BASE 
        self.px_base = PX_BASE
        self.px_altura = PX_ALTURA
        self.ccd = CCD
        self.dist_focal = DIST_FOCAL
        self.ox = OX
        self.oy = OY
        self.fsx = self.dist_focal * (self.px_base / self.ccd[0])
        self.fsy = self.dist_focal * (self.px_altura / self.ccd[1])
        self.fstheta = THETA

    def generate_intrinsix_matrix(self):
        self.K = np.array([[self.fsx,self.fstheta,self.ox],[0,self.fsy,self.oy],[0,0,1]])
    
        return self.K
    
    def move(self,dx,dy,dz):
        self.T = np.eye(4)
        self.T[0,-1] = dx
        self.T[1,-1] = dy
        self.T[2,-1] = dz
        return self.T

    def rotation(self, axis, angle):
        if axis == 'x':
            self.rotation_matrix=np.array([[1,0,0,0],[0, cos(angle),-sin(angle),0],[0, sin(angle), cos(angle),0],[0,0,0,1]])
            
        if axis == 'y':
            self.rotation_matrix=np.array([[cos(angle),0, sin(angle),0],[0,1,0,0],[-sin(angle), 0, cos(angle),0],[0,0,0,1]])
            
        if axis == 'z':
            self.rotation_matrix=np.array([[cos(angle),-sin(angle),0,0],[sin(angle),cos(angle),0,0],[0,0,1,0],[0,0,0,1]])
        return self.rotation_matrix

    def generate_extrinsix_matrix(self):
        self.g = self.rotation_matrix@self.T
        return self.g

    def update(self):
        self.move()
        self.rotation()
        self.generate_extrinsix_matrix()
        self.generate_intrinsix_matrix() 