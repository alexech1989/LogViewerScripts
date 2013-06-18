'''
    Modulo: database.py

    Descripcion: Modulo de conexion y acceso a la base de datos del log
        en linea

    Desarrollado por: Daniel Echevarria Iparraguirre
        sistemas8@carolinaperu.com

    Fecha Creacion: 17/06/2013

    Fecha Modificacion: 17/06/2013
'''

import MySQLdb
from contextlib import closing
from setting import CONNECTION_PARAMETERS
from setting import SP_INS_ENTRY
from setting import SP_GET_READING
from setting import SP_INS_READING
from setting import SP_UPD_READING
from classes import DateReading


def getconnection():
    '''
        Factoria de conexiones a la base de datos, a partir
        de parametros establecidos en el modulo setting.py
    '''
    return MySQLdb.connect(**CONNECTION_PARAMETERS)


def insertlogentrys(entrys):
    '''
        Funcion que registra en la base de datos todas la lista de
        entradas del log, recibida como parametro
    '''
    with closing(getconnection()) as cnn:
        with closing(cnn.cursor()) as cur:
            for entry in entrys:
                cur.callproc(SP_INS_ENTRY, entry.getprocparams())

        cnn.commit()


def getdatereading():
    '''
        Funcion que retorna la fecha de lectura activa
    '''
    fechalectura = None

    with closing(getconnection()) as cnn:
        with closing(cnn.cursor()) as cur:
            cur.callproc(SP_GET_READING)
            record = cur.fetchone()

            if record is not None:
                fechalectura = DateReading()
                fechalectura.setid(record[0])
                fechalectura.setdate(record[1])
                fechalectura.setstate(record[2])

    return fechalectura


def insertdatereading(datetime):
    '''
        Funcion que registra la nueva fecha de lectura activa
    '''
    with closing(getconnection()) as cnn:
        with closing(cnn.cursor()) as cur:
            cur.callproc(SP_INS_READING, [datetime])

        cnn.commit()


def updatedatereading(id):
    '''
        Funcion que deshabilita la fecha de lectura ya utilizada
    '''
    with closing(getconnection()) as cnn:
        with closing(cnn.cursor()) as cur:
            cur.callproc(SP_UPD_READING, [id])

        cnn.commit()






