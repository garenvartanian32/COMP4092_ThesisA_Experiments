def start_logging(logfile="gromacs.log"):
    from . import log
    log.create("gromacs", logfile=logfile)
    logging.getLogger("gromacs").info("GromacsWrapper %s STARTED logging to %r",
                                      __version__, logfile)