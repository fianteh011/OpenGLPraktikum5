#### Erweiterte Grundversion: 2 Objekte mit Textur in OpenGL #################
#### und Keyboard-Interaktion für das 1. Objekt ##############################
import glfw
from OpenGL.GL import *
from glfwUtils import GlfwUtils
from openGLUtils import OpenGLUtils
from Aufgabe_1.geometry_bvb import Geometry
from matrix import Matrix
from math import sin, cos, pi
from PIL import Image

from camera import Camera

# from OpenGL.raw.GL.VERSION.GL_2_0 import glUseProgram


WIDTH, HEIGHT = 1560, 1260
left, right, forward, backward, up, down = False, False, False, False, False, False
xrot, yrot = False, False

first_mouse = True
lastX, lastY = WIDTH / 2, HEIGHT / 2

cam = Camera()

#### Shader aus Datei laden
# vertex shader code einlesen
vsCode = open("vs_bvb.txt", 'r').read()

# fragment shader code einlesen
fsCode = open("fs_bvb.txt", 'r').read()

# Ausgabefenster (glfw) initialisieren
window = GlfwUtils().initWindow(WIDTH, HEIGHT)


# glfw callback functions
# window resize callback
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = Matrix.makePerspective(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_TRUE, projection)


# keyboard input callback
def key_input_clb(window, key, scancode, action, mode):
    global left, right, forward, backward, xrot, yrot, up, down
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
        left = True
    elif key == glfw.KEY_A and action == glfw.RELEASE:
        left = False
    if key == glfw.KEY_D and action == glfw.PRESS:
        right = True
    elif key == glfw.KEY_D and action == glfw.RELEASE:
        right = False

    # for y-Direction
    if key == glfw.KEY_UP and action == glfw.PRESS:
        up = True
    elif key == glfw.KEY_UP and action == glfw.RELEASE:
        up = False
    if key == glfw.KEY_DOWN and action == glfw.PRESS:
        down = True
    elif key == glfw.KEY_DOWN and action == glfw.RELEASE:
        down = False

    # for rotation along the x-axis
    if key == glfw.KEY_RIGHT and action == glfw.PRESS:
        xrot = True
    elif key == glfw.KEY_RIGHT and action == glfw.RELEASE:
        xrot = False

    # for rotation along the y-axis
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        yrot = True
    elif key == glfw.KEY_LEFT and action == glfw.RELEASE:
        yrot = False


# mouse position callback function

def mouse_look_clb(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = -xpos + lastX
    yoffset = -lastY + ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)


# window resize callback setzen
glfw.set_window_size_callback(window, window_resize)
# keyboard input callback setzen
glfw.set_key_callback(window, key_input_clb)
# mouse position callback setzen
glfw.set_cursor_pos_callback(window, mouse_look_clb)
# mouse cursor an das Fenster binden
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

#### Anwendung initialisieren
programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
glUseProgram(programRef)

#### Geometrie/Objekte laden

# für mac osx vao initialisieren
# vaoRef = glGenVertexArrays(1)
# glBindVertexArray(vaoRef)
#
geometrie = Geometry()

# Vertex Array Objects
VAO1, VAO2, VAO3 = glGenVertexArrays(3)

# 1. Objekt
vertices, indices = geometrie.cubeObjectbvb(programRef)
glBindVertexArray(1)

# Vertex Buffer Object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# Element Buffer Object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(12))

########## TEXTUR ANLEGEN (3 Objekte = 3 #######################
# Texturen anlegen und laden
textures = glGenTextures(3)

# für das 1. Objekt
glBindTexture(GL_TEXTURE_2D, textures[0])

# Set the texture wrapping parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
# Set texture filtering parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# Bild für Textur laden
image = Image.open("textures/Logo BvB.jpg")
image = image.transpose(Image.FLIP_TOP_BOTTOM)
img_data = image.convert("RGBA").tobytes()
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

# 2. Objekt
vertices2, indices2 = geometrie.cubeObject2(programRef)
glBindVertexArray(VAO2)

# Vertex Buffer Object
VBO2 = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO2)
glBufferData(GL_ARRAY_BUFFER, vertices2.nbytes, vertices2, GL_STATIC_DRAW)

# Element Buffer Object
EBO2 = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO2)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices2.nbytes, indices2, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices2.itemsize * 5, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))

# für das 2. Objekt
glBindTexture(GL_TEXTURE_2D, textures[1])

# Set the texture wrapping parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
# Set texture filtering parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# Bild für Textur laden
image = Image.open("textures/holzkiste.jpg")
image = image.transpose(Image.FLIP_TOP_BOTTOM)
img_data = image.convert("RGBA").tobytes()
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

################## Objekt 3: Pyramide #########################################################
vertices3, indices3 = geometrie.pyramide()
glBindVertexArray(3)

# Vertex Buffer Object Pyramide
VBO3 = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO3)
glBufferData(GL_ARRAY_BUFFER, vertices3.nbytes, vertices3, GL_STATIC_DRAW)

# Element Buffer Object
EBO3 = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO3)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices3.nbytes, indices3, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))

