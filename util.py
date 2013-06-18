'''
    Modulo: util.py

    Descripcion: Modulo de funciones reutilizables

    Desarrollado por: Daniel Echevarria Iparraguirre
        sistemas8@carolinaperu.com

    Fecha Creacion: 17/06/2013

    Fecha Modificacion: 17/06/2013
'''


def removeelementsbyvalue(lst, value):
    while value in lst:
        lst.remove(value)

    return lst
