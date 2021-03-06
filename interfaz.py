# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla y coordenadas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 40, 521, 451))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.formLayoutWidget)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.spinX = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinX.setMinimum(1)
        self.spinX.setObjectName("spinX")
        self.horizontalLayout_4.addWidget(self.spinX)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinY = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinY.setMinimum(1)
        self.spinY.setObjectName("spinY")
        self.horizontalLayout_4.addWidget(self.spinY)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.labelTurno = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelTurno.setObjectName("labelTurno")
        self.verticalLayout.addWidget(self.labelTurno)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.labelPieza = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPieza.sizePolicy().hasHeightForWidth())
        self.labelPieza.setSizePolicy(sizePolicy)
        self.labelPieza.setMinimumSize(QtCore.QSize(513, 123))
        self.labelPieza.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPieza.setObjectName("labelPieza")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelPieza)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Partida = QtWidgets.QMenu(self.menubar)
        self.menu_Partida.setObjectName("menu_Partida")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNueva = QtWidgets.QAction(MainWindow)
        self.actionNueva.setObjectName("actionNueva")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionReglas = QtWidgets.QAction(MainWindow)
        self.actionReglas.setObjectName("actionReglas")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.menu_Partida.addAction(self.actionNueva)
        self.menu_Partida.addAction(self.actionGuardar)
        self.menu_Partida.addAction(self.actionAbrir)
        self.menuAyuda.addAction(self.actionReglas)
        self.menubar.addAction(self.menu_Partida.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.labelTurno.setText(_translate("MainWindow", "Turno:"))
        self.pushButton.setText(_translate("MainWindow", "Colocar"))
        self.labelPieza.setText(_translate("MainWindow", "TextLabel"))
        self.menu_Partida.setTitle(_translate("MainWindow", "&Partida"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNueva.setText(_translate("MainWindow", "Nueva"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionReglas.setText(_translate("MainWindow", "Reglas"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
