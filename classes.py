'''
    Modulo: classes.py

    Descripcion: Modulo de clases de modelo del script

    Desarrollado por: Daniel Echevarria Iparraguirre
        #sistemas8@carolinaperu.com

    Fecha Creacion: 17/06/2013

    Fecha Modificacion: 17/06/2013
'''


class LogEntry:

    def __init__(self):
        self.uid = None
        self.date = None
        self.localip = None
        self.remoteip = None
        self.url = None

    def setuid(self, uid):
        self.uid = uid

    def setdate(self, date):
        self.date = date

    def setlocalip(self, localip):
        self.localip = localip

    def setremoteip(self, remoteip):
        self.remote = remoteip

    def seturl(self, url):
        self.url = url

    def getuid(self):
        return self.uid

    def getdate(self):
        return self.date

    def getlocalip(self):
        return self.localip

    def getremoteip(self):
        return self.remoteip

    def geturl(self):
        return self.url

    def getprocparams(self):
        return [
            self.date,
            self.localip,
            self.remoteip,
            self.url
        ]


class DateReading:

    def __init__(self):
        self.id = None
        self.date = None
        self.state = None

    def setid(self, id):
        self.id = id

    def setdate(self, date):
        self.date = date

    def setstate(self, state):
        self.state = state

    def getid(self):
        return self.id

    def getdate(self):
        return self.date

    def getstate(self):
        return self.state

