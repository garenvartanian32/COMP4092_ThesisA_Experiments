def set_close_callback(window, cbfun):
    """
    Sets the close callback for the specified window. Wrapper for:
    GLFWwindowclosefun glfwSetWindowCloseCallback(GLFWwindow* window, GLFWwindowclosefun cbfun);
    """
    glfw.set_window_close_callback(window, cbfun)
