import glfw
from OpenGL.GL import *

glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

window = glfw.create_window(800, 600, "Fakhema First Window", None, None)
glfw.make_context_current(window)

print("GL", glGetString(GL_VERSION).decode(), "on", glGetString(GL_RENDERER).decode())

while not glfw.window_should_close(window):
    glClearColor(0.0, 0.5, 0.5, 1.0)     # teal colour, aap apna chunein
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()