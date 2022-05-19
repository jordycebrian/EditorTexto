# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(555, 311)
        icon = QIcon()
        icon.addFile(u"../../../Downloads/tarea.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNuevo = QAction(MainWindow)
        self.actionNuevo.setObjectName(u"actionNuevo")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGuardar_Como = QAction(MainWindow)
        self.actionGuardar_Como.setObjectName(u"actionGuardar_Como")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 611, 301))
        self.textEdit.setStyleSheet(u"QObject{\n"
"	background-color: Black;\n"
"	color: #ffff00;\n"
"	font: 75 italic 12pt \"Arial\";\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 555, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menuAbrir.addAction(self.actionNuevo)
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addAction(self.actionGuardar)
        self.menuAbrir.addAction(self.actionGuardar_Como)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notas", None))
        self.actionNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionGuardar_Como.setText(QCoreApplication.translate("MainWindow", u"Guardar Como", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

