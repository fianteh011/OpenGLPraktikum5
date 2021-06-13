from OpenGL.GL import *
import numpy as np
from PIL import Image


class Geometry:

    def cubeObjectbvb(self, programref):
        vertices = [-0.5, -0.5, 0.5, 0.0, 0.0,
                    0.5, -0.5, 0.5, 1.0, 0.0,
                    0.5, 0.5, 0.5, 1.0, 1.0,
                    -0.5, 0.5, 0.5, 0.0, 1.0,

                    -0.5, -0.5, -0.5, 0.0, 0.0,
                    0.5, -0.5, -0.5, 1.0, 0.0,
                    0.5, 0.5, -0.5, 1.0, 1.0,
                    -0.5, 0.5, -0.5, 0.0, 1.0,

                    0.5, -0.5, -0.5, 0.0, 0.0,
                    0.5, 0.5, -0.5, 1.0, 0.0,
                    0.5, 0.5, 0.5, 1.0, 1.0,
                    0.5, -0.5, 0.5, 0.0, 1.0,

                    -0.5, 0.5, -0.5, 0.0, 0.0,
                    -0.5, -0.5, -0.5, 1.0, 0.0,
                    -0.5, -0.5, 0.5, 1.0, 1.0,
                    -0.5, 0.5, 0.5, 0.0, 1.0,

                    -0.5, -0.5, -0.5, 0.0, 0.0,
                    0.5, -0.5, -0.5, 1.0, 0.0,
                    0.5, -0.5, 0.5, 1.0, 1.0,
                    -0.5, -0.5, 0.5, 0.0, 1.0,

                    0.5, 0.5, -0.5, 0.0, 0.0,
                    -0.5, 0.5, -0.5, 1.0, 0.0,
                    -0.5, 0.5, 0.5, 1.0, 1.0,
                    0.5, 0.5, 0.5, 0.0, 1.0]

        indices = [0, 1, 2, 2, 3, 0,
                   4, 5, 6, 6, 7, 4,
                   8, 9, 10, 10, 11, 8,
                   12, 13, 14, 14, 15, 12,
                   16, 17, 18, 18, 19, 16,
                   20, 21, 22, 22, 23, 20]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        # Textur anlegen und laden
        #        texture = glGenTextures(1)
        #        glBindTexture(GL_TEXTURE_2D, texture)

        # Set the texture wrapping parameters
        #        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        #        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        #        # Set texture filtering parameters
        #        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        #        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # load image
        #        image = Image.open("textures/Logo BvB.jpg")
        # image = Image.open("textures/cat.png")
        #        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        #        img_data = image.convert("RGBA").tobytes()
        # img_data = np.array(image.getdata(), np.uint8) # second way of getting the raw image data
        #        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        return vertices, indices

    def cubeObject1(self, programref):
        vertices = [-2.0, -0.1, 2.0, 1.0, 0.0, 0.0,
                    2.0, -0.1, 2.0, 0.0, 1.0, 0.0,
                    2.0, 0.1, 2.0, 0.0, 0.0, 1.0,
                    -2.0, 0.1, 2.0, 1.0, 1.0, 0.0,

                    -2.0, -0.1, -2.0, 1.0, 0.0, 1.0,
                    2.0, -0.1, -2.0, 0.0, 1.0, 1.0,
                    2.0, 0.1, -2.0, 1.0, 1.0, 0.0,
                    -2.0, 0.1, -2.0, 1.0, 1.0, 1.0]

        # indices = [ 0,  1,  2,  2,  3,  0,
        #            0,  4,  1,  1,  4,  5,
        #            1,  5,  2,  2,  5,  6,
        #            2,  7,  6,  2,  3,  7,
        #            3,  0,  4,  4,  7,  3,
        #            4,  5,  6,  6,  7,  4]

        indices = [0, 1, 2, 2, 3, 0,
                   4, 5, 6, 6, 7, 4,
                   4, 5, 1, 1, 0, 4,
                   6, 7, 3, 3, 2, 6,
                   5, 6, 2, 2, 1, 5,
                   7, 4, 0, 0, 3, 7]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        return vertices, indices

    def cubeObject2(self, programref):
        vertices = [-2.0, -2.0, 0.01, 0.0, 0.0,
                    2.0, -2.0, 0.01, 1.0, 0.0,
                    2.0, 2.0, 0.01, 1.0, 1.0,
                    -2.0, 2.0, 0.01, 0.0, 1.0,

                    -2.0, -2.0, -0.01, 0.0, 0.0,
                    2.0, -2.0, -0.01, 1.0, 0.0,
                    2.0, 2.0, -0.01, 1.0, 1.0,
                    -2.0, 2.0, -0.01, 0.0, 1.0,

                    2.0, -2.0, -0.01, 0.0, 0.0,
                    2.0, 2.0, -0.01, 1.0, 0.0,
                    2.0, 2.0, 0.01, 1.0, 1.0,
                    2.0, -2.0, 0.01, 0.0, 1.0,

                    -2.0, 2.0, -0.01, 0.0, 0.0,
                    -2.0, -2.0, -0.01, 1.0, 0.0,
                    -2.0, -2.0, 0.01, 1.0, 1.0,
                    -2.0, 2.0, 0.01, 0.0, 1.0,

                    -2.0, -2.0, -0.01, 0.0, 0.0,
                    2.0, -2.0, -0.01, 1.0, 0.0,
                    2.0, -2.0, 0.01, 1.0, 1.0,
                    -2.0, -2.0, 0.01, 0.0, 1.0,

                    2.0, 2.0, -0.01, 0.0, 0.0,
                    -2.0, 2.0, -0.01, 1.0, 0.0,
                    -2.0, 2.0, 0.01, 1.0, 1.0,
                    2.0, 2.0, 0.01, 0.0, 1.0]

        indices = [0, 1, 2, 2, 3, 0,
                   4, 5, 6, 6, 7, 4,
                   8, 9, 10, 10, 11, 8,
                   12, 13, 14, 14, 15, 12,
                   16, 17, 18, 18, 19, 16,
                   20, 21, 22, 22, 23, 20]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        return vertices, indices

    ######### Pyramide
    def pyramide(self):
        vertices = [-0.5, -0.5, 1.75, 0.0, 0.0,
                    0.5, -0.5, 1.75, 1.0, 0.0,
                    0.5, 0.5, 1.75, 1.0, 1.0,

                    0.5, 0.5, 1.75, 0.0, 0.0,
                    -0.5, 0.5, 1.75, 1.0, 0.0,
                    -0.5, -0.5, 1.75, 1.0, 1.0,

                    -0.5, -0.5, 1.75, 0.0, 0.0,
                    0.5, -0.5, 1.75, 1.0, 0.0,
                    0.0, 0.0, -1.75, 0.5, 1.0,

                    0.5, -0.5, 1.75, 0.0, 0.0,
                    0.5, 0.5, 1.75, 1.0, 0.0,
                    0.0, 0.0, -1.75, 0.5, 1.0,

                    0.5, 0.5, 1.75, 0.0, 0.0,
                    -0.5, 0.5, 1.75, 1.0, 0.0,
                    0.0, 0.0, -1.75, 0.5, 1.0,

                    -0.5, 0.5, 1.75, 0.0, 0.0,
                    -0.5, -0.5, 1.75, 1.0, 0.0,
                    0.0, 0.0, -1.75, 0.5, 1.0]

        indices = [0, 1, 2,
                   3, 4, 5,
                   6, 7, 8,
                   9, 10, 11,
                   12, 13, 14,
                   15, 16, 17]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        return vertices, indices
