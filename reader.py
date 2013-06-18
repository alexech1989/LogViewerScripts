'''
    Modulo: reader.py

    Descripcion: Modulo de lectura y parseo del archivo access.log
        administrado por el servicio Squid

    Desarrollado por: Daniel Echevarria Iparraguirre

    Fecha Creacion: 17/06/2013

    Fecha Modificacion: 17/06/2013
'''

import time
import database
import util
import statistic
from contextlib import closing
from setting import LOG_PATH
from setting import TMP_LOG_PATH
from setting import ENTRY_DELIMITER
from datetime import datetime
from classes import LogEntry


def readingtask():
    starttime = time.time()
    datereading = database.getdatereading()
    entrys = []

    copylogfile()
    actualdate = datetime.today()
    database.insertdatereading(actualdate)

    with closing(open(TMP_LOG_PATH, 'r')) as tmpf:
        for line in tmpf:
            entrys.append(createlogentry(line))

    if datereading is not None:
        entrys = filter(lambda e: e.date > datereading.date, entrys)

    database.insertlogentrys(entrys)
    database.updatedatereading(datereading.getid())
    endtime = time.time()
    statistic.savestatistic(actualdate, len(entrys), (endtime - starttime))

    print 'finished'


def copylogfile():
    with closing(open(TMP_LOG_PATH, 'w')) as tmpf:
        with closing(open(LOG_PATH, 'r')) as f:
            tmpf.write(f.read())


def createlogentry(line):
    lst = util.removeelementsbyvalue(line.split(ENTRY_DELIMITER), '')
    entry = LogEntry()
    entry.setdate(datetime.fromtimestamp(float(lst[0])))
    entry.setlocalip(lst[2])
    entry.setremoteip(lst[8].split('/')[1])
    entry.seturl(lst[6])

    return entry


