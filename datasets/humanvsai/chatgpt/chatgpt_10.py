import logging

def start_logging(file_name='gromacs.log', tag='gromacs'):
    logging.basicConfig(filename=file_name, format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger(tag).addHandler(console)
    logging.info('Logging started')
