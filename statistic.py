'''
    Modulo: statistic.py

    Descripcion: Modulo que almacena los resultados de ejecucion del script
        en un archivo de estadisticas para su posterior analisis

    Desarrollado por: Daniel Echevarria Iparraguirre
        sistemas8@carolinaperu.com

    Fecha Creacion: 17/06/2013

    Fecha Modificacion: 17/06/2013
'''

from contextlib import closing
from setting import STATISTICS_PATH
from setting import STATISTIC_TEMPLATE


def savestatistic(executedate, recordscount, duration):
    with closing(open(STATISTICS_PATH, 'a')) as f:
        f.write(STATISTIC_TEMPLATE.format(executedate, recordscount,
            duration))
