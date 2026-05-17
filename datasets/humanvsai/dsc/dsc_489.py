def get_second_pass_opts_ebu(self):
    # Define your options here
    options = {
        "i": "-i",
        "af": "-af",
        "loudnorm": "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=summary",
        "f": "-f",
        "null": "-f",
        "y": "-y",
        "nostdin": "-nostdin"
    }

    # Build the options string
    opts_str = " ".join([f"{options[k]} {v}" for k, v in options.items()])

    return opts_str