import numpy as np
from lenstronomy.LightModel.light_model import LightModel
from lenstronomy.Util import util

def extended_source_magnification(x_pos, y_pos, kwargs_lens, source_sigma, window_size=0.1,
                                          grid_number=100):
    # create window
    x_grid = np.linspace(-window_size / 2., window_size / 2., grid_number)
    y_grid = np.linspace(-window_size / 2., window_size / 2., grid_number)
    x_window, y_window = util.make_grid(x_grid, y_grid)

    # define light model
    gauss = LightModel(light_model_list=['GAUSSIAN'])

    # compute brightness
    brightness = np.zeros_like(x_pos)
    for i in range(len(x_pos)):
        kwargs_source = {'amp': 1, 'sigma': source_sigma, 'center_x': x_pos[i], 'center_y': y_pos[i]}
        flux = np.array(gauss.surface_brightness(x_window, y_window, **kwargs_source)).sum()
        brightness[i] = flux

    # compute magnification
    mag = util.magnification_via_hessian(kwargs_lens, x_pos, y_pos)

    # return magnification times brightness
    return mag * brightness
