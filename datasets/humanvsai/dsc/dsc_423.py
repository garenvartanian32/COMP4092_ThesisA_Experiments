import glfw

def window_close_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def set_window_close_callback(window, cbfun):
    glfw.set_window_close_callback(window, cbfun)

# Initialize GLFW
if not glfw.init():
    print("Failed to initialize GLFW")
    exit(1)

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(640, 480, "Hello World", None, None)
if not window:
    glfw.terminate()
    print("Failed to create GLFW window")
    exit(1)

# Set the window close callback
set_window_close_callback(window, window_close_callback)

# Main loop
while not glfw.window_should_close(window):
    # Render here

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

glfw.terminate()