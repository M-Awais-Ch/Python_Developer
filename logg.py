# import logging
# logging.basicConfig(filename="sam.log",level=logging.Debug)

# from logging import*
# sow="{lineno}# {name}= {asctime}: {message}"
# basicConfig(filename="logfile.log",level=NOTSET,filemode="w",style="{",format=sow)
# debug("Debug")
# warning("This is your warning")
# info("Info")
# error("Next is error")
# critical("Critical")
import logging
logging.basicConfig(filename="looog.log",level="NOTSET",style="{",format="{asctime}:{name} : {message}")
logging.debug("shoe debug")
logging.info("show info")
logging.warning("show warning")
logging.error("show error")
logging.critical("show critical")
