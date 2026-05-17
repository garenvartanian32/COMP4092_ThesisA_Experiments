import os
import sys

def patch_spyder_for_sos():
    try:
        from spyder.config.base import get_conf_path
        from spyder.plugins.ipythonconsole.utils.sos import (
            register_sos_kernel, validate_sos_kernel)
        from sos.notebook.kernel_extension import SOSKernelExtension
        from sos_notebook.kernel import SoS
        from ipykernel.kernelspec import register_kernel_spec

        # Register SOS kernel with IPython Console
        if validate_sos_kernel():
            register_sos_kernel()
            print("SOS kernel for Spyder's IPython console is now registered!")

        # Register SOS kernel with Jupyter Notebook
        if "jupyter-notebook" in sys.argv[0]:
            kernel_json = SoS().kernel_json()
            register_kernel_spec(kernel_json['name'], kernel_json)

            kernel_ext = SOSKernelExtension(kernel_json)
            kernel_ext.register_ipython_extension()

            print("SOS kernel for Jupyter Notebook is now registered!")
        else:
            print("NOTE: SOS kernel was not registered with Jupyter Notebook "
                  "as it is not being run by jupyter-notebook command.")

    except Exception as e:
        print("Failed to patch spyder for sos files and sos kernel:", e)

patch_spyder_for_sos()

