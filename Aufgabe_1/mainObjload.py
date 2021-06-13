#### Grundversion: 3D-Objekte laden (obj_Format) in OpenGL #################
#### mit Textur (als Bild) ##############################
import glfw
from OpenGL.GL import *
from glfwUtils import GlfwUtils
from openGLUtils import OpenGLUtils
from ObjLoader import ObjLoader
from matrix import Matrix
from math import sin, cos, pi
import numpy
from PIL import Image

# from OpenGL.raw.GL.VERSION.GL_2_0 import glUseProgram


WIDTH, HEIGHT = 800, 800
left, right, forward, backward = False, False, False, False
xrot, yrot = False, False

#### Shader aus Datei laden
# vertex shader code einlesen
vsCode = open("vs_objloader.txt", 'r').read()

# fragment shader code einlesen
fsCode = open("fs_objloader.txt", 'r').read()

# Ausgabefenster (glfw) initialisieren
window = GlfwUtils().initWindow(WIDTH, HEIGHT)


# glfw callback functions
# window resize callback
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = Matrix.makePerspective(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_TRUE, projection)


# window resize callback setzen
glfw.set_window_size_callback(window, window_resize)

#### Anwendung initialisieren
programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
glUseProgram(programRef)

#### Geometrie/Objekte laden

# externes 3D-Modell (wavefront obj) laden
object_indices, object_buffer = ObjLoader.load_model("textures/luigi.obj")
# print(object_buffer)

VAO = glGenVertexArrays(1)
VBO = glGenBuffers(1)
EBO = glGenBuffers(1)

glBindVertexArray(VAO)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, object_buffer.nbytes, object_buffer, GL_STATIC_DRAW)

# positions
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)
# textures
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(12))
glEnableVertexAttribArray(1)
# normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(2)

texture = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture)
# Set the texture wrapping parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
# Set texture filtering parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
# load image
image = Image.open("textures/luigi.jpg")
flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
img_data = numpy.array(list(flipped_image.getdata()), numpy.uint8)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
glEnable(GL_TEXTURE_2D)

#### Transformations-Pipeline einrichten
view = Matrix.makeTranslation(0.0, 0.0, -3.0)
projection = Matrix.makePerspective(65.0, WIDTH / HEIGHT, 0.1, 100.0)
model = Matrix.makeTranslation(0.0, 0.0, 0.0)

view_loc = glGetUniformLocation(programRef, "view")
proj_loc = glGetUniformLocation(programRef, "projection")
model_loc = glGetUniformLocation(programRef, "model")

glUniformMatrix4fv(view_loc, 1, GL_TRUE, view)
glUniformMatrix4fv(proj_loc, 1, GL_TRUE, projection)
glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)

#### OpenGl Parameter setzen
glClearColor(0.5, 0.5, 0.5, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#### Anwendung (application loop) starten
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_y = Matrix.makeRotationY(0.8 * glfw.get_time())
    # rot_y = Matrix.multiply(Matrix.makeRotationX(pi/2),rot_y)

    # Skalierung (falls notwendig)
    model = Matrix.multiply(rot_y, Matrix.makeScale(0.01))

    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)

    glDrawArrays(GL_TRIANGLES, 0, len(object_indices))

    glfw.swap_buffers(window)

# glfw beenden, allokierte Resourcen freigeben
glfw.terminate()