import numpy as np
from math import sin, cos, tan, pi

class Matrix(object):

    @staticmethod
    def Vec3(a, b, c):
        return np.array([a,b,c])

    @staticmethod
    def normalise(a):
        return a/np.linalg.norm(a)

    @staticmethod
    def cross(a,b):
        return np.cross(a,b)


    @staticmethod
    def makeIdentity():
        return np.array( [[1,0,0,0],
                          [0,1,0,0],
                          [0,0,1,0],
                          [0,0,0,1]]).astype(float)
    
    @staticmethod
    def makeTranslation(x, y, z):
        return np.array( [[1,0,0,x],
                          [0,1,0,y],
                          [0,0,1,z],
                          [0,0,0,1]]).astype(float)

    @staticmethod
    def makeRotationX(winkel):
        c= cos(winkel)
        #print(c)
        s= sin(winkel)
        #print(s)
        return np.array( [[1,0, 0,0],
                          [0,c,-s,0],
                          [0,s, c,0],
                          [0,0, 0,1]]).astype(float)
    
    @staticmethod
    def makeRotationY(winkel):
        c= cos(winkel)
        s= sin(winkel)
        return np.array( [[ c,0, s,0],
                          [ 0,1, 0,0],
                          [-s,0, c,0],
                          [ 0,0, 0,1]]).astype(float)
    
    @staticmethod
    def makeRotationZ(winkel):
        c= cos(winkel)
        s= sin(winkel)
        return np.array( [[c,-s, 0,0],
                          [s, c, 0,0],
                          [0, 0, 1,0],
                          [0, 0, 0,1]]).astype(float)

    @staticmethod
    def makeScale(s):
        return np.array( [[s,0,0,0],
                          [0,s,0,0],
                          [0,0,s,0],
                          [0,0,0,1]]).astype(float)

    @staticmethod
    def makeScale2(s1,s2,s3):
        return np.array( [[s1,0,0,0],
                          [0,s2,0,0],
                          [0,0,s3,0],
                          [0,0,0,1]]).astype(float)

    @staticmethod
    def makePerspective(angleOfView=60, aspectRatio=1,near=0.1,far=100):
        # Umwandlung in Bogenmass
        a= angleOfView*pi/180
        d=1.0/tan(a/2)
        r= aspectRatio
        b=(far+near)/(near-far)
        c=2*far*near/(near-far)
        return np.array( [[d/r,0,  0,0],
                          [0,  d,  0,0],
                          [0,  0,  b,c],
                          [0,  0, -1,0]]).astype(float)
    
    @staticmethod
    def makeLook_at(eye,target,up):
        z = (eye-target)/(np.sqrt((eye-target).dot(eye-target)))
        x = np.cross(up,z)
        y = np.cross(z,x)
        a=-x.dot(eye)
        b=-y.dot(eye)
        c=-z.dot(eye)
        return np.array([[x[0],y[0],z[0],0],
                         [x[1],y[1],z[1],0],
                         [x[2],y[2],z[2],0],
                         [a,b,c,1]]).astype(float)

    @staticmethod
    def makeTranspose(matrix):
        amatrix=matrix
        return np.transpose(amatrix)

    @staticmethod
    def multiply(matrix1,matrix2):
        return np.dot(matrix1,matrix2,)

