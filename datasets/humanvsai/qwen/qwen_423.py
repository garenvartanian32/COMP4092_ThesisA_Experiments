def set_window_close_callback(window, cbfun):
    _glfw.glfwSetWindowCloseCallback(window, cbfun)