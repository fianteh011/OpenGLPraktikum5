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


WIDTH, HEIGHT = 1000, 1200
left, right, forward, backward, A_LEFT, D_RIGHT = False, False, False, False, False, False
xrot, yrot = False, False


def key_input_clb(window, key, scancode, action, mode):
    global left, right, forward, backward, A_LEFT, D_RIGHT
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    # for z-Direction
    if key == glfw.KEY_W and action == glfw.PRESS:
        forward = True
    elif key == glfw.KEY_W and action == glfw.RELEASE:
        forward = False
    if key == glfw.KEY_S and action == glfw.PRESS:
        backward = True
    elif key == glfw.KEY_S and action == glfw.RELEASE:
        backward = False

    # for movement of x-direction
    if key == glfw.KEY_A and action == glfw.PRESS:
        A_LEFT = True
    elif key == glfw.KEY_A and action == glfw.RELEASE:
        A_LEFT = False
    if key == glfw.KEY_D and action == glfw.PRESS:
        D_RIGHT = True
    elif key == glfw.KEY_D and action == glfw.RELEASE:
        D_RIGHT = False

    ###Beim Drücken der rechten Pfeiltaste soll sich Würfel um seine X-Achse vor und zurück drehen.
    if key == glfw.KEY_RIGHT and action == glfw.PRESS:
        right = True
        print("PRESSED Taste ->")
    ###Beim Loslassen der rechten Pfeiltaste soll die Drehung des Würfels gestoppt werden
    elif key == glfw.KEY_RIGHT and action == glfw.RELEASE:
        right = False
        # print("RELEASED Taste ->")

    ## TASTE: [<-]
    ### Beim Drücken der linken Pfeiltaste soll sich Würfel um seine Y-Achse vor und zurück drehen.
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        left = True
        print("PRESSED Taste <-")
    ### Beim Loslassen der linken Pfeiltaste soll die Drehung des Würfels gestoppt werden.
    elif key == glfw.KEY_LEFT and action == glfw.RELEASE:
        left = False
        # print("RELEASED Taste <-")


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
#set the callback for keyboard interaction
glfw.set_key_callback(window, key_input_clb)

#### Anwendung initialisieren
programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
glUseProgram(programRef)

#### Geometrie/Objekte laden

# für mac osx vao initialisieren
# vaoRef = glGenVertexArrays(1)
# glBindVertexArray(vaoRef)
#


# print(object_buffer)

# Vertex array object anlegen
VAO1, VAO2 = glGenVertexArrays(2)
VBO1, VBO2 = glGenBuffers(2)
EBO1, EBO2 = glGenBuffers(2)
textur_list = glGenTextures(2)

####### Objekt 1: Luigi##############
# externes 3D-Modell (wavefront obj) laden
object_indices, object_buffer = ObjLoader.load_model("textures/luigi.obj")

glBindVertexArray(VAO1)
glBindBuffer(GL_ARRAY_BUFFER, VBO1)
glBufferData(GL_ARRAY_BUFFER, object_buffer.nbytes, object_buffer, GL_STATIC_DRAW)

# positions
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(0))
print(object_buffer.itemsize)
glEnableVertexAttribArray(0)
# textures
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(12))
glEnableVertexAttribArray(1)
# normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(2)

#####Textur für Luigi######
glBindTexture(GL_TEXTURE_2D, textur_list[0])
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
#####################################################################

####### Objekt 2: Mario##############
# Modell: Mario
object_indices2, object_buffer2 = ObjLoader.load_model("textures/mario.obj")
# print(object_buffer)

glBindVertexArray(VAO2)
glBindBuffer(GL_ARRAY_BUFFER, VBO2)
glBufferData(GL_ARRAY_BUFFER, object_buffer2.nbytes, object_buffer2, GL_STATIC_DRAW)

# positions
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)
# textures
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(12))
glEnableVertexAttribArray(1)
# normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, object_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(2)

#####Textur für Mario######
glBindTexture(GL_TEXTURE_2D, textur_list[1])
# Set the texture wrapping parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
# Set texture filtering parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
# load image
image = Image.open("textures/mario.jpg")
flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
img_data = numpy.array(list(flipped_image.getdata()), numpy.uint8)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
glEnable(GL_TEXTURE_2D)

#### Transformations-Pipeline einrichten
view = Matrix.makeTranslation(0.0, 0.0, -3.0)
projection = Matrix.makePerspective(65.0, WIDTH / HEIGHT, 0.1, 100.0)

### Luigi Model-Transformation
model = Matrix.makeIdentity()
model = Matrix.makeTranslation(0.5, 0.0, 0.5)
# Skalierung (falls notwendig)
model = Matrix.multiply(model, Matrix.makeScale(0.01))

### Mario Model-Transformation
model_mario = Matrix.makeIdentity()
model_mario = Matrix.makeTranslation(-0.5, 0.0, -0.3)
# Skalierung (falls notwendig)
model_mario = Matrix.multiply(model_mario, Matrix.makeScale(0.01))

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

    ##########################################
    ## Model Transformation für Luigi
    # Luigi Obj-daten binden
    glBindVertexArray(VAO1)
    if D_RIGHT:
        model = Matrix.multiply(Matrix.makeTranslation(0.001, 0, 0), model)
    elif A_LEFT:
        model = Matrix.multiply(Matrix.makeTranslation(-0.001, 0, 0), model)
    elif forward:
        model = Matrix.multiply(Matrix.makeTranslation(0, 0, 0.001), model)
    elif backward:
        model = Matrix.multiply(Matrix.makeTranslation(0, 0, -0.001), model)

    rot_y = Matrix.makeRotationY(0.8 * glfw.get_time())
    # rot_y = Matrix.multiply(Matrix.makeRotationX(pi/2),rot_y)

    # binding the texture for Luigi
    glBindTexture(GL_TEXTURE_2D, textur_list[0])
    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(object_indices))
    #############################

    ## Model Transformation für Mario
    # rot_y = Matrix.multiply(Matrix.makeRotationX(pi/2),rot_y)
    # Mario obj daten binden
    glBindVertexArray(VAO2)
    if right:
        model_mario = Matrix.multiply(Matrix.makeTranslation(0.001, 0, 0), model_mario)
    elif left:
        model_mario = Matrix.multiply(Matrix.makeTranslation(-0.001, 0, 0), model_mario)

    glBindTexture(GL_TEXTURE_2D, textur_list[1])

    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model_mario)

    glDrawArrays(GL_TRIANGLES, 0, len(object_indices2))

    glfw.swap_buffers(window)

# glfw beenden, allokierte Resourcen freigeben
glfw.terminate()