########## TEXTURE for Pyramid#######################
glBindTexture(GL_TEXTURE_2D, textures[2])
# Set the texture wrapping parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
# Set texture filtering parameters
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
# load image
image = Image.open("textures/wall.jpg")
image = image.transpose(Image.FLIP_TOP_BOTTOM)
img_data = image.convert("RGBA").tobytes()
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA,
             GL_UNSIGNED_BYTE, img_data)

# model-Transformation Pyramide
model3 = Matrix.makeTranslation(0.75, 0, 0)
model3 = Matrix.multiply(model3, Matrix.makeRotationX(pi / 2))
model3 = Matrix.multiply(model3, Matrix.makeRotationZ(pi / 6))

##########################################################

#### Transformations-Pipeline einrichten
projection = Matrix.makePerspective(45, WIDTH / HEIGHT, 0.1, 100)
model = Matrix.makeTranslation(0.0, 0.5, 0.0)
# model = Matrix.multiply(model,Matrix.makeRotationX(0.0))
# model = Matrix.multiply(model,Matrix.makeRotationY(pi/3))

# eye, target, up: Look_at_Matrix
view = Matrix.makeLook_at(Matrix.Vec3(0, 0, 5), Matrix.Vec3(0, 0, 0), Matrix.Vec3(0, 1, 0))

# shader-Verbindung einrichten
model_loc = glGetUniformLocation(programRef, "model")
proj_loc = glGetUniformLocation(programRef, "projection")
view_loc = glGetUniformLocation(programRef, "view")

glUniformMatrix4fv(proj_loc, 1, GL_TRUE, projection)
glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

#### OpenGl Parameter setzen
glClearColor(0.5, 0.5, 0.5, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#### Anwendung (application loop) starten
while not glfw.window_should_close(window):
    glfw.poll_events()
    # Interaktion
    # interaktion.do_movement(cam)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 1. Objekt   
    glBindVertexArray(VAO1)
    # Falls keyboard-Interaktion vorliegt: model-Matrix anpassen 
    if right:
        model = Matrix.multiply(Matrix.makeTranslation(0.001, 0, 0), model)
    elif left:
        model = Matrix.multiply(Matrix.makeTranslation(-0.001, 0, 0), model)
    elif forward:
        model = Matrix.multiply(Matrix.makeTranslation(0, 0, 0.001), model)
    elif backward:
        model = Matrix.multiply(Matrix.makeTranslation(0, 0, -0.001), model)
    elif xrot:
        model = Matrix.multiply(model, Matrix.makeRotationX(0.002))
    elif yrot:
        model = Matrix.multiply(model, Matrix.makeRotationY(0.002))
    ########## Kamerasteueriung über die Maus einrichten

    camX = sin(0.8) * 10
    camZ = cos(0.2) * 10

    # viewMatrix muss nun geändert werden

    view1 = Matrix.makeLook_at(Matrix.Vec3(camX, 5.0, camZ),  # cam_pos
                               Matrix.Vec3(0.0, 0.0, 0.0),  # lookat vector
                               Matrix.Vec3(0.0, 1.0, 0.0))  # up vector

    # view-Matrix aus Kamerasicht
    # hier abgefragt
    view2 = cam.get_view_matrix()

    # immer mit der aktuellen ViewMatrix aktualisieren und wieder zuweisen
    view = Matrix.multiply(view1, view2)

    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    ###########
    # 1. Objekt
    glBindVertexArray(VAO1)
    glBindTexture(GL_TEXTURE_2D, textures[0])
    # aktuelle model-Matrix zuweisen und zeichnen   
    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # 2. Objekt
    glBindVertexArray(VAO2)
    model2 = Matrix.makeTranslation(0.0, -1.0, 0.0)
    model2 = Matrix.multiply(model2, Matrix.makeRotationX(pi / 2))
    # model2 = Matrix.multiply(model2,Matrix.makeScale2(0.5,0.75,3.0))

    glBindVertexArray(VAO2)
    glBindTexture(GL_TEXTURE_2D, textures[1])
    # aktuelle model-Matrix zuweisen und zeichnen  
    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model2)
    glDrawElements(GL_TRIANGLES, len(indices2), GL_UNSIGNED_INT, None)

    # 3. Objekt(Pyramide)
    glBindVertexArray(VAO3)
    if up:
        model3 = Matrix.multiply(Matrix.makeTranslation(0, 0.001, 0), model3)
    elif down:
        model3 = Matrix.multiply(Matrix.makeTranslation(0, -0.001, 0), model3)

    glBindVertexArray(VAO3)
    glBindTexture(GL_TEXTURE_2D, textures[2])
    # aktuelle model-Matrix zuweisen und zeichnen
    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model3)
    glDrawElements(GL_TRIANGLES, len(indices2), GL_UNSIGNED_INT, None)

    ###
    # print('Kameraausrichtung = ',Matrix.normalise(cam.camera_front))
    ###
    glfw.swap_buffers(window)

# glfw beenden, allokierte Resourcen freigeben
glfw.terminate()
