#! /usr/bin/env python
# -*- coding: utf-8 -*-
######################################
import logging

LOG = logging.getLogger(name="Tranzactions ERROR")
FORMAT = '%(asctime)s %(message)s %(levelname)s %(pathname)s'
fl = "logging_file.log"
logging.basicConfig(filename=fl,format = FORMAT,filemode = "w")

LOG.info("INFO")
LOG.error("Error happened")
LOG.critical("Pipec")
LOG.warning("warning error")
LOG.debug("This is a low-level debug message")

LOG.setLevel(logging.INFO) # Вызов setLevel() устанавливает минимальный уровень логирования
#print(LOG.level)
print("Boris")
