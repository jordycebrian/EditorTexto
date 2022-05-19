
from PySide2.QtWidgets import QMainWindow ,QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_notas import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """conexion de widget con funciones"""
        self.ui.actionGuardar.triggered.connect(self.guardarNota)
        self.ui.actionAbrir.triggered.connect(self.abrirNota)
        self.ui.actionNuevo.triggered.connect(self.nuevaNota)
        self.ui.actionGuardar_Como.triggered.connect(self.guardarComoNota)
        self.ui.actionSalir.triggered.connect(self.salir)
        
        
    """Funciones de opciones de la pestaña"""
    @Slot()
    def guardarNota(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            '(*.txt)'
        )[0]
        try:
            self.guardar(ubicacion)
        except:
            QMessageBox.critical(self, 'Error!!', 'Fallo Guardar' + ubicacion)

    @Slot()
    def abrirNota(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            '(*.txt)'
        )[0]    
        try:
            self.abrir(ubicacion)
        except:
            QMessageBox.critical(self, 'Error!!', 'Fallo Guardar' + ubicacion)

    @Slot()
    def nuevaNota(self):
        self.ui.textEdit.clear()


    @Slot()
    def guardarComoNota(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Gaurdar Como',
            '.',
            '(*.txt)'
        )[0]
        try:
            self.guardarComo(ubicacion) 
        except:
            QMessageBox.critical(self, 'Error!!', 'Fallo Guardar' + ubicacion)

    @Slot()
    def salir(self):
        if self.ui.actionSalir:
            exit()


    """

    Funciones para la manipulacion de los archivos de texto

    """
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as fichero:
                fichero.write(self.ui.textEdit.toPlainText())
                fichero.close()
            QMessageBox.information(self, 'Exito!!', 'Nota Guardada' + ubicacion)
        except:
            QMessageBox.critical(self, 'Error!!', 'Guardar Cancelado')
    
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as fichero:
                text = "".join(lineas for lineas in fichero)
                self.ui.textEdit.setPlainText(text)
            QMessageBox.information(self, 'Exito!!', 'Nota Guardad ')
        except:
            QMessageBox.critical(self, 'Error!!', 'Guardar Cancelado' + ubicacion)

    def guardarComo(self,ubicacion):
        try:
            with open(ubicacion, 'w+') as fichero:
                fichero.write(self.ui.textEdit.toPlainText())
                fichero.close()
            QMessageBox.information(self, 'Exito!!', 'Nota Guardad ' + ubicacion)
        except:
            QMessageBox.critical(self, 'Error!!', 'Guardar Cancelado')
    """
    Fin de Funciones manipulacion de archivo
    
    """