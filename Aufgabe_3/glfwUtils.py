import glfw
from OpenGL.GL import *
XPOS=200
YPOS=200

class GlfwUtils(object):

     def initWindow(self,width,height):
        self.width=width
        self.height=height
        
        # initializing glfw library
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        # Configure the OpenGL context mac osx.
        # If we are planning to use anything above 2.1 we must at least
        # request a 3.3 core context to make this work across platforms.
        #glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        #glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 4)
        #glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        #glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        # 4 MSAA is a good default with wide support
        #glfw.window_hint(glfw.SAMPLES, 4)

        # creating the window
        window = glfw.create_window(self.width, self.height, "Mein Grafikfenster", None, None)
        # check if window was created
        if not window:
            glfw.terminate()
            raise Exception("glfw window can not be created!")
        
        # set window's position
        glfw.set_window_pos(window, XPOS, YPOS)

        # make the context current
        glfw.make_context_current(window)
        return window
