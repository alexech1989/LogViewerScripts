'''
    Modulo: setting.py

    Descripcion: Modulo de configuracion, define constantes y parometros
        configurables utilizados por el resto de modulos del script

    Desarrollado por: Daniel Echevarria Iparraguirre

    Fecha Creacion: 17/06/2013

    Fecha Modificacion: 17/06/2013
'''

# Parametros del modulo database.py

CONNECTION_PARAMETERS = {
    'host': '192.168.19.21',
    'db': 'logviewer',
    'user': 'root',
    'passwd': 'root'
}

SP_GET_READING = 'sp_get_reading'

SP_INS_READING = 'sp_ins_reading'

SP_UPD_READING = 'sp_upd_reading'

SP_INS_ENTRY = 'sp_ins_entry'

# Parametros del modulo reader.py

LOG_PATH = 'D:\\daniel\\proyectos\\LogViewerScripts\\log\\access.log'

TMP_LOG_PATH = 'D:\\daniel\\proyectos\\LogViewerScripts\\log\\tmpaccess.log'

ENTRY_DELIMITER = ' '

# Parametros del modulo statistic.py

STATISTICS_PATH = ('D:\\daniel\\proyectos\\LogViewerScripts\\statistics' +
'\\statistics.txt')

STATISTIC_TEMPLATE = '{0} \t {1} \t {2} \r\n'

