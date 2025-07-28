# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_modernita.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget_2 = QWidget(self.centralwidget)
        self.centralwidget_2.setObjectName(u"centralwidget_2")
        self.centralwidget_2.setGeometry(QRect(250, 110, 384, 234))
        self.mainLayout_2 = QHBoxLayout(self.centralwidget_2)
        self.mainLayout_2.setObjectName(u"mainLayout_2")
        self.mainLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftPanel_2 = QFrame(self.centralwidget_2)
        self.leftPanel_2.setObjectName(u"leftPanel_2")
        self.leftLayout_2 = QVBoxLayout(self.leftPanel_2)
        self.leftLayout_2.setObjectName(u"leftLayout_2")
        self.btnHome = QPushButton(self.leftPanel_2)
        self.btnHome.setObjectName(u"btnHome")

        self.leftLayout_2.addWidget(self.btnHome)

        self.btnSettings = QPushButton(self.leftPanel_2)
        self.btnSettings.setObjectName(u"btnSettings")

        self.leftLayout_2.addWidget(self.btnSettings)


        self.mainLayout_2.addWidget(self.leftPanel_2)

        self.rightPanel_2 = QFrame(self.centralwidget_2)
        self.rightPanel_2.setObjectName(u"rightPanel_2")
        self.rightLayout_2 = QVBoxLayout(self.rightPanel_2)
        self.rightLayout_2.setObjectName(u"rightLayout_2")
        self.labelTitle_2 = QLabel(self.rightPanel_2)
        self.labelTitle_2.setObjectName(u"labelTitle_2")

        self.rightLayout_2.addWidget(self.labelTitle_2)

        self.listContent_2 = QListWidget(self.rightPanel_2)
        self.listContent_2.setObjectName(u"listContent_2")

        self.rightLayout_2.addWidget(self.listContent_2)


        self.mainLayout_2.addWidget(self.rightPanel_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a tu aplicaci\u00f3n", None))
    # retranslateUi

