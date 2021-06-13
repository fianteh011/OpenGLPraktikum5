from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

# Methoden zum Laden, Kompilieren umd Linken (GPU) von shadern
# Systemdaten OpenGL und GLSL anzeigen

class OpenGLUtils(object):
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        #print('shadertype = ',shaderType)
        # version von OpenGL/GLSL
        #extension = "#extension GL_ARB_shading_language_420pack: require \n"
        shaderCode = "#version 410\n " + shaderCode
        # shader object erzeugen
        shaderRef = glCreateShader(shaderType)
        # source code zuweisen
        glShaderSource(shaderRef, shaderCode)
        # kompilieren
        glCompileShader(shaderRef)

        # erfolgreich kompiliert? Fehlersuche
        compileSuccess=glGetShaderiv(shaderRef,GL_COMPILE_STATUS)
        if not compileSuccess:
            errorMessage = glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)
            # convert byte string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            raise Exception(errorMessage)

        # Erfolg
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        # shader kompilieren
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        # program object
        programRef = glCreateProgram()

        # shader zuweisen
        glAttachShader(programRef,vertexShaderRef)
        glAttachShader(programRef,fragmentShaderRef)

        # link
        glLinkProgram(programRef)

        # Linking erfolgreich?
        linkSuccess = glGetProgramiv(programRef,GL_LINK_STATUS)

        if not linkSuccess:
            errorMessage = glGetProgramInfoLog(programRef)
            glDeleteProgram(programRef)
            # convert byte string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            raise Exception(errorMessage)

        # Erfolg
        return programRef
    
    @staticmethod
    def printSystemInfo():
        print("===========================================================================")
        print(" Vendor: "+ glGetString(GL_VENDOR).decode('utf-8'))   
        print(" Renderer: "+ glGetString(GL_RENDERER).decode('utf-8'))
        print(" OpenGL supported:" + glGetString(GL_VERSION).decode('utf-8'))
        print(" GLSL supported:" + 
              glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
        print("===========================================================================")
