import subprocess, traceback
from PyQt4 import QtCore

#-Class to run subprocess in a thread
class SubProcessWorker(QtCore.QObject):
    '''Example worker'''
    #- commands are required. If the worker is about a map creation, then the following is required: 
    # mapname, filename, added to canvas (True or False), and ftype ('raster' or 'shape')
    def __init__(self, commands, textLog, mapname=None, filename=None, addmap=None, ftype=None, env=None):
        QtCore.QObject.__init__(self)
        self.commands = commands
        self.process = None
        self.mapName = mapname
        self.fileName = filename
        self.addMap = addmap
        self.fType = ftype
        self.env = env
        self.textLog = textLog  # required to know to which text log in the GUI append the processing text log
    def run(self):
        try:#-execute each individual command in a separate subprocess
            for command in self.commands:
                self.process = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    universal_newlines=False,
                    env=self.env
                    )
                  
                proc = self.process.stdout
     
                for line in iter(proc.readline, ''):
                    if line.find("Traceback")>=0:
                        self.process = None
                        break
                    elif line.find("WARNING")>=0:
                        self.cmdProgress.emit(['...', self.textLog])
                    elif line.find("temp")>=0:
                        self.cmdProgress.emit(['...', self.textLog])
                    elif line.find("ERROR")>=0:
                        self.cmdProgress.emit(['...', self.textLog])
                    elif line.find("Permission")>=0:
                        self.cmdProgress.emit(['...', self.textLog])
                    else:
                        self.cmdProgress.emit([line, self.textLog])
        except Exception, e:
            # forward the exception upstream
            self.error.emit(e, traceback.format_exc())
        self.finished.emit([self.process, self.mapName, self.fileName, self.addMap, self.fType, self.textLog])
         
    finished = QtCore.pyqtSignal(object)
    error = QtCore.pyqtSignal(Exception, basestring)
    cmdProgress = QtCore.pyqtSignal(object)